# Automatic tag verification and correction

### Introduction

The OCR model is tested on the _in-domain_ file from the RDA catalogue (`1871_08_RDA_N028-1.png`).

The result of the OCRisation is in the `Pour_les_tests.txt` file (sample output below):

```
5
6
7


<b>Août 1874..
<b>N° 28</b>
REVUE
DES
JUAUS
<b>LAHS</b>
<b>DES CURIOSITÉS DE L'HISTOIRE & DE LA BIOGRAPHE</b>
PARAISSANT CHAQUE MOIS, SOUS LA DIRECTION DE
<b>GABRIEL CHARAVAY</b>
<b>ABONNEMENTS</>:
< <b>BUREAUX:</
France, un an (12 Numéros) 3 fr.
GO, rue Saint-Andre-des Arts
Etranger...... 4
<b>UN NUMÉRO: 25 CENTIMES</b>
<b>LETTRES AUTOGRAPHES/b>
A PRIX MARQUÉS
En vente chez Gabriel CHARAVAY,</b> expert,
rue Saint-André-des-Arts, 60.
1
<b>Abington</b> (Miss Frances), l’une des plus célèbres comédiennes
du Théâtre anglais. — L. a. sig., (à la 3e pers.), au dessinateur
Cosway, 2 p. in-8, avec son portrait dessiné par Cosway. 3 »
2 <b>Achard</b> (P.-Fréd.), spirituel acteur comique, né à Lyon. — L.
D</i
a. s., 1845, 1 p. in-8.
```

### Tasks

Check automatically the well-formedness of all the tags, whether any open tag is closed, and if the order of the tags is correct. The Python quality control script for the output tags `balises_lignes.py` is written for that purpose.

### Method 

Create regex in a fairly flexible format allowing to find *a priori* all the anomalies of the `<b>` `</b>` and `<i>` `</i>  ` tags with the following rule:

We consider that we are dealing with such a tag if we have a character string containing at most only the characters: `SPACE`, `<`, `{bi}`, `/`, `>`,
and containing at least either

• `<`, `/`and `{bi}` 

• `{bi}` and `>`,

in order to handle errors such as: `< <b>` or `<b<b>`.

### Workflow

1. define regex patterns;
2. find the correct tags;
3. find the lines not containing any tag;
4. check the number of tags;
5. check the tags' order;
6. correct the tags if needed;
7.  output results.
   

### Output description

The programme output is in the format of three columns:

* the 1<sup>st</sup> column is the original text line;
* the 2<sup>nd</sup> is the programme's output;
* the 3<sup>rd</sup> could be either the error signalisation or the suggestion of the correction. 

The possible code's outputs (corresponding to the situation after the possible correction):
**0**: line with no tags, no error message;
**1**: the tags are well-formed, respecting the order of opening and closing tags (including the original tag well-formedness and the well-formedness resulting from the corrections by the programme), no error message;
**2**: the tags are well-formed and there are as many opening as closing tags;
     but the "opening/closing" order is not respected, message error `WRONG TAG ORDER`;
**3**: the tags are well-formed but the number of opening and closing tags is not the same, message error `MISSING TAGS`;
**4**: there is at least potentially an erroneous tag which could not be corrected, message error `PROBLEM WITH THE TAG`.

Output for the first 106 lines:

