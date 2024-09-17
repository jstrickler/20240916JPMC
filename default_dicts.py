import collections

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

if 'CMH' in airports:
    print(f"{airports['CMH'] = }")

print(f"{airports.get('CMH') = }")

def get_default():
    return "NO AIRPORT WITH THAT NAME"

airport2 = collections.defaultdict(get_default)

airport2['RDU'] = "Raleigh/Durham"
airport2['IAD'] = "Washington-Dulles"

print(f"{airport2['IAD'] = }")
print(f"{airport2['CMH'] = }")
