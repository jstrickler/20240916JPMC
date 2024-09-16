from pyparsing import pyparsing_common


url_text = """
    blah blah
    https://www.potusinfo.com:8080/presidents/byterm?term=26&name=Roosevelt#bio
    blah blah
    http://www.python.org
    blah blah
"""

for result in pyparsing_common.url.search_string(url_text):
    print(result)
    print(result.scheme, result.host, result.path, result.fragment)
    print()
