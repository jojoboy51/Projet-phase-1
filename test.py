import json
import argparse

symbole = 'goog'
url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

params = {
    'début': '2019-02-18',
    'fin': '2019-02-24',
}

réponse = requests.get(url=url, params=params)
réponse = json.loads(réponse.text)
print(réponse)[]


#réponse vaux ça pour les valeur d'entré -d=2019-02-18 -f=2019-02-24 goog
{'compagnie': 'Google Inc.', 'symbole': 'GOOG', 'période': 'du 2019-02-18 au 2019-02-24',
 'historique': {'2019-02-22': {'ouverture': 1100.9, 'min': 1095.6, 'max': 1111.24, 'fermeture': 1110.37, 'volume': 1049545},
 '2019-02-21': {'ouverture': 1110.84, 'min': 1092.52, 'max': 1111.94, 'fermeture': 1096.97, 'volume': 1415473},
 '2019-02-20': {'ouverture': 1119.99, 'min': 1105.28, 'max': 1123.41, 'fermeture': 1113.8, 'volume': 1087817},
 '2019-02-19': {'ouverture': 1110.0, 'min': 1110.0, 'max': 1121.89, 'fermeture': 1118.56, 'volume': 1046628}}}


#ce qui m'est retourné avec ces lignes de commande
for clé in réponse.keys():
        print(f'{clé}, {réponse[clé][v]}')

titre=goog: valeur=fermeture, début=datetime.date(2019-02-19), fin=datetime.date(2019-02-21)
2019-02-21, 1096.97
2019-02-20, 1113.8
2019-02-19, 1118.56