from pyparsing import *

# https://bob:secret@some.host.com:1234/more/path?p1=v1&p2=v2#junk

'''   
URL grammar
   url ::= scheme '://' [userinfo] host [port] [path] [query] [fragment]
   scheme ::= http | https | ftp | file
   userinfo ::= url_chars+ ':' url_chars+ '@'
   host ::= alphanums | host (. + alphanums)
   port ::= ':' nums
   path ::= url_chars+
   query ::= '?' + query_pairs
   query_pairs ::= query_pairs | (query_pairs '&' query_pair)
   query_pair = url_chars+ '=' url_chars+
   fragment = '#' + url_chars
   url_chars = alphanums + '-_.~%+'
'''  # Top-down grammar definition

url_chars = alphanums + '-_.~%+'  # Define legal characters in a URL

fragment  = Combine((Suppress('#') + Word(url_chars)))('fragment')  # Fragment is trailing information such as a tag ID

scheme = oneOf('https http ftp file')('scheme')   # Scheme is the type of URL (technically the type of URI) e.g. https
host = Combine(delimitedList(Word(url_chars), '.'))('host')  # Host is the registered name or IP address of the resource
port = Suppress(':') + Word(nums)('port')   # Port is optional network port of the resource  e.g. :1234
user_info = (   # User info is optional username/password e.g. USER:PASSWORD@
    Word(url_chars)('username')    # User name contains any legal url characters
    + Suppress(':')                # Skip the ':'
    + Word(url_chars)('password')  # Password contains any legal url characters
    + Suppress('@')                # Skip the '@'
)
query_pair = Group(Word(url_chars) + Suppress('=') + Word(url_chars))  # Query pair is a key/value pair separated by '='
query = Group(Suppress('?') + delimitedList(query_pair, '&'))('query')  # Query is list of query pairs separated by ''

path = Combine(
    Suppress('/')
    + OneOrMore(~query + Word(url_chars + '/'))
)('path')  # Path contains sections delimited by '/'

url_parser = (
    scheme
    + Suppress('://')
    + Optional(user_info)
    + host
    + Optional(port)
    + Optional(path)
    + Optional(query)
    + Optional(fragment)
)   # URL parser combines all of the above in the proper order
