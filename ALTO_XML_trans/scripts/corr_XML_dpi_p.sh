#!/bin/bash

# define all possible flags (-a, -h, -p)

while getopts "ahp:" opt; do 
	case ${opt} in
	a )  option_total=${opt}
	  ;;
	h ) option_total=${opt}; echo '########## Help ##########'
	  ;;	
	p ) option_path=${opt}; path_ALTO_XML=${OPTARG}
	  ;;

	  # if we don't pass the -a or the -h argument, the script throws the error

	\? ) echo 'Invalid flag, use -a to transform all.'; exit 1
	  ;;
	esac
done



# # if the option -p (path to some directory of directories to transform) is not fulfilled, a default path is set

if [ "${option_path}" != "p" ]; then
	path_ALTO_XML='/Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/'
fi

# display help/description text with the flag -h

if [ "${option_total}" == "h" ]; then
	echo "Flag description:
	-a 		Transform all the files in all the catalogue folders, whether they have already been transformed or not;
			Intended to handle the situations if somebody incorrectly modifies the transformed file, so we want to make sure that all the files are transformed in a regular way defined by the scripts .py and .sh themselves:

	-p 		When we add new (non-transformed) files, we can transform only those files;
			Run the code, followed by the -p flag and the absolute path to the folder containing all the catalogues;
			For the already transformed files, the script throws the error that those files are already transformed.

	-h 		Get help/text description of the flags.

			For the detailed explanation of the script, go to https://github.com/ljpetkovic/OCR-cat/tree/master/ALTO_XML_trans."
	
	exit 0

# pass the argument -a to transform all files, no matter if they had already been transformed

elif [ "${option_total}" == "a" ]; then

	for g in $path_ALTO_XML/doc/* # find all the catalogue folders
	do
		echo Processing $g
		liste_image=( $g/*.jpg ) # find the image from which we fetch the dpi
		image=${liste_image[0]} 
		dpi=$(convert $image -format "%x" info:)  # fetch the dpi from the image
		liste_trans=$(find $g  -type f -name "*trans.xml") # find all the files ending with 'trans.xml'
		for f in $liste_trans
		do
			rm $f # delete all the 'trans.xml' files
		done
		for f in $g/*.xml # search for all the original .xml files
		do 
			python3 $path_ALTO_XML/scripts/corr_XML_dpi.py $f $dpi # and start over the transformation
			echo "Processing $f" 
		done
	done	
else

	# if we don't specify any flag 

	for g in $path_ALTO_XML/doc/* # find all the catalogue folders
	do
		if compgen -G "$g/*_trans.xml" > /dev/null; then # find the .xml file ending with '_trans.xml'
        	echo $g "already transformed" # throw the message that the file is already transformed
		else
			echo Processing $g
			liste_image=( $g/*.jpg ) # find the image from which we fetch the dpi
			image=${liste_image[0]} 
			dpi=$(convert $image -format "%x" info:) # fetch the dpi from the image
			for f in $g/*.xml # find all the .xml files
			do 
				python3 $path_ALTO_XML/scripts/corr_XML_dpi.py $f $dpi # transform files
				echo "Processing $f" 
			done
		fi
	done
fi  

