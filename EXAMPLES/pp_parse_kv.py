from pyparsing import *

ENTRIES = """
city=Atlanta
state=Georgia
population=5522942
"""

# grammar description for entries
"""
    key_value_pair ::= key '=' value
    key ::= alphanums+
    value ::= chars+
"""

value = Word(' \t' + printables, excludeChars='=')('value')  # A value can be any character, plus space or tab, _except_ '='
key = Word(alphanums)('key')  # A key can be any alphanumeric character (but not '=')
key_value_pair = Group(key + Suppress('=') + value)  # A key/value pair is key + '=' + value
kv_pairs = OneOrMore(key_value_pair)

for entry in kv_pairs.parse_string(ENTRIES):  # Parse the string
    print(f"KEY: {entry.key:12s} VALUE: {entry.value}")
