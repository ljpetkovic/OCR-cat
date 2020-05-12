for f in /Users/ljudmilapetkovic/Downloads/OCRcat/DATA_typographic/{1845_05_14_CHA_typo,1856_10_LAV_N03_gt_typo,1857_02_05_JA1_bpt6k9677856h_typo,1866_04_23_GAB_typo,1885_12_RDA_N095_gt_typo,1887_bovet_bpt6k6325943w_typo,1896_05_30_ETI_gt_typo,1899_02_LAD_N293_gt_typo,1912_XX_Kra_12_gt_bpt6k6527450d_typo,Manuel_synonymie_typo}/{extracted_1,extracted_2,extracted_3,extracted_4,extracted_5,extracted_6}/*.gt.txt
*.gt.txt; do 
	perl -p -i -e '
	s/'"'"'/'"’"'/g;
	s/\n//g;
	' $f;
done 
