class Relation:
    def __init__(self, line: list):
        self.id = line[0]
        self.origine = line[1]
        self.valeur = line[2]
        self.cible = line[3]
        self.source = line[4]
        self.datePublication = line[5]
        self.dateConsultation = line[6]