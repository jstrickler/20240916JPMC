import csv
from presidentdc import President

FILE_PATH = "../DATA/presidents.csv"

class Presidents:
    def __init__(self):
        pres_in = open(FILE_PATH)
        self._rdr = csv.reader(pres_in)

    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self._rdr)
        return President(*row)


iter_pres = Presidents()

for president in iter_pres:
    print(president.first_name, president.last_name, "==>", president.party)
