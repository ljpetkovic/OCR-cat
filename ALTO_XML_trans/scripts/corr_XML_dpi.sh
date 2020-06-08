#!/bin/bash
for g in /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/doc/*
do
	echo Processing $g
	liste_image=( $g/*.jpg )
	image=${liste_image[0]} 
	u=$(convert $image -format "%x" info:)
	for f in $g/*.xml
	do 
		python3 /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/scripts/corr_XML_dpi.py $f $u 
		echo "Processing $f" 
	done
done
