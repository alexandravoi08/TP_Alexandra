import requests
import json


def lister_parties(idul):
    """
    Qu'est-ce que fait ma fonction? La fonction permet de lister les parties d'un joueur
    Quels sont les paramètres en entré de ma fonction? idul
    Quelle est la sortie et/ou le retour de ma fonction? 
    """
    url_lister = "https://python.gel.ulaval.ca/quoridor/api/lister/"
    reponse = requests.get(url_lister, params={"idul": idul})
    if reponse.status_code == 200:
        reponse = reponse.text
        json_objet = json.loads(reponse)
        json_format = json.dumps(json_objet, indent=4)
        print(json_format)
    else:
        print("Le GET sur '{}' a produit le code d'erreur {}".format(
            url_lister, reponse.status_code)
        )
