# Transformation and evaluation of the ALTO-XML files

### Introduction

In this phase, the OCR output (text + typographical information) is exported from Transkribus into ALTO-XML format (at the word level), in order to be further processed and injected into the GROBID-dictionaries. However, we have noticed two problems that prevent this injection:<br>

* the XML structure of exported files did not correspond to the structure which could be accepted by the GROBID-dictionaries;<br>
* the markup is stored in attribute values, and such a design is fundamentally flawed (e.g.`<String CONTENT="&lt;b&gt;Août"`, where `&lt;b&gt;` is equivalent to the tag `<b>` indicating the word in bold).<br>



### Redesigning the ALTO-XML files

After the initial experimenting with the XSLT transformations, we have mitigated the problem with the structure, but the attribute values indicating the font were not always correctly assigned (e.g. `<String CONTENT="Août" STYLEREFS="FONT2"` is incorrect - the value `FONT1` should be assigned to the attribute `STYLEREFS ` instead of `FONT2`):

The original (flawed) structure of the ALTO-XML file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<alto xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns="http://www.loc.gov/standards/alto/ns-v2#"
      xmlns:page="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15"
      xsi:schemaLocation="http://www.loc.gov/standards/alto/ns-v2# http://www.loc.gov/standards/alto/alto.xsd">
   <Description>
      <MeasurementUnit>pixel</MeasurementUnit>
      <OCRProcessing ID="IdOcr">
         <ocrProcessingStep>
            <processingDateTime>2020-05-17T21:22:02.419+02:00</processingDateTime>
            <processingSoftware>
               <softwareCreator>READ COOP</softwareCreator>
               <softwareName>Transkribus</softwareName>
            </processingSoftware>
         </ocrProcessingStep>
      </OCRProcessing>
   </Description> 																				------------------> below goes <Styles> with its fonts
   <Tags/>
   <Layout>
      <Page ID="Page1" PHYSICAL_IMG_NR="1" HEIGHT="2885" WIDTH="1858">    
         <TopMargin HEIGHT="5" WIDTH="1858" VPOS="0" HPOS="0"/>  				-----> unnecessary, convert into pixels
         <LeftMargin HEIGHT="2614" WIDTH="0" VPOS="5" HPOS="0"/> 				-----> unnecessary, convert into pixels
         <RightMargin HEIGHT="2614" WIDTH="179" VPOS="5" HPOS="1679"/> 	-----> unnecessary, convert into pixels
         <BottomMargin HEIGHT="266" WIDTH="1858" VPOS="2619" HPOS="0"/> -----> unnecessary, convert into pixels
         <PrintSpace HEIGHT="2614" WIDTH="1679" VPOS="5" HPOS="0">
            <TextBlock ID="r2" HEIGHT="241" WIDTH="34" VPOS="2334" HPOS="249">
               <Shape> 																									 ----> unnecessary
                  <Polygon POINTS="249,2334 249,2575 283,2575 283,2334"/> ---> unnecessary
               </Shape>
               <TextLine ID="r2l1"
                         BASELINE="2391"
                         HEIGHT="58"
                         WIDTH="44"
                         VPOS="2333"
                         HPOS="241">
                  <String HEIGHT="58"      ------> <String> needs the incremental ID and STYLEREFS="FONT{0,1,2}"
                  			  WIDTH="132" 
                  				VPOS="2333" 
                  				HPOS="153" 
                  				CONTENT="5"/> 										
               </TextLine>
               <TextLine ID="r2l2"
                         BASELINE="2486"
                         HEIGHT="71"
                         WIDTH="56"
                         VPOS="2415"
                         HPOS="239">
                  <String HEIGHT="71" 
                  				WIDTH="168" 
                  				VPOS="2415" 
                  				HPOS="127" 
                  				CONTENT="6"/>
               </TextLine>
               <TextLine ID="r2l3"
                         BASELINE="2569"
                         HEIGHT="58"
                         WIDTH="44"
                         VPOS="2511"
                         HPOS="243">
                  <String HEIGHT="58" 
                  				WIDTH="132" 
                  				VPOS="2511" 
                  				HPOS="155" 
                  				CONTENT="7"/>
               </TextLine>
            </TextBlock>
            <TextBlock ID="r3" 
            					 HEIGHT="2480" 
            					 WIDTH="1451" 
            					 VPOS="128" 
            					 HPOS="222">
               <Shape>
                  <Polygon POINTS="222,128 222,2608 1673,2608 1673,128"/>
               </Shape>
               <TextLine ID="r3l1"
                         BASELINE="175"
                         HEIGHT="65"
                         WIDTH="300"
                         VPOS="110"
                         HPOS="1319">
                  <String HEIGHT="65"
                          WIDTH="236"
                          VPOS="110"
                          HPOS="1298"
                          CONTENT="&lt;b&gt;Août"/>
                  <SP HEIGHT="65" WIDTH="21" VPOS="110" HPOS="1533"/>
                  <String HEIGHT="65"
                          WIDTH="171"
                          VPOS="110"
                          HPOS="1448"
                          CONTENT="1874.."/>
               </TextLine>
               <TextLine ID="r3l2"
                         BASELINE="175"
                         HEIGHT="65"
                         WIDTH="187"
                         VPOS="110"
                         HPOS="243">
                  <String HEIGHT="65"
                          WIDTH="140"
                          VPOS="110"
                          HPOS="227"
                          CONTENT="&lt;b&gt;N°"/>
                  <SP HEIGHT="65" WIDTH="16" VPOS="110" HPOS="368"/>
                  <String HEIGHT="65"
                          WIDTH="125"
                          VPOS="110"
                          HPOS="305"
                          CONTENT="28&lt;/b&gt;"/>
               </TextLine>
