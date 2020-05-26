import re




######### Fonctions ##############################

def regexbalise(x):
    return r'[ <{0}>]*<[ <{0}>]*{0}([ <{0}>]*>[ <{0}>]*)*|([ <{0}>]*<[ <{0}>]*)*{0}[ <{0}>]*>[ <{0}>]*'.format(x) # x = 'b' ou 'i'


def regexbaliseouv(x):
    return r'[ <{0}>]*<[ <{0}>]*{0}([ <{0}>]*>[ <{0}>]*)*'.format(x) # x = 'b' ou 'i'

def regexbalisefer(x):
    return r'[ <{0}>]+/[ <{0}>]*|[ <{0}>]*/[ <{0}>]+'.format(x)  # x = 'b' ou 'i'


def bonneBalises(ligne):
    L_bo = [] # liste des span des balises ouvrantes  ex : [(0,4),(19,22)]
    L_bf = [] # liste des span des balises ouvrantes  ex : [(6,10),(36,40)]
    pattern_bo = re.compile(r'<b>')   # pattern balise ouvrante correcte
    matches_bo = pattern_bo.finditer(ligne) # itérateur
    pattern_bf = re.compile(r'</b>')   # pattern balise fermante correcte
    matches_bf = pattern_bf.finditer(ligne)
    for match in matches_bo:
        u = match.span()
        L_bo.append(u)
    for match in matches_bf:
        u = match.span()
        L_bf.append(u)
    ### On enlève toute les bonnes balises :
    ligne_test = re.sub(r'<b>', '', ligne)
    ligne_test = re.sub(r'</b>', '', ligne_test)
    ### Et on test ce qui reste (ici présence de <, >) remarque : on ne cherche pas les / tous seuls, car présence de fractions éventuelles
    if re.search(r'[<>]',ligne_test):    
        return False,[]
    elif (len(L_bo) == len(L_bf)) and len(L_bo) == 0:  # cas où il s'agit d'une ligne a priori sans balise
        return True,[True]
    elif (len(L_bo) == len(L_bf)):
        return True, [L_bo,L_bf]  # bonnes balises et même nombre ouvrantes/fermantes
    else:
        return True, [False]   # bonnes balises mais pas le même nombre ouvrantes/fermantes

def verifEntrelacement(L_bo,L_bf):
    verif = [ u[1]<v[0] for u,v in zip(L_bo,L_bf)]   
    return all(verif)  # all(list) = True si et seulement tous les éléments de list sont True


def correctionBalises(ligne):
    ligne_corr = re.sub(regexbaliseouv('b'), r'<b>', ligne)
    ligne_corr = re.sub(regexbalisefer('b'), r'</b>', ligne_corr)
    return ligne_corr

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
input('AVERTISSEMENT : Agrandir le shell au maximum!')




print('')
print('########################################################################################################################################################################')
print('')

 

nombre_ligne = 106


with open("Pour_les_tests.txt") as myfile:
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
        ligne_corr = correctionBalises(ligne)
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
            L_bo,L_bf = verif[1]
            entrelacement = verifEntrelacement(L_bo,L_bf)
            sans_balise = False
            bon_nombre_balise = True
    parametres = (bonneBalise,sans_balise,bon_nombre_balise,corr,entrelacement)         
    affichage(ligne,parametres,max_taille)
 
    
 
