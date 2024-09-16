import csv
import pickle
from pres_tuple import President

presidents = []
with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    for row in rdr:
        president = President(*row)
        presidents.append(president)


with open('potus.pkl','wb') as POTUS:
    pickle.dump(presidents,POTUS)

# test for Abraham Lincoln
p = presidents[15]
print(p.firstname, p.lastname, p.party)
