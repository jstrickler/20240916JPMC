from pyparsing import *

"""
Grammar:
email ::= name '@' domain
name ::= name | '.' name
name_part ::= (alphanumeric + '_-')+
domain ::= domain_part | '.' domain_part
domain_part ::= alphanumeric+
"""

domain_part = Word(alphanums)
domain = delimitedList(domain_part, '.', combine=True)('domain')
name_part = Word(alphanums + '_-')
name = delimitedList(name_part, '.', combine=True)('name')
email_address = name + Suppress('@') + domain

with open('../DATA/correspondence.txt') as corr_in:
    text = corr_in.read()

    # scan_string() returns a list of 3-tuples.
    # *_ puts rest of each tuple in variable _, which is then ignored.
    # We only need the actual token list, which can be accessed with 
    # the specified names
    for token_list, *_ in email_address.scan_string(text):
        # print(f "Start: {start} Stop: {stop}")
        print('Name:', token_list.name)   # could also use token_list[0]
        print(f"type(token_list): {type(token_list)}")
        
        print('Domain:', token_list.domain)
        print('---')

results = email_address.search_string(text)
print(type(results))
print(results)
print(type(results[0]))    
print(type(results[0][0]))
