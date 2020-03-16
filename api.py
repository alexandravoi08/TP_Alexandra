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

def initialiser_partie(idul):
    """
    Qu'est-ce que fait ma fonction? La fonction permet de lister les parties d'un joueur
    Quels sont les paramètres en entré de ma fonction? idul
    Quelle est la sortie et/ou le retour de ma fonction? 
    """
    url_initial = "https://python.gel.ulaval.ca/quoridor/api/initialiser/"
    try:
        reponse = requests.post(url_initial, data={"idul": idul})
        if reponse.status_code == 200:
            json_rep = reponse.json()
            return json_rep["id"], json_rep["état"]
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}".format(
                url_initial, reponse.status_code)
            )
    except RuntimeError as error:
        print(error)



    def jouer_coup(id_partie, type_coup, position):
    url_coup = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        response = requests.post(url_coup, data={'id': id_partie, 'type': type_coup, 'pos': position})
        if response.status_code == 200:
            json_res = response.json()
            return json_res
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_coup, response.status_code)
            )
    except RuntimeError as error:
        print(error)


print(initialiser_partie("alvoi4"))