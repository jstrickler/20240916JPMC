from pyparsing import *

"""Grammar Description
date = month + separator + day + separator + year
month = 1-digit month or 2-digit month
1-digit-month = optional '0' + digit '1' through digit '9'
2-digit-months = '10' | '11' | '12'
month = month-name | short-month-name | 1-digit-month | 2-digit-month
separator = '/' | '-' | ':'
day = '1' |  '2' | '3' ... '30' | '31'   will check for invalid days
year = ('1' or '2') + digit + digit + digit 
"""
def validate_day(text, position, tokens):
    month = tokens[0].lstrip('0') # remove leading '0'
    day = int(tokens[1])
    year = int(tokens[2])
    if any(
        [
            (month in ('4', '6', '9', '11')) and (day > 30),
            (month == '2') and (day > 29),
            (month == '2') and (day == 29) and (year % 4),
        ]   
    ):
        raise ValueError(f"Day {day} is invalid for month {month}")
    


year = Combine(oneOf('1 2') + Word(nums, exact=3))
one_digit_day = Combine(Optional('0') + oneOf("1 2 3 4 5 6 7 8 9"))
two_digit_day = oneOf("""
     10 11 12 13 14 15 16 17 18 19 20 21 22 
    23 24 25 26 27 28 29 30 31
""")
day = one_digit_day ^ two_digit_day
separator = Suppress(oneOf("/ - :"))
one_digit_month = Combine(Optional('0') + oneOf('1 2 3 4 5 6 7 8 9'))
two_digit_month = oneOf('10 11 12')
month = one_digit_month ^ two_digit_month  # '^' means Or

date_grammar = month + separator + day + separator + year
date_grammar.set_parse_action(validate_day)

if __name__ == "__main__":
    test_dates = (
        '10/31/1956', '1/1/2023', '01/01/2023',
        '2/28/2020', '2/29/2020', '2/29/2021',
        '4-31-2023', '01:03:1900',
    )
    for test_date in test_dates:
        print(f"{test_date}:", end=' ')
        try:
            result = date_grammar.matches(test_date)
        except ValueError as err:
            print(err)
        else:
            print(result)