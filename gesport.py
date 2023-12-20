import argparse
import datetime


parser = argparse.ArgumentParser




subparser = parser.add_subparsers

subparser.add_argument('-d', '--date', metavar='DATE', default=str(datetime.date.today()), help='Date effective (par défaut, date du jour)')
subparser.add_argument('-q', '--quantité', metavar='INT', default=1, help='Quantité désirée (par défaut: 1)')
subparser.add_argument('-t', '--titres', metavar='STRING', help='Le ou les titres à considérer (par défaut, tous les titres du portefeuille sont considérés)')
subparser.add_argument('-r', '--rendement', metavar='FLOAT', help='Rendement annuel global (par défaut, 0)')
subparser.add_argument('-v', '--volatilité', metavar='FLOAT', default=0, help='Indice de volatilité global sur le rendement annuel (par défaut, 0)')
subparser.add_argument('-g', '--graphique', metavar='BOOL', default=None, help='''Affichage graphique (par défaut, pas d'affichage graphique)''')
subparser.add_argument('-p', '--portefeuille', metavar='STRING', default='folio', help='Nom de portefeuille (par défaut, utiliser folio)')