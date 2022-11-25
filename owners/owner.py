from tree import RelationTree
from typing import List
                
class Ownership:
    def __init__(self, value: float, name: str):
        self.value = value
        self.name = name

class OwnershipList:
    def __init__(self, tree: RelationTree):
        self.object_name: str = tree.root.cible
        self.ownerships: List[Ownership] = []
        self.calculate(tree)

    def __str__(self) -> str:
        ret = self.object_name + " : \n" 
        for ownership in self.ownerships:
            ret += ownership.name + " : " \
                + str(round(ownership.value * 100, 2)) + "%\n"
        return ret

    def calculate(self, tree: RelationTree, value=1.0):
        value = value * (float(tree.root.valeur.replace(',', '.')) / 100)
        if len(tree.list) == 0:
            self.ownerships.append(
                Ownership(value, tree.root.origine)
            )
        else:
            for tree in tree.list:
                self.calculate(tree, value)

