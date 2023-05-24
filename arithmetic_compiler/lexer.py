import re
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

TOKEN_MAP = {
    r'\d+(\.\d*)?': 'NUMBER',
    r'\+': 'PLUS',
    r'-': 'MINUS',
    r'\*': 'MUL',
    r'/': 'DIV',
    r'\(': 'LPAR',
    r'\)': 'RPAR',
}

def tokenize(expression):
    token_pattern = '|'.join(f'(?P<{name}>{pattern})' for pattern, name in TOKEN_MAP.items())
    for match in re.finditer(token_pattern, expression):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        yield Token(token_type, token_value)

expression = "(3 + 5) * 2"
tokens = list(tokenize(expression))
