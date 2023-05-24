# main.py
from arithmetic_compiler.lexer import tokenize
from arithmetic_compiler.parser import parse
from arithmetic_compiler.codegen import compile_ast

if __name__ == "__main__":
    expression = "(3 + 5) * 2"
    tokens = list(tokenize(expression))
    ast = parse(tokens)
    llvm_ir = compile_ast(ast)
    print(llvm_ir)
