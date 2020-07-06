# Unit tests

### Goals

* Guaranteeing the high-quality performance of the `corr_trans_ALTO.py` script (cf. also [here](https://github.com/ljpetkovic/OCR-cat/tree/unittests/ALTO_XML_trans/scripts)) which transforms the raw exported ALTO-XML files containing the misconstructed tags outputted by the OCR model into the same file format to be accepted by the GROBID-dictionaries;

* Preventing the possible deterioration of the results produced during the transformation when introducing a certain regex, that is, making sure that one regex is used in order to handle *one* particular case, without influencing the others: 
  * e. g. using the `(?!\w)<b`, it had been possible to transform correctly the `<bManuscrits` into `<b>Manuscrits`; however, this method also modified some cases that were **not** intended to be handled with that specific regex, which led to the incorrect results (such as the modification of the original form `<b>Gallay</b>` into `<b>>Gallay</b>`);

* If the tests spot the error(s), adjust the regex(es).

### Workflow 

##### Demo

1. Export the original ALTO-XML files from Transkribus at the **line** level (`1855_08_LAC_N72_0002_line.xml`);
2. Run the `python3 -m unittest test_regex.py` on the command line.

##### Results

* The transformed ALTO-XML file `1855_08_LAC_N72_0002_line.xml_trans.xml`;
* The command line output indicating whether the test passed:

```
(base) Ljudmilas-MacBook-Air:unit_tests ljudmilapetkovic$ python3 -m unittest test_regex.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```



or failed, with the indication of the error(s).

*NB:* In order to simulate the error, we modified the desired result in the `test_result_1` variable in the `test_regex.py` script:

```
(base) Ljudmilas-MacBook-Air:unit_tests ljudmilapetkovic$ python3 -m unittest test_regex.py 
F
======================================================================
FAIL: test_closed_i (test_regex.TestClosed)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/ljudmilapetkovic/Desktop/Katabase/OCRcat/unit_tests/test_regex.py", line 20, in test_closed_i
    self.assertEqual(closed_i(test_input_1), test_result_1)
AssertionError: 'en Grèce. <i>L. a. s</i>, à Barbié du Bocage, Paris, 1806, 1 p. 1/4,' != 'en Grèce. i>L. a. s</i>, à Barbié du Bocage, Paris, 1806, 1 p. 1/4,'
- en Grèce. <i>L. a. s</i>, à Barbié du Bocage, Paris, 1806, 1 p. 1/4,
?           -
+ en Grèce. i>L. a. s</i>, à Barbié du Bocage, Paris, 1806, 1 p. 1/4,


----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (failures=1)
```

### Regexes tested 

To be extended.

| Actual             | Expected         |
| ------------------ | ---------------- |
| `<i>L. a. s</i>/i` | `<i>L. a. s</i>` |










