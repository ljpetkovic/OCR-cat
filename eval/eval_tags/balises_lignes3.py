import re




######### Fonctions ##############################

 

def regexbaliseouv(x):
    return r'([ <](([< ])*{0}([ >])*)+[>])|([<](([< ])*{0}([ >])*)+[ >])|(^(([< ])*{0}([ >])*)+[>])'.format(x) # x = 'b' ou 'i'

def regexbalisefer(x):
    return r'(([<]*[ ]*[/][ ]*{0}([ >])*)+[ >])|(([<]*[ ]*[/][ ]*{0}([ >])*)+$)'.format(x)  # x = 'b' ou 'i'


def bonneBalises(ligne):
    L_bo_b = [] # liste des span des balises ouvrantes b ex : [(0,4),(19,22)]
    L_bf_b = [] # liste des span des balises fermantes b ex : [(6,10),(36,40)]
    L_bo_i = [] # liste des span des balises ouvrantes i ex : [(41,45),(70,74)]
    L_bf_i = [] # liste des span des balises fermantes i ex : [(60,64),(80,84)]
    pattern_bo_b = re.compile(r'<b>')   # pattern balise ouvrante correcte
    matches_bo_b = pattern_bo_b.finditer(ligne) # itérateur
    pattern_bf_b = re.compile(r'</b>')   # pattern balise fermante correcte
    matches_bf_b = pattern_bf_b.finditer(ligne)
    pattern_bo_i = re.compile(r'<i>')   # pattern balise ouvrante correcte
    matches_bo_i = pattern_bo_i.finditer(ligne) # itérateur
    pattern_bf_i = re.compile(r'</i>')   # pattern balise fermante correcte
    matches_bf_i = pattern_bf_i.finditer(ligne)
    for match in matches_bo_b:
        u = match.span()
        L_bo_b.append(u)
    for match in matches_bf_b:
        u = match.span()
        L_bf_b.append(u)
    for match in matches_bo_i:
        u = match.span()
        L_bo_i.append(u)
    for match in matches_bf_i:
        u = match.span()
        L_bf_i.append(u)
    ### On enlève toute les bonnes balises :
    ligne_test = re.sub(r'<b>', '', ligne)
    ligne_test = re.sub(r'</b>', '', ligne_test)
    ligne_test = re.sub(r'<i>', '', ligne_test)
    ligne_test = re.sub(r'</i>', '', ligne_test)
    ### Et on teste ce qui reste (ici présence de <, >) remarque : on ne cherche pas les / tous seuls, car présence de fractions éventuelles
    if re.search(r'[<>]',ligne_test):    
        return False,[]
    elif (len(L_bo_b) == len(L_bf_b)) and (len(L_bo_i) == len(L_bf_i)) and len(L_bo_b) == 0 and len(L_bo_i) == 0:  # cas où il s'agit d'une ligne a priori sans balise
        return True,[True]
    elif (len(L_bo_b) == len(L_bf_b)) and (len(L_bo_i) == len(L_bf_i)):
        return True, [L_bo_b,L_bf_b,L_bo_i,L_bf_i]  # bonnes balises et même nombre ouvrantes/fermantes
    else:
        return True, [False]   # bonnes balises mais pas le même nombre ouvrantes/fermantes

def verifEntrelacement(L_bo_b,L_bf_b,L_bo_i,L_bf_i):
    verif_b = [ u[1]<v[0] for u,v in zip(L_bo_b,L_bf_b)]
    verif_i = [ u[1]<v[0] for u,v in zip(L_bo_i,L_bf_i)]
    def not_between(Liste,Liste_o,Liste_f):
        return [ not ( u[1]<x[0] and x[1]<v[0]) for x in Liste for u,v in zip(Liste_o,Liste_f)]
    verif_bo_i = not_between(L_bo_b,L_bo_i,L_bf_i) # <b> ne doit pas etre entre <i> et </i>
    verif_bf_i = not_between(L_bf_b,L_bo_i,L_bf_i) # </b> ne doit pas etre entre <i> et </i>
    verif_io_b = not_between(L_bo_i,L_bo_b,L_bf_b) # <i> ne doit pas etre entre <b> et </b>
    verif_if_b = not_between(L_bf_i,L_bo_b,L_bf_b) # </i> ne doit pas etre entre <b> et </b>
    return all([all(verif_b), all(verif_i), all(verif_bo_i),all(verif_bf_i),all(verif_io_b),all(verif_if_b)])  # all(list) = True si et seulement tous les éléments de list sont True


