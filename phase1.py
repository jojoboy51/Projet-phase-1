import json
import argparse

parser = argparse.ArgumentParser(description='Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.')
parser.add_argument('symbole', help='Nom d un symbole boursier')
parser.add_argument('-d', '--début', metavar='DATE',  help='date rechercher la plus ancienne(format: AAAA-MM-JJ)')
parser.add_argument('-f', '--fin', metavar='DATE', help='date rechercher la plus ancienne(format: AAAA-MM-JJ)')
parser.add_argument('-v', '--valeur', metavar='{fermeture,ouverture,min,max,volume}', help='La valeur désiré(par défaut: fermeture)')
args = parser.parse_args()

