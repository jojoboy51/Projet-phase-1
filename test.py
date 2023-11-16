import json
import argparse

parser = argparse.ArgumentParser(description='additionner deux nombre')
parser.add_argument('premier', type=int, help='première valeur', metavar='--rrrrrr')
parser.add_argument('deuxième', type=int, help='deuxième valeur')
args = parser.parse_args()
def addition(premier, deuxième):
    return premier + deuxième
