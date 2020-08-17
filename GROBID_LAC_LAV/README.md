# Training the *GROBID*-dictionaries with the ALTO-XML files

The main idea is to train two _GROBID-dictionaries_ models:

* one using the markup tags `<b>` (bold) and `<i>` (italic);
* the other without the typographical information,

on the fixed-price catalogues published by:

* Jacques Charavay (hereinafter `LAC`);
* Auguste Laverdet (hereinafter `LAV`);

in the ALTO-XML format.

### Sampling criteria

For each type of catalogue we sample the oldest and the most recent publications.

The catalogues were divided into two subsets: the training set containing 4 pages, and the validation set containing 1 page.

**N.B.:** In order to have a sufficient number of pages from the oldest releases of the `LAC `catalogues containing the information about the manuscrips sales, we combined one page from the catalogue released in November 1845 (Nº4) and four pages from the one released the 1st January 1846 (Nº5).   

#### 1. With the typographical information

Current results after training the model on the `LAC` catalogues (the `LAV` catalogues' training data are to be added):

![LAC_dictionary-segmentation](img/LAC_dictionary-segmentation.jpg)

#### 2. Without the typographical information

TO DO
