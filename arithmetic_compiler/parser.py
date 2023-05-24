
class Node:
    pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

class BinOpNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class AddNode(BinOpNode):
    pass

class SubNode(BinOpNode):
    pass

class MulNode(BinOpNode):
    pass

class DivNode(BinOpNode):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token = None
        self._advance()
        self._advance()

    def _advance(self):
        if self.next_token is None and len(self.tokens) > 0:
            self.next_token = self.tokens.pop(0)

        self.current_token = self.next_token
        if len(self.tokens) > 0:
            self.next_token = self.tokens.pop(0)
        else:
            self.next_token = None

    def parse(self):
        return self.expr()

    def expr(self):
        node = self.term()
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            if self.current_token.type == 'PLUS':
                self._advance()
                node = AddNode(node, self.term())
            elif self.current_token.type == 'MINUS':
                self._advance()
                node = SubNode(node, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token and self.current_token.type in ('MUL', 'DIV'):
            if self.current_token.type == 'MUL':
                self._advance()
                node = MulNode(node, self.factor())
            elif self.current_token.type == 'DIV':
                self._advance()
                node = DivNode(node, self.factor())
        return node

    def factor(self):
        if not self.current_token:
            raise SyntaxError("Unexpected end of input")

        if self.current_token.type == 'NUMBER':
            node = NumberNode(float(self.current_token.value))
            self._advance()
            return node
        elif self.current_token.type == 'LPAR':
            self._advance()
            node = self.expr()
            if self.current_token.type == 'RPAR':
                self._advance()
                return node
        raise SyntaxError("Invalid syntax")

def parse(tokens):
    parser = Parser(tokens)
    ast = parser.parse()
    if parser.current_token is not None:
        raise SyntaxError("Unexpected token at the end of input")

    return ast
