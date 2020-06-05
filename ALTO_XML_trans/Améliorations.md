# Améliorations

* retirer les séquences d'échappement

## etree -> lxml

* pas besoin de ET.register_namespace 
* garder le `xmlns:page="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15"`
* `XMLParser(remove_blank_text=True)` : `</Styles>` &mdash; la nouvelle ligne &mdash; `<Tags/>` &mdash; l'indentation
* ajouter les balises `<Styles>` étendues (avec les attributs et les valeurs fictives si on n'a rien) 

## Récupération des dpi à partir des images 

* `brew install imagemagick` (directement en ligne de commande)
* déplacer une image de chaque catalogue dans chaque dossier 

## Questions

* `1896_05_30_ETI-3.xml` : il y a une valeur trop petite pour être un entier 
- Problème avec la connexion à Transkribus ("Already connected")
- Taille dans les différents chaînes 

# À faire

* README