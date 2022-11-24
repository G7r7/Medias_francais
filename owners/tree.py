from typing import List
from find import Relation, find_relations_by_target_name
        
class RelationTree:
    def __init__(self, data: list, name: str):
        matches = find_relations_by_target_name(data, name)
        if len(matches) == 0:
            return
        self.root = matches[0]
        self.list = RelationTreeList(data, self.root.origine)


class RelationTreeList(list):
    def __init__(self, data: list, name: str):
        matches = find_relations_by_target_name(data, name)
        for match in matches:
            self.append(RelationTree(data, match.cible))