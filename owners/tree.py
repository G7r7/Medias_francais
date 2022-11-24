from typing import List
from find import Relation, find_relations_by_target_name

class RelationTree:
    def __init__(self, data: list, root: Relation):
        self.root = root
        self.list = RelationTreeList(data, root.origine)

class RelationTreeList(list):
    def __init__(self, data: list, name: str):
        matches = find_relations_by_target_name(data, name)
        for match in matches:
            self.append(RelationTree(data, match))

def get_relation_tree(data: list, name: str) -> RelationTree:
    matches = find_relations_by_target_name(data, name)
    return RelationTree(data, matches[0])
    
