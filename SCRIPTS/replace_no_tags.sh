for f in /Users/ljudmilapetkovic/Downloads/OCRcat/DATA_typographic/{1845_05_14_CHA_typo,1856_10_LAV_N03_gt_typo,1857_02_05_JA1_bpt6k9677856h_typo,1866_04_23_GAB_typo,1885_12_RDA_N095_gt_typo,1887_bovet_bpt6k6325943w_typo,1896_05_30_ETI_gt_typo,1899_02_LAD_N293_gt_typo,1912_XX_Kra_12_gt_bpt6k6527450d_typo,Manuel_synonymie_typo}/extracted_5/*.gt.txt; do 
	sed -i '' '
s/\<b\>//g
s/\<\/b\>//g
s/\<i\>//g
s/\<\/i\>//g
' $f;
done 
