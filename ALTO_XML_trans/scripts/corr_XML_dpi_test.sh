#!/bin/bash
#for g in /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/doc/*
#do
	
	input_file=../test/1871_08_RDA_N028-1.xml
	input_image=../test/1871_08_RDA_N028-1.jpg
	echo "Processing $input_file..." | sed 's/..\/test\///g'
	python3 corr_XML_dpi_test.py $input_file $(convert $input_image -format "%x" info:) #$f is the file name, here '1871_08_RDA_N028-1.xml'
	echo Done