from pyparsing import *

def upper_case_it(tokens):  # A function to uppercase every string in a list of strings
    return [t.upper() for t in tokens]

prefix = 'A Fist Full of '  # Fixed-text prefix of what the script is looking for

fist_contents = Word(alphas + ' ')  # Text can be letters or spaces (should fine-tune to require at least letter)

fist_contents.set_parse_action(upper_case_it)  # Call upper_case_it() when target text found

title_parser = Combine(prefix + fist_contents)('title')  # Complete title is "A Fist Full of" + more text

titles = (
    'A Fist Full of Dollars',
    'A Fist Full of Spaghetti',
    'A Fist Full of Wombats',
    'A Fist Full of Jelly Beans',
    'A Fist Full of Clint Eastwood Movies',
)

for title in titles:
    print(title_parser.parse_string(title).title)  # Parse the titles of of the string
