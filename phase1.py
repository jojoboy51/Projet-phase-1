import json
import argparse
import datetime


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
    
print(analyser_commande(args))

def produire_historique():
    
    pass
