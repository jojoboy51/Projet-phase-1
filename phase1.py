import json
import argparse
import datetime
import requests

#ceci est l'initialisation de mon parser qui gère les arguments du module.
parser = argparse.ArgumentParser(description='Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.')

#ceci est la liste des argument qu'accept le module lors de l'appel, sybole est le seul obligatoire.
parser.add_argument('symbole', type=str, help='Nom d un symbole boursier')
parser.add_argument('-d', '--début', metavar='DATE', type=str, help='date rechercher la plus ancienne(format: AAAA-MM-JJ)')
parser.add_argument('-f', '--fin', metavar='DATE', type=str, default=datetime.date.today(), help='date rechercher la plus ancienne(format: AAAA-MM-JJ)')
parser.add_argument('-v', '--valeur', metavar='{fermeture,ouverture,min,max,volume}', type=str, default='fermeture',  help='La valeur désiré(par défaut: fermeture)')
#ici un objet args est créé contenant la liste des entré lors de l'appel du module.
args=parser.parse_args()

#méthode permettant de transformer argument de la méthode parse_args en un affichage désiré
def analyser_commande(args):
    if args.début == None:
        args.début = args.fin
    return ('titre={}: valeur={}, début=datetime.date({}), fin=datetime.date({})'.format(args.symbole, args.valeur, args.début, args.fin))

#affichage à la console des commandes donné fournie au module   
print(analyser_commande(args))

s = args.symbole
v = args.valeur
d = args.début
f = args.fin
def produire_historique(s, v, d, f):
    if d == None:
        d = f
    
    symbole = s
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

    params = {'début': d,'fin': f,}
    réponse = requests.get(url=url, params=params)
    réponse = json.loads(réponse.text)
    réponse = réponse['historique']
    t = ()
    h = []
    for clé in réponse.keys():
        t += (clé, réponse[clé][v])
    l = len(t)
    for i in range(0,l,2):
        h.append(t[i:i+2])
    print(h)
        
    print(len(t))

produire_historique(s, v, d, f)