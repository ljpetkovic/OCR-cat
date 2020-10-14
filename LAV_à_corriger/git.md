To clone to *Present Working Directory*:

```
git clone https://github.com/link.git
```

To clone to *Another Directory*:

```
git clone https://github.com/link.git ./Folder1/Folder2
```



docker run -v /Users/ljudmilapetkovic/Downloads/GROBID-master-3/grobid_RDA_LAD/toyData:/grobid/grobid-dictionaries/resources -p 8080:8080 -it medkhem/grobid-dictionaries bash

java -jar /grobid/grobid-dictionaries/target/grobid-dictionaries-0.5.4-SNAPSHOT.one-jar.jar -dIn resources/dataset/dictionary-segmentation/corpus/pdf/  -dOut resources -exe createTrainingDictionarySegmentation

java -jar /grobid/grobid-dictionaries/target/grobid-dictionaries-0.5.4-SNAPSHOT.one-jar.jar -dIn resources/dataset/dictionary-segmentation/corpus/tei/  -dOut resources -exe createTrainingDictionaryBodySegmentation

cd ./Desktop/Katabase/OCRcat/Data/1845_05_14_CHA_typo
./1-transkribus_to_kraken.sh

/Users/ljudmilapetkovic/Desktop/OCRcat/env/bin/ketos extract --binarize --normalization NFD --normalize-whitespace --output extracted data/*html

git init /Users/ljudmilapetkovic/Downloads/
git clone https://github.com/ljpetkovic/OCR-cat
git remote add origin https://github.com/ljpetkovic/OCR-cat
git remote -v
cd Katabase
git add test.txt
git commit -m "test"
git push -u origin master
git add  {1845_05_14_CHA_typo,1856_10_LAV_N03_gt_typo,1857_02_05_JA1_bpt6k9677856h_typo,1866_04_23_GAB_typo,1885_12_RDA_N095_gt_typo,1887_bovet_bpt6k6325943w_typo,1896_05_30_ETI_gt_typo,1899_02_LAD_N293_gt_typo,1912_XX_Kra_12_gt_bpt6k6527450d_typo,Manuel_synonymie_typo}/extracted_6 # ajouter les sous-directoires en même temps

cat .git/config  # note <github-url>
rm -rf .git

git stash # stash all the changes in the working tree
git fetch --all
git reset --hard origin/master # discard changes, back to last commit
git pull origin master
git stash pop # get your changes back 
git reset --soft HEAD~ # reset to the last commit, save your changes, back to last commit
git rm -r --cached FolderName # supprimer le dossier du dépôt
git rm --cached FileName # supprimer le fichier du dépôt
git commit -m "Removed folder from repository"
git mv old_filename new_filename # renommer le fichier
git status # vérifier l'ancien et le nouveau nom


git init
git add <folder1> <folder2> <etc.>
git commit -m "Your message about the commit"
git remote add origin https://github.com/yourUsername/yourRepository.git
git remote -v
git push -u origin master
git push origin master
git add .gitignore
git commit -m ".gitignore" .gitignore
git rm -r --cached myFolder # Remove directory from git but NOT local
git rm --cached myFile # Remove file from git but NOT local
git reset <file> # undo git add before a commit 
git reset # unstage all changes

##### Git copy changes from one branch to another
git checkout -b production //to create branch production
git checkout master // to be positioned on the master 
git push origin production

##### git auto-complete for *branches* at the command line?

curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash

vi ~/.bash_profile

if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi

##### git auto-complete for *branches* at the command line?

open .bash_profile with your favorite tekst editor

for example you can use 'vi'

open your terminal and make sure you are in your home directory

type vi .bash_profile and press enter

in vi, type i to be able to type

enter your line

press escape

hold shift and press z twice (z z) to save and quit

##### remove the branch on the remote

git push origin --delete new_branch

##### delete the local branch

git branch -d test
git branch -D test ##### delete the branch regardless of its merge status.

##### Checkout to master

echo "moutarde" >> recetteDesCrepes.txt
git checkout ingredients

error: Vos modifications locales aux fichiers suivants seraient écrasées par l'extraction :
	recetteDesCrepes.txt
Veuillez valider ou remiser vos modifications avant de basculer de branche.
Abandon

git stash
git stash list
git checkout master
git stash apply

##### Renommer le dernier commit 

git commit --amend -m "New message" 
git push --force repository-name branch-name

##### Annuler le dernier add/commit

git reset HEAD^

##### copy the content of a branch to a new local branch

git checkout -b new_branch old_branch

##### Lancer l'environnement virtuel

virtualenv env
source env/bin/activate
pip3 install kraken

python3 randomise_data.py extracted/*.png

../Data/1845_05_14_CHA_typo/extracted/000841.png

cd ~/Desktop/Katabase/OCRcat/gt
ketos train -t train.txt -e val.txt

sed -i "" 's/<b>/#/g' extracted/*.gt.txt
sed -i "" 's/<\/b>/#/g' extracted/*.gt.txt
sed -i "" 's/<i>/_/g' extracted/*.gt.txt
sed -i "" 's/<\/i>/_/g' extracted/*.gt.txt