```



The desired structure demanded the following structural modifications:<br>

1. Removing the unnecessary tags `<TopMargin>`, `<LeftMargin>`, `<RightMargin>`, `<BottomMargin>`,`<Shape>`,`<Polygon>`;

2. Adding the `<Styles>` tag in the header with the following content: 

   ```xml
   <Styles>
        <TextStyle ID="font0" FONTSTYLE=""/>
        <TextStyle ID="font1" FONTSTYLE="bold"/>
        <TextStyle ID="font2" FONTSTYLE="italics"/>
   </Styles>
   ```

3. Adding the `ID` attribute for each element `<String>`; the value of its `ID` is the incremented value generated by the `ID` of its parent element `TextLine`; 										
   
   ```xml
   <TextBlock ID="r_2_1" HEIGHT="205" WIDTH="2840" VPOS="833" HPOS="793">
          <TextLine ID="tl_2" <-------- used to generate incrementally the value of the <String>'s ID attribute
                    BASELINE="943"
                    HEIGHT="109"
                    WIDTH="2836"
                    VPOS="834"
                    HPOS="794">
             <String ID="tl_2_1" <------- The ID with the incremented value
                     HEIGHT="109"
                     WIDTH="324"
                     VPOS="834"
                     HPOS="753"
                     CONTENT="154."/>
   ```
   
4. Applying the `FONT{0,1,2} ` attributes to the elements `<String>` in the following manner:<br>

    a. the default value is `STYLEREFS="FONT0"` (normal text);

    b. if the attribute `CONTENT` contains the tags `<b> `or `</b>` then `STYLEREFS="FONT1"` (bold); 

    c. if the attribute `CONTENT` contains the tags `<i> `or `</i>` then `STYLEREFS="FONT2"` (italic).

    ```xml
    <String CONTENT="&lt;b&gt;Août" 
    				HEIGHT="18.4251968503937" 
            HPOS="367.93700787401576" 
            ID="r3l1_1" 
            STYLEREFS="FONT1" 				-------> bold
            VPOS="31.181102362204726" 
            WIDTH="66.89763779527559" />
    <SP HEIGHT="18.4251968503937" HPOS="434.5511811023622" VPOS="31.181102362204726" WIDTH="5.952755905511811"/>
    <String CONTENT="1874.." 
            HEIGHT="18.4251968503937" 
            HPOS="410.45669291338584" 
            ID="r3l1_2" 
            STYLEREFS="FONT0" 				-------> normal text
            VPOS="31.181102362204726" 
            WIDTH="48.47244094488189" />
    ```



The extended desired structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<alto xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns="http://www.loc.gov/standards/alto/ns-v2#"
      xmlns:page="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15"
      xsi:schemaLocation="http://www.loc.gov/standards/alto/ns-v2# http://www.loc.gov/standards/alto/alto.xsd">
   <Description>
      <MeasurementUnit>pixel</MeasurementUnit>
      <OCRProcessing ID="IdOcr">
         <ocrProcessingStep>
            <processingDateTime>2020-05-17T21:22:02.419+02:00</processingDateTime>
            <processingSoftware>
               <softwareCreator>READ COOP</softwareCreator>
               <softwareName>Transkribus</softwareName>
            </processingSoftware>
         </ocrProcessingStep>
      </OCRProcessing>
   </Description>
   <Styles>
        <TextStyle ID="FONT0" FONTSTYLE=""/>
        <TextStyle ID="FONT1" FONTSTYLE="bold"/>
        <TextStyle ID="FONT2" FONTSTYLE="italics"/>
   </Styles>
   <Tags/>
   <Layout>
      <Page ID="Page1" PHYSICAL_IMG_NR="1" HEIGHT="2885" WIDTH="1858">
         <PrintSpace HEIGHT="2614" WIDTH="1679" VPOS="5" HPOS="0">
            <TextBlock ID="r2" HEIGHT="241" WIDTH="34" VPOS="2334" HPOS="249">
               <TextLine ID="r2l1"
                         BASELINE="2391"
                         HEIGHT="58"
                         WIDTH="44"
                         VPOS="2333"
                         HPOS="241">
                  <String ID="r2l1_1" 
                  				HEIGHT="58" 
                  				WIDTH="132" 
                  				VPOS="2333" 
                  				HPOS="153" 
                  				CONTENT="5"
                          STYLEREFS="FONT0"/>
               </TextLine>
               <TextLine ID="r2l2"
                         BASELINE="2486"
                         HEIGHT="71"
                         WIDTH="56"
                         VPOS="2415"
                         HPOS="239">
                  <String ID="r2l2_1" 
                  				HEIGHT="71" 
                  				WIDTH="168" 
                  				VPOS="2415" 
                  				HPOS="127" 
                  				CONTENT="6"
                          STYLEREFS="FONT0"/>
               </TextLine>
               <TextLine ID="r2l3"
                         BASELINE="2569"
                         HEIGHT="58"
                         WIDTH="44"
                         VPOS="2511"
                         HPOS="243">
                  <String ID="r2l3_1" 
                  				HEIGHT="58" 
                  				WIDTH="132" 
                  				VPOS="2511" 
                  				HPOS="155" 
                  				CONTENT="7"
                          STYLEREFS="FONT0"/>
               </TextLine>
            </TextBlock>
            <TextBlock ID="r3" HEIGHT="2480" WIDTH="1451" VPOS="128" HPOS="222">
               <TextLine ID="r3l1"
                         BASELINE="175"
                         HEIGHT="65"
                         WIDTH="300"
                         VPOS="110"
                         HPOS="1319">
                  <String ID="r3l1_1"
                  				HEIGHT="65"
                          WIDTH="236"
                          VPOS="110"
                          HPOS="1298"
                          CONTENT="&lt;b&gt;Août"
                          STYLEREFS="FONT1"/>
                  <SP HEIGHT="65" WIDTH="21" VPOS="110" HPOS="1533"/>
                  <String ID="r3l1_2"
                  				HEIGHT="65"
                          WIDTH="171"
                          VPOS="110"
                          HPOS="1448"
                          CONTENT="1874.."
                          STYLEREFS="FONT0"/>
               </TextLine>
               <TextLine ID="r3l2"
                         BASELINE="175"
                         HEIGHT="65"
                         WIDTH="187"
                         VPOS="110"
                         HPOS="243">
                  <String ID="r3l2_1"
                  				HEIGHT="65"
                          WIDTH="140"
                          VPOS="110"
                          HPOS="227"
                          CONTENT="&lt;b&gt;N°"
                          STYLEREFS="FONT1"/>
                  <SP HEIGHT="65" WIDTH="16" VPOS="110" HPOS="368"/>
                  <String ID="r3l2_2"
                  				HEIGHT="65"
                          WIDTH="125"
                          VPOS="110"
                          HPOS="305"
                          CONTENT="28&lt;/b&gt;"
                          STYLEREFS="FONT1"/>
               </TextLine>
```

### Remarks

* For the transformation of the ALTO-XML files we opted for the `ElementTree` built-in Python library, instead of the non-native Python library `lxml`;
* With this library it was possible to reproduce the results made during the experimental phase, and as well to improve the crucial aspect of the transformation, that is, the correct assignment of the attribute values `FONT{0,1,2}`;
* There were some initial problems in the displaying of the ALTO-XML header (e.g. the insertion of `<ns0:` in `<ns0:Description>` ). Those issues were resolved by adding the explicit statements of the namespaces and the metadata in the header, which facilitated the creation of the valid ALTO-XML structure and the access to the XML nodes (e.g. `{http://www.loc.gov/standards/alto/ns-v2#}Page` );



### TO DO

* Transform all the annotated training data using this procedure.