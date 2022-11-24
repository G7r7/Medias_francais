import csv

def read_tsv_file(path: str):
    with open(path) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        lines = [line for line in tsv_file]
        return lines