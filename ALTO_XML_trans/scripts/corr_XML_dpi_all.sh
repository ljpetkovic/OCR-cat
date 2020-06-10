#!/bin/bash

	
while getopts "ah" opt; do 
	case ${opt} in
	a )  option_total=${opt}
	  ;;
	h ) option_total=${opt}; echo '########## Help ##########'
	  ;;
	  # if we don't pass the -a or the -h argument, the script throws the error
	\? ) echo 'Invalid flag, use -a to transform all files.'
	  ;;
	esac
done




path_ALTO_XML='/Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/'

# the -h argument providing the help instruction for the script usage
if [ "${option_total}" == "h" ]; then
	echo "Flag description:
	-a 		transforms all files in all the catalogue folders, no matter if they had already been transformed. 
	
	If the flag is not specified, the script transforms only the non-transformed files. 
	However, if the script is run against the files already transformed, it throws the error 'Already transformed'.
	"
# pass the argument -a to transform all files, no matter if they had already been transformed
elif [ "${option_total}" == "a" ]; then

	for g in $path_ALTO_XML/doc/* # find all the catalogue folders
	do
		echo Processing $g
		liste_image=( $g/*.jpg )
		image=${liste_image[0]} 
		dpi=$(convert $image -format "%x" info:) # convert mm10 into pixels
		liste_trans=$(find $g  -type f -name "*trans.xml") # find all the files ending with 'trans.xml'
		for f in $liste_trans
		do
			rm $f # delete all the 'trans.xml' files...
		done
		for f in $g/*.xml # search for all the original .xml files
		do 
			python3 $path_ALTO_XML/scripts/corr_XML_dpi.py $f $dpi # ...and start over the transformation
			echo "Processing $f" 
		done
	done	
else
	# if we don't specify any flag...  

	for g in $path_ALTO_XML/doc/* # find all the catalogue folders
	do
		if compgen -G "$g/*_trans.xml" > /dev/null; then # ...and the script finds the .xml file ending with '_trans.xml'
        	echo $g "already transformed." # throws the message that the file is already transformed
		else
			echo Processing $g
			liste_image=( $g/*.jpg ) # fetch the dpi from the image
			image=${liste_image[0]} 
			dpi=$(convert $image -format "%x" info:) # mm10 to pixels conversion
			for f in $g/*.xml # find all the .xml files
			do 
				python3 $path_ALTO_XML/scripts/corr_XML_dpi.py $f $dpi # transform files
				echo "Processing $f" 
			done
		fi
	done
fi  