def correctionBalisesPleines(ligne):
    ligne_corr = re.sub(regexbaliseouv('b'), r' <b>', ligne)
    ligne_corr = re.sub(regexbalisefer('b'), r'</b> ', ligne_corr)
    ligne_corr = re.sub(regexbaliseouv('i'), r' <i>', ligne_corr)
    ligne_corr = re.sub(regexbalisefer('i'), r'</i> ', ligne_corr)
    return ligne_corr


def correctionBalisesVides(ligne):
    pass


    

def affichage(ligne,parametres,max_taille):
    bonneBalise,sans_balise,bon_nombre_balise,corr,entrelacement = parametres
    l = ligne.strip()
    if sans_balise:
        print(l+' '*(max_taille-len(l))+' | '+'0'+' | ')
    else:
        if not corr[0]:
            if bonneBalise and entrelacement:
                print(l+' '*(max_taille-len(l))+' | '+'1'+' | ')
            elif bonneBalise and bon_nombre_balise:
                print(l+' '*(max_taille-len(l))+' | '+'2'+' | '+' PROBLEME ORDRE DES BALISES')
            elif bonneBalise:
                print(l+' '*(max_taille-len(l))+' | '+'3'+' | '+' BALISES MANQUANTES')
            else:
                print(l+' '*(max_taille-len(l))+' | '+'4'+' | '+' PROBLEME BALISE')
        else:
            ligne_corr = corr[1]
            if bonneBalise and entrelacement:
                print(l+' '*(max_taille-len(l))+' | '+'1'+' | '+ligne_corr)
            elif bonneBalise and bon_nombre_balise:
                print(l+' '*(max_taille-len(l))+' | '+'2'+' | '+ligne_corr)
            elif bonneBalise:
                print(l+' '*(max_taille-len(l))+' | '+'3'+' | '+ligne_corr)
            else:
                print(l+' '*(max_taille-len(l))+' | '+'4'+' | '+ligne_corr)
                



######### Texte de description des sorties #######


with open("balises_lignes_description.txt") as myfile:
    f = myfile.read()
    print(f)


########## Importation des données ################

print('')
print('AVERTISSEMENT : Agrandir le shell au maximum!')

texte = input("Donner le nom du fichier à traiter : ") #Pour_les_tests.txt


print('')
print('########################################################################################################################################################################')
print('')

if texte == 'fichier_demo.txt':
    nombre_ligne = 16
elif texte == 'Pour_les_tests.txt':
    nombre_ligne = 300


with open(texte) as myfile:
    head = [next(myfile) for x in range(nombre_ligne)]  # pour extraire seulement les 'nombre_ligne' premières lignes
    taille = [len(ligne) for ligne in head] # liste des longueurs des lignes
    max_taille = max(taille) - 1 # longueur de la ligne la plus longue
    print(max_taille)

    


######### Corps du programme #####################


for i,ligne in enumerate(head[:nombre_ligne]):
    corr = [False,[]]
    verif = bonneBalises(ligne)
    if verif[0] == False:
        corr[0] = True
        ligne_corr = correctionBalisesPleines(ligne)
        corr[1] = ligne_corr
        verif = bonneBalises(ligne_corr)
    if verif[0] == False:
        bonneBalise = False,
        sans_balise = False
        bon_nombre_balise = False
        entrelacement = False
    else:
        bonneBalise = True
        if len(verif[1]) == 1:
            if verif[1][0] == True:
                sans_balise = True
                bon_nombre_balise = True
                entrelacement = True
            else:
                sans_balise = False
                bon_nombre_balise = False
                entrelacement = False
        else:
            L_bo_b,L_bf_b,L_bo_i,L_bf_i = verif[1]
            entrelacement = verifEntrelacement(L_bo_b,L_bf_b,L_bo_i,L_bf_i)
            sans_balise = False
            bon_nombre_balise = True
    parametres = (bonneBalise,sans_balise,bon_nombre_balise,corr,entrelacement)         
    affichage(ligne,parametres,max_taille)
 
    
 