from pyparsing import *

test_string = "spam=123"

grammar = Word(alphas)('key') + Suppress('=') + Word(nums)('value')

result = grammar.parse_string(test_string)
print(f"type(result): {type(result)}")  # result is ParseResults object
print(f"result: {result}")  # string representation is a list
print(f"result.key, result.value: {result.key}, {result.value}")  # access tokens as attributes
print(f"result[0], result[1]: {result[0]}, {result[1]}")          # access tokens by position
print(f"result['key'], result['value']: {result['key']}, {result['value']}")  # access tokens by keys
key, value = result                    # unpack tokens
print(f"key, value: {key}, {value}")