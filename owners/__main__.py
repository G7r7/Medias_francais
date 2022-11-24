import os
from read import read_tsv_file
from tree import get_relation_tree

if __name__=='__main__':
    print('Démarrage du programme principal ...')

    current_dir = os.path.dirname(__file__)
    MEDIA_PATH = os.path.join(current_dir, '../medias_francais.tsv')
    RELATION_PATH = os.path.join(current_dir, '../relations_medias_francais.tsv')

    print('Lecture du fichier medias_francais.tsv')
    medias = read_tsv_file(MEDIA_PATH)
    print('Lecture du fichier relations_medias_francais.tsv')
    relations = read_tsv_file(RELATION_PATH)

    print("Recherche de Télérama ...")
    tree = get_relation_tree(relations, 'Télérama')
    print(tree)

    
