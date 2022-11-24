from typing import List
from find import Relation, find_relations_by_target_name
        
class RelationTree(Relation):
    def __init__(self, data: list, name: str):
        matches = find_relations_by_target_name(data, name)
        if len(matches) == 0:
            return
        self = matches[0]
        self.tree = RelationTree(data, self.origine)
