import os
import sys
from read import read_tsv_file
from tree import get_relation_tree
from owner import OwnershipList

if __name__=='__main__':
    # total arguments
    if len(sys.argv) != 2:
        print('usage: python owners MEDIA_NAME')
        exit(1)
    else:
        media_name = sys.argv[1]

    print('Démarrage du programme principal ...')

    current_dir = os.path.dirname(__file__)
    MEDIA_PATH = os.path.join(current_dir, '../medias_francais.tsv')
    RELATION_PATH = os.path.join(current_dir, '../relations_medias_francais.tsv')

    print('Lecture du fichier medias_francais.tsv')
    medias = read_tsv_file(MEDIA_PATH)
    print('Lecture du fichier relations_medias_francais.tsv')
    relations = read_tsv_file(RELATION_PATH)

    print("Recherche de " + media_name + " ...")
    tree = get_relation_tree(relations, media_name)
    print(tree)

    owners = OwnershipList(tree)
    print(owners)

    
