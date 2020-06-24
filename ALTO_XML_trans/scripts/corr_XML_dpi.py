import lxml.etree as etree
import sys, argparse
import re


########### récupération du chemin du fichier #######################

fichier = sys.argv[1] #'1885_12_RDA_N095-1.xml'  # '1871_08_RDA_N028-1.xml'
 
########### récupération du dpi #######################

dpi = int(sys.argv[2])

########### récupération du nom du fichier #######################

pattern = r'[^/]+$'
p = re.compile(pattern)
result = p.search(fichier)
fileName = result.group()  

##################################################################


parser_XML = etree.XMLParser(remove_blank_text=True) # </Styles> - la nouvelle ligne - <Tags/> - l'indentation  
tree = etree.parse(fichier,parser_XML)
root = tree.getroot()

############## ajout des namespaces et des méta-données dans l'en-tête ##############

 
sourceImageInformationText = """
      <sourceImageInformation xmlns="http://www.loc.gov/standards/alto/ns-v2#">
         <fileName>{}</fileName>
      </sourceImageInformation>

""".format(fileName)

processingSoftwareText = """
            <processingSoftware xmlns="http://www.loc.gov/standards/alto/ns-v2#">
               <softwareCreator>CONTRIBUTORS</softwareCreator>
               <softwareName>pdfalto</softwareName>
               <softwareVersion>0.1</softwareVersion>
            </processingSoftware>
"""
sourceImageInformation = etree.fromstring(sourceImageInformationText)
processingSoftware = etree.fromstring(processingSoftwareText)
for processing_software in root[0][1]:
    for p in processing_software.findall('{http://www.loc.gov/standards/alto/ns-v2#}processingSoftware'):
        processing_software.remove(p)

    
root[0].insert(1, sourceImageInformation)
root[0][2][0].insert(1, processingSoftware)

#############   nettoyage du ficher des balises inutiles     ################

tag_a_supprimer = ['{http://www.loc.gov/standards/alto/ns-v2#}TopMargin',
                   '{http://www.loc.gov/standards/alto/ns-v2#}LeftMargin',
                   '{http://www.loc.gov/standards/alto/ns-v2#}RightMargin',
                   '{http://www.loc.gov/standards/alto/ns-v2#}BottomMargin']

for page in root[2].iter('{http://www.loc.gov/standards/alto/ns-v2#}Page'):
    for tag in tag_a_supprimer:
        for elem in page.findall(tag):
            page.remove(elem)
    for printspace in page.findall('{http://www.loc.gov/standards/alto/ns-v2#}PrintSpace'):
        for textblock in printspace.findall('{http://www.loc.gov/standards/alto/ns-v2#}TextBlock'):
            for shape in textblock.findall('{http://www.loc.gov/standards/alto/ns-v2#}Shape'):
                textblock.remove(shape)

############    ajout d'une balise <Styles> avec les polices dans l'en-tête     ##########

stylesText = """
<Styles xmlns="http://www.loc.gov/standards/alto/ns-v2#">
     <TextStyle ID="FONT0"
                FONTFAMILY="unknown"
                FONTSIZE="unknown"
                FONTTYPE="unknown"
                FONTWIDTH="unknown"
                FONTCOLOR="unknown"
                FONTSTYLE=""/>
     <TextStyle ID="FONT1"
                FONTFAMILY="unknown"
                FONTSIZE="unknown"
                FONTTYPE="unknown"
                FONTWIDTH="unknown"
                FONTCOLOR="unknown"
                FONTSTYLE="bold"/>
     <TextStyle ID="FONT2"
                FONTFAMILY="unknown"
                FONTSIZE="unknown"
                FONTTYPE="unknown"
                FONTWIDTH="unknown"
                FONTCOLOR="unknown"
                FONTSTYLE="italics"/>
</Styles>
"""

styles = etree.fromstring(stylesText)
root.insert(1, styles)


#######  Récupération et création incrémentale des ID des éléments <String> à partir de l'ID des éléments <TextLine> #########

for page in root[3].iter('{http://www.loc.gov/standards/alto/ns-v2#}Page'):
    for printspace in page.findall('{http://www.loc.gov/standards/alto/ns-v2#}PrintSpace'):
        for textblock in printspace.findall('{http://www.loc.gov/standards/alto/ns-v2#}TextBlock'):
            id_tex_block = textblock.attrib['ID']
            for textline in textblock.findall('{http://www.loc.gov/standards/alto/ns-v2#}TextLine'):
                id_textline = textline.attrib['ID']
                for i, string in enumerate(textline.findall('{http://www.loc.gov/standards/alto/ns-v2#}String'),
                                           start=1):
                    string.set('ID', id_textline + "_{}".format(str(i)))

###### Application des trois styles (FONT0, FONT1, FONT2) à tous les éléments <String>	######

for page in root[3].iter('{http://www.loc.gov/standards/alto/ns-v2#}Page'):
    for printspace in page.findall('{http://www.loc.gov/standards/alto/ns-v2#}PrintSpace'):
        for textblock in printspace.findall('{http://www.loc.gov/standards/alto/ns-v2#}TextBlock'):
            for textline in textblock.findall('{http://www.loc.gov/standards/alto/ns-v2#}TextLine'):
                start_b = False
                start_i = False
                for string in textline.findall('{http://www.loc.gov/standards/alto/ns-v2#}String'):
                    string.set('STYLEREFS', 'FONT0')
                    if '<b>' in string.attrib['CONTENT']:
                        start_b = True
                        string.attrib['CONTENT'] = string.attrib['CONTENT'].replace('<b>', '')
                    elif '<i>' in string.attrib['CONTENT']:
                        start_i = True
                        string.attrib['CONTENT'] = string.attrib['CONTENT'].replace('<i>', '')
                    if start_b == True:
                        string.set('STYLEREFS', 'FONT1')
                    if start_i == True:
                        string.set('STYLEREFS', 'FONT2')
                    if '</b>' in string.attrib['CONTENT']:
                        start_b = False
                        string.attrib['CONTENT'] = string.attrib['CONTENT'].replace('</b>', '')
                    elif '</i>' in string.attrib['CONTENT']:
                        start_i = False
                        string.attrib['CONTENT'] = string.attrib['CONTENT'].replace('</i>', '')
                    ###### Conversion mm10 en pixels #######

liste_attribut = ["HPOS", "VPOS", "HEIGHT", "WIDTH"]
for elt in root.iter():
    dic = elt.attrib
    for l in liste_attribut:
        if l in dic.keys():
            mm10 = dic[l]
            pixels = str(int(mm10) * dpi / 254)
            elt.set(l, pixels)

tree.write(fichier + '_trans.xml', encoding='utf8', pretty_print=True)

