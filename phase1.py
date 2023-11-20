import json
import argparse
import datetime
import requests


#ceci est l'initialisation de mon parser qui gère les arguments du module.
parser = argparse.ArgumentParser(
    description='Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.')

#ceci est la liste des argument qu'accept le module lors de l'appel, sybole est le seul obligatoire.
parser.add_argument('symbole', type=str, help='Nom d un symbole boursier')
parser.add_argument('-d', '--début', 
                    metavar='DATE', 
                    type=str, 
                    help='date rechercher la plus ancienne(format: AAAA-MM-JJ)')
parser.add_argument('-f', '--fin', 
                    metavar='DATE', 
                    type=str, 
                    default=str(datetime.date.today()),
                    help='date rechercher la plus ancienne(format: AAAA-MM-JJ)')
parser.add_argument('-v', '--valeur', 
                    metavar='{fermeture,ouverture,min,max,volume}', 
                    type=str, 
                    default='fermeture', 
                    help='La valeur désiré(par défaut: fermeture)')
#ici un objet args est créé contenant la liste des entré lors de l'appel du module.
args=parser.parse_args()

#redéfinition des variables d'entré pour simplifier le code
s = args.symbole
v = args.valeur
d = args.début
f = args.fin


#méthode permettant de transformer argument de la méthode parse_args en un affichage désiré
def analyser_commande(s, v, d, f):
    if d == None:
        d = f
    return ('titre={}: valeur={}, début=datetime.date({}), fin=datetime.date({})'
            .format(s, v, d.replace('-',', '), f.replace('-',', ')))

#affichage à la console des commandes donné fournie au module   
print(analyser_commande(s, v, d, f))


def produire_historique(s, v, d, f):
    if d == None:
        d = f
    
    url = f'https://pax.ulaval.ca/action/{s}/historique/'

    params = {'début': d,'fin': f,}
    réponse = requests.get(url=url, params=params)
    réponse = json.loads(réponse.text)
    réponse = réponse['historique']
    
    t = ()
    h = []
    for clé in réponse.keys():
        date = f'datetime.date({clé.replace('-',', ')})'
        t += (date, réponse[clé][v])
    
    l = len(t)
    for i in range(0,l,2):
        h.append(t[i:i+2])
    h.sort()

    return h

#affichage à la consol de l'historique demandé     
print(produire_historique(s, v, d, f))