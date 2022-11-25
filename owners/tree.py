from typing import List
from find import Relation, find_relations_by_target_name

class RelationTree:
    def __init__(self, data: list, root: Relation):
        self.root = root
        self.list = RelationTreeList(data, root.origine)

    def __str__(self, level=0):
        ret = "\t"*level \
            + self.root.cible \
            + '-' \
            + self.root.valeur \
            + '-' \
            + self.root.origine \
            + "\n"
        for tree in self.list:
            ret += tree.__str__(level+1)
        return ret

class RelationTreeList(List[RelationTree]):
    def __init__(self, data: list, name: str):
        matches = find_relations_by_target_name(data, name)
        for match in matches:
            self.append(RelationTree(data, match))

def get_relation_tree(data: list, name: str) -> RelationTree:
    matches = find_relations_by_target_name(data, name)
    if len(matches) == 0:
        print('Erreur : aucun média trouvé pour "' + name + '"')
        exit(1)
    return RelationTree(data, matches[0])
    
