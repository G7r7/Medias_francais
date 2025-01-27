import typing
from relation import Relation

def find_relations_by_target_name(data: list, name: str) -> typing.List[Relation]:
    results = [line for line in data if line[3] == name]
    relations = []
    for result in results:
        relations.append(Relation(result))
    return relations

def find_media_type_by_name(data: list, name: str) -> str:
    results = [line for line in data if line[1] == name]
    return results[0][2]

