from tree import RelationTree
from typing import List
from find import find_media_type_by_name
                
class Ownership:
    def __init__(self, value: float, name: str, media_type: str):
        self.value = value
        self.name = name
        self.media_type = media_type

class OwnershipList:
    def __init__(self, tree: RelationTree, medias: list):
        self.object_name: str = tree.root.cible
        self.ownerships: List[Ownership] = []
        self.calculate(tree, medias)

    def __str__(self) -> str:
        ret = self.object_name + " : \n" 
        for ownership in self.ownerships:
            ret += ownership.name + " : " \
                + str(round(ownership.value * 100, 2)) + "% " \
                + "(" + ownership.media_type + ")" \
                + "\n"
        return ret

    def calculate(self, tree: RelationTree, medias: list, value=1.0):
        try:
            multiplier = float(tree.root.valeur.replace(',', '.'))
        except:
            print(f"Avertissement : relation ignorée, valeur \"{tree.root.valeur}\" - \"{tree.root.origine}\"")
            multiplier = 100.0

        value = value * multiplier / 100
        if len(tree.list) == 0:
            media_type = find_media_type_by_name(medias, tree.root.origine)
            self.ownerships.append(
                Ownership(value, tree.root.origine, media_type)
            )
        else:
            for tree in tree.list:
                self.calculate(tree, medias, value)

