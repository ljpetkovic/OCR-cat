import lxml.etree as etree
import argparse
import re


########### Récupération du chemin du fichier #######################

fichier = '1855_08_LAC_N72_0002_line.xml' 

########## Parser le fichier ############

tree = etree.parse(fichier)
root = tree.getroot()
              

####### Correction des balises pleines dans les fichiers ALTO-XML ##########
patt_b_open = r'([ <](([< ])*b([ >])*)+[>])|([<](([< ])*b([ >])*)+[ >])|(^(([< ])*b([ >])*)+[>])|[ <b>]*<[ <b>]*b([ <b>]*>[ <b>]*)*|(?<=[(b>)])b>|(?<=)b>'
patt_i_open = r'([ <](([< ])*i([ >])*)+[>])|([<](([< ])*i([ >])*)+[ >])|(^(([< ])*i([ >])*)+[>])|[ <i>]*<[ <i>]*i([ <i>]*>[ <i>]*)*|(?<=[(i>)])i>|(?=<.*<\/i>)<'
patt_b_closed = r'(([<]*[ ]*[\/][ ]*b([ >])*)+[ >.,;])|(([<]*[ ]*[\/][ ]*b([ >])*)+$)|[ <b>]*<[ <b>]*[\/]b([ <b>]*>[ <b>]*)*|(?<=[(b>)])\/b>'
patt_i_closed = r'(([<]*[ ]*[\/][ ]*i([ >])*)+)|(([<]*[ ]*[\/][ ]*i([ >])*)+$)|[ <i>]*<[ <i>]*[\/]i([ <i>]*>[ <i>]*)*|(?<=[(i>)])\/i>'
lonely_closed_i_tag = r'(<i>[A-Za-z\d.,?!=\s]*)>+'



for page in root[1][0].iter('{http://www.loc.gov/standards/alto/ns-v2#}Page'):
    for printspace in page.findall('{http://www.loc.gov/standards/alto/ns-v2#}PrintSpace'):
        for textblock in printspace.findall('{http://www.loc.gov/standards/alto/ns-v2#}TextBlock'):
            for textline in textblock.findall('{http://www.loc.gov/standards/alto/ns-v2#}TextLine'):
                for string in textline.findall('{http://www.loc.gov/standards/alto/ns-v2#}String'):
                    #print(string)
                    
##                    if re.search(patt_b_open,string.attrib['CONTENT']): 
##                        string.attrib['CONTENT'] = re.sub(patt_b_open,'<b>',string.attrib['CONTENT'])
####    ####                      #print(string.attrib['CONTENT'])
##                    if re.search(patt_i_open,string.attrib['CONTENT']): 
##                        string.attrib['CONTENT'] = re.sub(patt_i_open,'<i>',string.attrib['CONTENT'])
####    ##                        #print(string.attrib['CONTENT'])
##                    if re.search(patt_b_closed,string.attrib['CONTENT']): 
##                        string.attrib['CONTENT'] = re.sub(patt_b_closed,'</b>',string.attrib['CONTENT'])
####    ####                      #print(string.attrib['CONTENT'])
                    def closed_i(s):
                        if re.search(patt_i_closed,string.attrib['CONTENT']):
                            string.attrib['CONTENT'] = re.sub(patt_i_closed,'</i>',string.attrib['CONTENT'])
                            #print(string.attrib['CONTENT'])
                            s = string.attrib['CONTENT']
                            return s
                            #print(s)
                    closed_i(string)
####                        #print(string.attrib['CONTENT'])
#                    if re.search(lonely_closed_i_tag,string.attrib['CONTENT']):
##                        string.attrib['CONTENT'] = re.sub(lonely_closed_i_tag,r'\1</i>',string.attrib['CONTENT'])
                    


tree.write(fichier + '_trans.xml', encoding='utf8', pretty_print=True)


