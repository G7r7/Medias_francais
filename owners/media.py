class Media:
    def __init__(self, line: list):
        self.id = line[0]
        self.nom = line[1]
        self.typeLibelle = line[2]
        self.typeCode = line[3]
        