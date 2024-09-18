from dataclasses import dataclass
import csv
from presidentdc import President

FILE_PATH = "../DATA/presidents.csv"

def iter_presidents():
    with open(FILE_PATH) as pres_in:
        rdr = csv.reader(pres_in)
        for row in rdr:
            yield President(*row)

for president in iter_presidents():
    print(president.first_name, president.last_name, "==>", president.party)