```
77
5                                                                             | 0 | 
6                                                                             | 0 | 
7                                                                             | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
<b>Août 1874..                                                                | 3 |  BALISES MANQUANTES
<b>N° 28</b>                                                                  | 1 | 
REVUE                                                                         | 0 | 
DES                                                                           | 0 | 
JUAUS                                                                         | 0 | 
<b>LAHS</b>                                                                   | 1 | 
<b>DES CURIOSITÉS DE L'HISTOIRE & DE LA BIOGRAPHE</b>                         | 1 | 
PARAISSANT CHAQUE MOIS, SOUS LA DIRECTION DE                                  | 0 | 
<b>GABRIEL CHARAVAY</b>                                                       | 1 | 
<b>ABONNEMENTS</>:                                                            | 1 | <b>ABONNEMENTS</b>:

< <b>BUREAUX:</                                                               | 1 | <b>BUREAUX:</b>

France, un an (12 Numéros) 3 fr.                                              | 0 | 
GO, rue Saint-Andre-des Arts                                                  | 0 | 
Etranger...... 4                                                              | 0 | 
<b>UN NUMÉRO: 25 CENTIMES</b>                                                 | 1 | 
<b>LETTRES AUTOGRAPHES/b>                                                     | 1 | <b>LETTRES AUTOGRAPHES</b>

A PRIX MARQUÉS                                                                | 0 | 
En vente chez Gabriel CHARAVAY,</b> expert,                                   | 3 |  BALISES MANQUANTES
rue Saint-André-des-Arts, 60.                                                 | 0 | 
1                                                                             | 0 | 
<b>Abington</b> (Miss Frances), l’une des plus célèbres comédiennes           | 1 | 
du Théâtre anglais. — L. a. sig., (à la 3e pers.), au dessinateur             | 0 | 
Cosway, 2 p. in-8, avec son portrait dessiné par Cosway. 3 »                  | 0 | 
2 <b>Achard</b> (P.-Fréd.), spirituel acteur comique, né à Lyon. — L.         | 1 | 
D</i                                                                          | 3 | D</b>i

a. s., 1845, 1 p. in-8.                                                       | 0 | 
3                                                                             | 0 | 
<Achard</b> (Léon), célèbre ténor de l’Opéra-Comique, né à Lyon,              | 3 | <Achard</b>(Léon), célèbre ténor de l’Opéra-Comique, né à Lyon,

fils du précédent. — L. a. s., 1 p. in-8.                                     | 0 | 
2                                                                             | 0 | 
4 <b>Adélaïde</b> (Louise-Thér.-Car.-Amélie), princesse de Saxe-Mei¬          | 1 | 
ningen, reine d’Angleterre, femme de Georges IV. — L. a, s.,                  | 0 | 
en anglais, à Alex. Vattemare, 7 juin 1838, 1 p. in-4, cach.                  | 0 | 
4                                                                             | 0 | 
»                                                                             | 0 | 
Gracteux remerciments à Vattemare, qui lui a communiqué sa collection d'auto¬ | 0 | 
grapbes et de dessins.                                                        | 0 | 
<b<b>Adelon</b> (N.-Philib.), savant médecin et physiologiste, né à           | 1 | <b>Adelon</b>(N.-Philib.), savant médecin et physiologiste, né à

2                                                                             | 0 | 
»                                                                             | 0 | 
Dijon. — L. a. s., 1834, 1 p. 1/2 in-4.                                       | 0 | 
<b<b>Affo</b> (Ireneo), historien de Guastalla et de Parme. — L. a. s.        | 1 | <b>Affo</b>(Ireneo), historien de Guastalla et de Parme. — L. a. s.

2 50                                                                          | 0 | 
au graveur Rosaspina; Parme, 1793, 1 p. in-4.                                 | 0 | 
<b>Agar</> (Mme), célèbre tragédienne. —                                      | 1 | <b>Agar</b>(Mme), célèbre tragédienne. —

L. a. s., 1 p. in-8, relative                                                 | 0 | 
à une soiree de bienfaisance chez la princesse Mathilde. 3 »                  | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
8 <b>Ainsworth</b> (W. Harrison), célèbre romancier angl., imitateur          | 1 | 
                                                                              | 0 | 
                                                                              | 0 | 
heureux du genre d’Anne Radcliffe. — L. a. s., 1865, 4 p.                     | 0 | 
in-8. 2 50                                                                    | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
9 <b>Akakia</b> (Jean), médecin de Louis XIII, régent-doyen de la             | 1 | 
                                                                              | 0 | 
                                                                              | 0 | 
Faculté de Paris. — Quittance sig. sur vélin, 1619. 1 50                      | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
10 <b>Albani</b> (le card. Joseph), soupçonné de complicité dans l’assas¬     | 1 | 
                                                                              | 0 | 
                                                                              | 0 | 
sinat de Basseville, ministre de Pie VIII, musicien. — L. a. s.,              | 0 | 
en français; Rome, 1816, 1 p. 1/2 in-4. 3 »                                   | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
Relative à des marbres antiques que son fière voulait vendre à Paris.         | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
11 <b>Aleotti</b> (J.-B.), illustre architecte du XVIe siècle, constructeur   | 1 | 
                                                                              | 0 | 
                                                                              | 0 | 
du théâtre Farnèse, à Parme. — Fin d’un compte, sig., relatif                 | 0 | 
à la construction de la citadelle de Ferrare, 1 p. in-4,                      | 0 | 
oblong. 2 »                                                                   | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
12 <b>Alghisi</b> (Tommaso), chirurgien florentin, célèbre par ses            | 1 | 
travaux sur la lithotomie. — L. a. s., 1698, 1 p. in-f. 3 »                   | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
13 <b>Alizard</b> (Adolphe), célèbre chanteur du grand Opéra. — L. a. s.;     | 1 | 
                                                                              | 0 | 
                                                                              | 0 | 
Bruxelles, 1843, 2 p. in-8. 2 »                                               | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
14 <b>Allan</b> (Louise), une des plus célèbres comédiennes du Théâtre        | 1 | 
                                                                              | 0 | 
                                                                              | 0 | 
français. — L. a. s., 1848, 1 p. in-8. 2 50                                   | 0 | 
                                                                              | 0 | 
                                                                              | 0 | 
15 <b>Allan</b> (A.), acteur comique du Gymnase, mari de la précédente.       | 1 | 
                                                                              | 0 | 
                                                                              | 0 | 
— L. a. s., 1/2 p. in-4. 5 4. 1 50                                            | 0 | 
                                                                              | 0 | 
>>> 
```

### Statistics

| Code                                                         | Nº of occurrences | %    |
| :----------------------------------------------------------- | ----------------- | ---- |
| 0 (lines with no tags)                                       | 80                | 75.5 |
| 1 (well-formed tags, correct opening/closing tags order)     | 22                | 20.8 |
| 2 (well-formed tags, same number of opening/closing tags, wrong opening/closing tags order) | 0                 | 0    |
| 3 (well-formed tags, different number of opening and closing tags) | 4                 | 3.8  |
| 4 (at least one wrong tag that could not be corrected.)      | 0                 | 0    |

### Remarks

The same code could be used to check the validity of the italic tags by replacing the arguments `b`, `<b>` and `</b>` with the corresponding `i`,`<i>` and`</i>` arguments (note that the latter tags appear in the text, starting from the line 108).

In order to avoid matching real words starting with `b` with an accidental `<` before (for example: `<boat`), the regex`[ <b>]*<[ <b>]*b([ <b>]*>[ <b>]*)*` should be tested beforehand.

We are not looking for the `/` in isolation, because of the presence of possible fractions (`1/2`).

This programme is supposed to generalise well in the cases of the individual tags `<b>text</b>` and `<i>text</i>`. However, in order to further check the robustness of the results, and to be certain that this code could handle the case of the nested tags (e.g. `<b><i>text</i></b>`, where the sequences `<b><i>` and `</i></b>` should not be treated as error), more test data will be provided.

### TO DO

* Correct manually the text not recognised properly by the OCR model;
* Add more test data to check the generalisability of the code.