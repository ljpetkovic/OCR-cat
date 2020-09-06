# Transformation and evaluation of the ALTO-XML files 

The core idea of redesigning the ALTO-XML files in order to be injected into the GROBID-dictionaries is available [here](https://github.com/ljpetkovic/OCR-cat/blob/GROBID_eval/ALTO_XML_trans/ALTO-transformation.md).<br>

This is the updated version of the code, which includes the transformation of **all the files** in all the catalogue folders.<br>

### Preliminaries

You will need to have **Python 3** and **pip/pip3** installed. <br>

To create your Python virtual environment (optional):

1. Install the `virtualenv` PyPI library: <br>

   `pip3 install virtualenv` <br>

2. Move to the project directory:<br>

   `cd path/to/my/project/directory`

3. Set up your Python virtual environment in the project directory (this will create the `env` sub-directory):<br>

   `virtualenv -p python3 env`<br> (you can use any name instead of `env`)

4. Activate the environment:<br>

   `source env/bin/activate`<br>

5. Install libraries and dependencies:

   `pip3 install -r requirements.txt`<br>

   <!--In order to install the `imagemagick` library on macOS/Linux, it is necessary to install [Homebrew](https://brew.sh) (The Missing Package Manager for macOS/Linux).<br>-->
   
   <!--After you installed `homebrew`, type:-->
   
   <!--`brew bundle`-->
   
   <!--This command installs the `imagemagick` library on macOS/Linux (indicated in the `Brewfile`), and it is mandatory for the mm10 to pixels conversion.<br>-->

*NB*:

* To deactivate the virtual environment:<br>

  `deactivate`

* Allow user to read and execute scripts:<br>

  `chmod 755 myScript.sh`

### New features

##### Iterative transformation of all files in all the catalogues:<br>

cf. e.g. `corr_trans_ALTO.sh`:

* One `for` loop enables access to all the catalogue folders (`$g`), as well as to the corresponding image samples providing the information about the dpi:

  ```bash
  for g in /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/doc/* ---------- locate all the catalogue folders
  do
  	echo Processing $g
  	liste_image=( $g/*.jpg ) ---------- open all the folders and find images in those folders
  	image=${liste_image[0]}  
  	u=$(convert $image -format "%x" info:) ---- mm10 to pixels conversion, cf. the next subsection
  	...
  	done
  ```

* The other loop opens and transforms all the .xml files (`$f`) located in their corresponding folders:

  ```bash
  	for f in $g/*.xml
  	do 
  		python3 /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/scripts/corr_XML_dpi.py $f $u 
  		echo "Processing $f" 
  	done
  ```

  

##### <!--Image resolutions:<br>-->

* <!--Measurement unit: pixels per inch of an image (PPI).-->


##### Remove escape sequences  of the markup tags from the attribute values<br>

e.g. `BELLE` instead of `&lt;b&gt;BELLE`

#### Advantages of integrating the `lxml` library into the code<br>

##### Extending the `<Styles>` tag content:<br>

```xml
<Styles>
     <TextStyle ID="FONT0" FONTSTYLE=""/>
     <TextStyle ID="FONT1" FONTSTYLE="bold"/>
     <TextStyle ID="FONT2" FONTSTYLE="italics"/>
</Styles>
```

- no need to register the namespace (unlike with the previously used `etree` command `ET.register_namespace`);
- <!--preserving the `xmlns:page="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15"` namespace from the original ALTO-XML files;-->

##### Correct placing of the tag `<Tags/>` after inserting the tag `<Styles>`<br>

- The function `etree.XMLParser(remove_blank_text=True)` makes sure that the tag `</Styles>` is followed by a line feed and the tag `<Tags/>` (in the earlier version the tag `<Tags/>` followed immediately the tag `</Styles>` in the same line):

  ```xml
    <Styles>
         <TextStyle ID="FONT0" FONTSTYLE=""/>
         <TextStyle ID="FONT1" FONTSTYLE="bold"/>
         <TextStyle ID="FONT2" FONTSTYLE="italics"/>
    </Styles>
  <Tags/>
  ```
  
##### Dispay `--help`/description text of the Bash script

* `./corr_trans_ALTO.sh -h`

  ```
              ########## Help ##########
  Flag description:
  	-a 	Transform all files in all catalogue folders, whether they have already been transformed or not;
  		Intended to handle the situations if somebody incorrectly modifies the transformed file, so we want to make sure that all the files are transformed in a regular way defined by the .py and .sh scripts:
  
  	-d 	When we add new (non-transformed) files, we can transform only those files, and ignore those already transformed;
  		Run the code, followed by the -d flag and the folder name containing those files;
  		For the already transformed files, the script throws the error that these files have already been transformed.
  
  	-h 	Get help/text description of the flags.
  
  For the detailed explanation of the script, go to https://github.com/ljpetkovic/OCR-cat/tree/GROBID_eval/ALTO_XML_trans.
  ```

  


### Running the scripts

#### Demo

When in `scripts` folder, to transform only one file (for testing purposes), run:<br>

```bash
python3 corr_trans_alto.py ../test/1871_08_RDA_N028-1.xml 
```

<!--The above command runs the Python transforming script `corr_XML_dpi_test.py` on the input file `../test/1871_08_RDA_N028-1.xml`, while performing the mm10 to pixels conversion using the `imagemagick` library with the command `$(convert ../test/1871_08_RDA_N028-1.jpg -format "%x" info:)` (the `"%x"` indicates the horizontal resolution).-->

If you uncomment

```
# fichier = '../doc/1845_11_LAC_N01_duplicated/1845_11_LAC_N01_8_train.xml'
# base=os.path.basename(fichier) # pour récupérer le nom du fichier sans extension
# print('Processing ', os.path.splitext(base)[0], '.xml...\nDone.')
```

The output of the terminal would be:<br>

```bash
Processing 1871_08_RDA_N028-1.xml...
Done
```

Output of the transformed file `1871_08_RDA_N028-1.xml_trans`:<br>

```xml
<?xml version='1.0' encoding='UTF8'?>
<alto xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.loc.gov/standards/alto/ns-v2#" xmlns:page="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15" xsi:schemaLocation="http://www.loc.gov/standards/alto/ns-v2# http://www.loc.gov/standards/alto/alto.xsd">
  <Description>
    <MeasurementUnit>pixel</MeasurementUnit>
    <sourceImageInformation>
         <fileName>1871_08_RDA_N028-1.xml</fileName>
      </sourceImageInformation>
    <OCRProcessing ID="IdOcr">
      <ocrProcessingStep>
        <processingDateTime>2020-05-17T21:22:02.419+02:00</processingDateTime>
        <processingSoftware>
               <softwareCreator>CONTRIBUTORS</softwareCreator>
               <softwareName>pdfalto</softwareName>
               <softwareVersion>0.1</softwareVersion>
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
          <TextLine ID="r2l1" BASELINE="2391" HEIGHT="58" WIDTH="44" VPOS="2333" HPOS="241">
            <String HEIGHT="58" WIDTH="132" VPOS="2333" HPOS="153" CONTENT="5" ID="r2l1_1" STYLEREFS="FONT0"/>
          </TextLine>
          <TextLine ID="r2l2" BASELINE="2486" HEIGHT="71" WIDTH="56" VPOS="2415" HPOS="239">
            <String HEIGHT="71" WIDTH="168" VPOS="2415" HPOS="127" CONTENT="6" ID="r2l2_1" STYLEREFS="FONT0"/>
          </TextLine>
          <TextLine ID="r2l3" BASELINE="2569" HEIGHT="58" WIDTH="44" VPOS="2511" HPOS="243">
            <String HEIGHT="58" WIDTH="132" VPOS="2511" HPOS="155" CONTENT="7" ID="r2l3_1" STYLEREFS="FONT0"/>
          </TextLine>
        </TextBlock>
        <TextBlock ID="r3" HEIGHT="2480" WIDTH="1451" VPOS="128" HPOS="222">
          <TextLine ID="r3l1" BASELINE="175" HEIGHT="65" WIDTH="300" VPOS="110" HPOS="1319">
            <String HEIGHT="65" WIDTH="236" VPOS="110" HPOS="1298" CONTENT="Août" ID="r3l1_1" STYLEREFS="FONT1"/>
            <SP HEIGHT="65" WIDTH="21" VPOS="110" HPOS="1533"/>
            <String HEIGHT="65" WIDTH="171" VPOS="110" HPOS="1448" CONTENT="1874.." ID="r3l1_2" STYLEREFS="FONT1"/>
          </TextLine>
          ...
```

#### Full version

From the same folder, run `./corr_trans_ALTO.sh`.

Output of the terminal:<br>

```bash
Processing /Users/ljudmilapetkovic/Desktop/Katabase/ALTO_XML_trans/doc/1845_05_14_CHA_typo
Processing /Users/ljudmilapetkovic/Desktop/Katabase/ALTO_XML_trans/doc/1845_05_14_CHA_typo/1845_05_14_CHA-0008.xml
...
Processing /Users/ljudmilapetkovic/Desktop/Katabase/ALTO_XML_trans/doc/1856_10_LAV_N03_gt_typo
Processing /Users/ljudmilapetkovic/Desktop/Katabase/ALTO_XML_trans/doc/1856_10_LAV_N03_gt_typo/1856_10_LAV_N03-1.xml
...
```

<!--Output of the transformed file `1845_05_14_CHA-0008.xml_trans.xml`:<br>-->