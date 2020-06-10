##### `corr_XML_dpi_p.sh`

### Running the script without the additional flags:  

* if the files are not yet transformed, the script transforms those files;
* if the files have been transformed, the script throws the error that those files have already been transformed:

```
(base) Ljudmilas-MacBook-Air:scripts ljudmilapetkovic$ ./corr_XML_dpi_all.sh 
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1845_05_14_CHA_typo ----------- folder name
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1845_05_14_CHA_typo/1845_05_14_CHA-0008.xml ----------- file name
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1845_05_14_CHA_typo/1845_05_14_CHA-0009.xml
...
/Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1856_10_LAV_N03_gt_typo already transformed.
... 
```



### Running the script with the flag `-a`:

* Transform all the files in all the catalogue folders, whether they have already been transformed or not;
  * Intended to handle the situations if somebody incorrectly modifies the transformed file, so we want to make sure that all the files are transformed in a regular way defined by the scripts `.py` and `.sh` themselves:

```bash
(base) Ljudmilas-MacBook-Air:scripts ljudmilapetkovic$ ./corr_XML_dpi_all.sh -a
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1845_05_14_CHA_typo ---------- first folder
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1845_05_14_CHA_typo/1845_05_14_CHA-0008.xml
...
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/Manuel_synonymie_typo ---------- last folder
...
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/Manuel_synonymie_typo/Manuel_de_Synonymie_Latine-0037.xml
```

### Running the script with the flag `-p` and the path name:

* When we add new (non-transformed) files, we can transform only those files, and ignore the files already transformed;
* Run the code, followed by the `-p` flag and the absolute path to the folder containing all the catalogues;
* For the already transformed files, the script throws the error that those files are already transformed.

```bash
(base) Ljudmilas-MacBook-Air:scripts ljudmilapetkovic$ ./corr_XML_dpi_p.sh -p /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans/
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1845_05_14_CHA_typo
Processing /Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1845_05_14_CHA_typo/1845_05_14_CHA-0008.xml
...
/Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/ALTO_XML_trans//doc/1856_10_LAV_N03_gt_typo already transformed.
```

### Get help/text description with the flag `-h`:

```bash
(base) Ljudmilas-MacBook-Air:scripts ljudmilapetkovic$ ./corr_XML_dpi_p.sh -h
########## Help ##########
Flag description:
	-a 		Transform all the files in all the catalogue folders, whether they have already been transformed or not;
			Intended to handle the situations if somebody incorrectly modifies the transformed file, so we want to make sure that all the files are transformed in a regular way defined by the script itself:

	-p 		When we add new (non-transformed) files, we can transform only those files;
			Run the code, followed by the -p flag and the absolute path to the folder containing all the catalogues;
			For the already transformed files, the script throws the error that those files are already transformed.

	-h 		Get help/text description of the flags.

			For the detailed explanation of the script, go to https://github.com/ljpetkovic/OCR-cat/tree/master/ALTO_XML_trans.
```







