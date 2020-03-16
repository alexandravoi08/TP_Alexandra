import argparse


jeu_prof = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 5]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}
def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument("IDUL", metavar="IDUL", 
                        default="alvoi4", help="IDUL du joueur")
    parser.add_argument("-l", "--lister", dest="liste", 
                       help="Lister les identifiants de vos 20 dernières parties,")
    return parser.parse_args()

    
def afficher_damier_ascii(etat_de_jeu):
    """
    Fonction pour afficher à la console le damier complet actuel d'un état de jeu.
    :param etat_de_jeu: Un dictionnaire contenant tous les infos d'un état de jeu.
    :return: None
    """
    # 
    damier, verti, horiz = [], [], []
    # 
    for i in range(9):
        mat_damier, mat_verti, mat_horiz = [], [], []
        for j in range(9):
            mat_damier.append('.')
            mat_verti.append(' ')
            mat_horiz.append('   ')
        damier.append(mat_damier)
        verti.append(mat_verti)
        horiz.append(mat_horiz)
    # 
    posi_j_1 = etat_de_jeu['joueurs'][0]['pos']
    posi_j_2 = etat_de_jeu['joueurs'][1]['pos']
    damier[posi_j_1[1] - 1][posi_j_1[0] - 1] = '1'
    damier[posi_j_2[1] - 1][posi_j_2[0] - 1] = '2'
    damier.reverse()
    # 
    for a, b in etat_de_jeu['murs']['horizontaux']:
        horiz[b - 1][a - 1] = '---'
    horiz.reverse()
    # 
    for a, b in etat_de_jeu['murs']['verticaux']:
        verti[b - 1][a - 1] = '|'
    verti.reverse()
    # 
    sortie = "   -----------------------------------\n"
    # 
    for i in range(9):
        # 
        if i == 8:
            sortie += "1 |"
            sortie += "{}{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}  ".format(
                verti[8][0], damier[8][0],
                verti[8][1], damier[8][1],
                verti[8][2], damier[8][2],
                verti[8][3], damier[8][3],
                verti[8][4], damier[8][4],
                verti[8][5], damier[8][5],
                verti[8][6], damier[8][6],
                verti[8][7], damier[8][7],
                verti[8][8], damier[8][8],
            )
            sortie = sortie[:-1]
            sortie += "|\n"
        #
        else:
            sortie += "{} |".format(9 - i)
            sortie += "{}{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}  ".format(
                verti[i][0] if verti[i + 1][0] != '|' else '|', damier[i][0],
                verti[i][1] if verti[i + 1][1] != '|' else '|', damier[i][1],
                verti[i][2] if verti[i + 1][2] != '|' else '|', damier[i][2],
                verti[i][3] if verti[i + 1][3] != '|' else '|', damier[i][3],
                verti[i][4] if verti[i + 1][4] != '|' else '|', damier[i][4],
                verti[i][5] if verti[i + 1][5] != '|' else '|', damier[i][5],
                verti[i][6] if verti[i + 1][6] != '|' else '|', damier[i][6],
                verti[i][7] if verti[i + 1][7] != '|' else '|', damier[i][7],
                verti[i][8] if verti[i + 1][8] != '|' else '|', damier[i][8],
            )
            sortie = sortie[:-1]
            sortie += "|\n"
            sortie += "  |"
            sortie += "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
                horiz[i][0], '-' if horiz[i][0] == '---' else verti[i + 1 if i < 8 else 0][1],
                horiz[i][1] if horiz[i][0] != '---' else '---', '-' if horiz[i][1] == '---' else verti[i + 1 if i < 8 else 0][2],
                horiz[i][2] if horiz[i][1] != '---' else '---', '-' if horiz[i][2] == '---' else verti[i + 1 if i < 8 else 0][3],
                horiz[i][3] if horiz[i][2] != '---' else '---', '-' if horiz[i][3] == '---' else verti[i + 1 if i < 8 else 0][4],
                horiz[i][4] if horiz[i][3] != '---' else '---', '-' if horiz[i][4] == '---' else verti[i + 1 if i < 8 else 0][5],
                horiz[i][5] if horiz[i][4] != '---' else '---', '-' if horiz[i][5] == '---' else verti[i + 1 if i < 8 else 0][6],
                horiz[i][6] if horiz[i][5] != '---' else '---', '-' if horiz[i][6] == '---' else verti[i + 1 if i < 8 else 0][7],
                horiz[i][7] if horiz[i][6] != '---' else '---', '-' if horiz[i][7] == '---' else verti[i + 1 if i < 8 else 0][8],
                horiz[i][8] if horiz[i][7] != '---' else '---', '-' if horiz[i][8] == '---' else verti[i + 1 if i < 8 else 0][0]
            )
            sortie = sortie[:-1]
            sortie += "|\n"
    sortie += "--|-----------------------------------\n"
    sortie += "  | 1   2   3   4   5   6   7   8   9\n"
    print(sortie)      

def main():
    afficher_damier_ascii(jeu_prof)


if __name__ == "__main__":
    main()

