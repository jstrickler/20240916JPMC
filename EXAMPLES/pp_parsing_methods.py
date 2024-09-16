from pyparsing import *
from pp_parse_dates import date_grammar

MONTHS = """January February March April May June July August September
October November December""".split()

def replace_month(month_number):
    return MONTHS[month_number]

test_dates = (
    '10/31/1956', '1/1/2023', '01/01/2023',
    '2/28/2020', '2/29/2020', '2/29/2021',
    '4-31-2023', '01:03:1900', '9-22-1952'
)

for test_date in test_dates:
    print(test_date)
    try:
        print("   .matches()", date_grammar.matches(test_date))

        print("   .parse_string()", date_grammar.parse_string(test_date))

        print("   .search_string()", date_grammar.search_string(test_date))

        print("   .scan_string()")
        results = date_grammar.scan_string(test_date)
        for result in results:
            print(f"        {result}")
    except ValueError as err:
        print(err)
    print('-' * 60)



