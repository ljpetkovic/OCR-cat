# Evaluation

The OCR model is tested on the _in-domain_ file from the RDA catalogue (`1871_08_RDA_N028-1.png`).

The result of the OCRisation is in the `1871_08_RDA_N028-1-test.txt` file.

For the evaluation purpose, that is, to determine the percentage error between the output tags and the actual tags, the corresponding  `1871_08_RDA_N028-1-corr.txt` file is created, in which the missing tags were added and the misformed tags are corrected manually. 

Statistics of the corrected file:

| Tag     | Nº of occurrences |
| ------- | ----------------- |
| `<b>`   | 277               |
| `</b>`  | 277               |
| `<i>`   | 125               |
| `</i>`  | 125               |
| _Total_ | 804               |

19 corrections have been performed, which comprises the 2.4% of the text (19 / 804). For the visualisation of these corrections, cf. https://www.diffchecker.com/aZYO8jrf).

In order to have a precise evaluation of the OCR output, run the `tags_lines.py`

regexes





