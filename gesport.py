import argparse
import datetime
import portefeuille

parser = argparse.ArgumentParser(
    description='''Gestionnaire de portefeuille d'actions''')


subparsers = parser.add_subparsers(title='ACTION', required=True)

parser_d = subparsers.add_parser('déposer',
    help ='À la date spécifiée, déposer la quantité de dollars spécifiée')
parser_d.add_argument('-d', '--date', metavar='DATE', default=str(datetime.date.today()), 
    help='Date effective (par défaut, date du jour)')
parser_d.add_argument('-q', '--quantité', metavar='INT', default=1,
    help='Quantité désirée (par défaut: 1)')
parser_d.add_argument('-t', '--titres', metavar='STRING', default='goog', 
    help='Le ou les titres à considérer (par défaut, tous les titres du portefeuille sont considérés)')
parser_d.add_argument('-r', '--rendement', metavar='FLOAT', default=0,
    help='Rendement annuel global (par défaut, 0)')
parser_d.add_argument('-v', '--volatilité', metavar='FLOAT', default=0, 
    help='Indice de volatilité global sur le rendement annuel (par défaut, 0)')
parser_d.add_argument('-g', '--graphique', metavar='BOOL', default=None, 
    help='''Affichage graphique (par défaut, pas d'affichage graphique)''')
parser_d.add_argument('-p', '--portefeuille', metavar='STRING', default='folio', 
    help='Nom de portefeuille (par défaut, utiliser folio)')

parser_a = subparsers.add_parser('acheter', 
    help='À la date spécifiée, acheter la quantité spécifiée des titres spécifiés')
parser_a.add_argument('-d', '--date', metavar='DATE', default=str(datetime.date.today()),
    help='Date effective (par défaut, date du jour)')
parser_a.add_argument('-q', '--quantité', metavar='INT', default=1, 
    help='Quantité désirée (par défaut: 1)')
parser_a.add_argument('-t', '--titres', metavar='STRING', default='goog',
    help='Le ou les titres à considérer (par défaut, tous les titres du portefeuille sont considérés)')
parser_a.add_argument('-r', '--rendement', metavar='FLOAT', default=0,
    help='Rendement annuel global (par défaut, 0)')
parser_a.add_argument('-v', '--volatilité', metavar='FLOAT', default=0, 
    help='Indice de volatilité global sur le rendement annuel (par défaut, 0)')
parser_a.add_argument('-g', '--graphique', metavar='BOOL', default=None, 
    help='''Affichage graphique (par défaut, pas d'affichage graphique)''')
parser_a.add_argument('-p', '--portefeuille', metavar='STRING', default='folio', 
    help='Nom de portefeuille (par défaut, utiliser folio)')

parser_v = subparsers.add_parser('vendre', 
    help='À la date spécifiée, vendre la quantité spécifiée des titres spécifiés')
parser_v.add_argument('-d', '--date', metavar='DATE', default=str(datetime.date.today()), 
    help='Date effective (par défaut, date du jour)')
parser_v.add_argument('-q', '--quantité', metavar='INT', default=1, 
    help='Quantité désirée (par défaut: 1)')
parser_v.add_argument('-t', '--titres', metavar='STRING', default='goog',
    help='Le ou les titres à considérer (par défaut, tous les titres du portefeuille sont considérés)')
parser_v.add_argument('-r', '--rendement', metavar='FLOAT', default=0,
    help='Rendement annuel global (par défaut, 0)')
parser_v.add_argument('-v', '--volatilité', metavar='FLOAT', default=0, 
    help='Indice de volatilité global sur le rendement annuel (par défaut, 0)')
parser_v.add_argument('-g', '--graphique', metavar='BOOL', default=None, 
    help='''Affichage graphique (par défaut, pas d'affichage graphique)''')
parser_v.add_argument('-p', '--portefeuille', metavar='STRING', default='folio', 
    help='Nom de portefeuille (par défaut, utiliser folio)')

parser_l = subparsers.add_parser('lister', 
    help='''À la date spécifiée, pour chacun des titres spécifiés, lister les nombres d'actions détenues ainsi que leur valeur totale''')
parser_l.add_argument('-d', '--date', metavar='DATE', default=str(datetime.date.today()), 
    help='Date effective (par défaut, date du jour)')
parser_l.add_argument('-q', '--quantité', metavar='INT', default=1, 
    help='Quantité désirée (par défaut: 1)')
parser_l.add_argument('-t', '--titres', metavar='STRING', default='goog',
    help='Le ou les titres à considérer (par défaut, tous les titres du portefeuille sont considérés)')
parser_l.add_argument('-r', '--rendement', metavar='FLOAT', default=0,
    help='Rendement annuel global (par défaut, 0)')
parser_l.add_argument('-v', '--volatilité', metavar='FLOAT', default=0, 
    help='Indice de volatilité global sur le rendement annuel (par défaut, 0)')
parser_l.add_argument('-g', '--graphique', metavar='BOOL', default=None, 
    help='''Affichage graphique (par défaut, pas d'affichage graphique)''')
parser_l.add_argument('-p', '--portefeuille', metavar='STRING', default='folio', 
    help='Nom de portefeuille (par défaut, utiliser folio)')

parser_p = subparsers.add_parser('projeter', 
    help='À la date future spécifiée, projeter la valeur totale des titres spécifiés, en tenant compte des rendements et indices de volatilité spécifiés')
parser_p.add_argument('-d', '--date', metavar='DATE', default=str(datetime.date.today()), 
    help='Date effective (par défaut, date du jour)')
parser_p.add_argument('-q', '--quantité', metavar='INT', default=1, 
    help='Quantité désirée (par défaut: 1)')
parser_p.add_argument('-t', '--titres', metavar='STRING', default='goog',
    help='Le ou les titres à considérer (par défaut, tous les titres du portefeuille sont considérés)')
parser_p.add_argument('-r', '--rendement', metavar='FLOAT', default=0,
    help='Rendement annuel global (par défaut, 0)')
parser_p.add_argument('-v', '--volatilité', metavar='FLOAT', default=0, 
    help='Indice de volatilité global sur le rendement annuel (par défaut, 0)')
parser_p.add_argument('-g', '--graphique', metavar='BOOL', default=None, 
    help='''Affichage graphique (par défaut, pas d'affichage graphique)''')
parser_p.add_argument('-p', '--portefeuille', metavar='STRING', default='folio', 
    help='Nom de portefeuille (par défaut, utiliser folio)')

args = parser.parse_args()

A = subparsers
d = args.date
q = args.quantité
t = args.titres
r = args.rendement
v = args.volatilité
g = args.graphique
p = args.portefeuille


def analyser_commande(A, d, q, t, r, v, g, p):
    return ('action={}, date={}, quantité={}, titre={}, rendement={}, volatilité={}, grphique={}, portefeuille={}'
            .format(A, d.replace('-',', '), q, t, r, v, g, p))


print(analyser_commande(A, d, q, t, r, v, g, p))


principal = portefeuille(p)


if A == 'déposer':
    principal.déposer(q, d)

if A == 'acheter':
    principal.acheter(t, q, d)

if A == 'vendre':
    principal.vendre(t, q, d)

if A == 'lister':
    principal.titres(d)
    principal.valeur_des_titres(t, d)

if A == 'projeter':
    principal.valeur_projetée(d, r)