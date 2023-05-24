from llvmlite import ir
from .parser import Node, NumberNode, AddNode, SubNode, MulNode, DivNode

def generate_code(ast):
    double = ir.DoubleType()
    function_type = ir.FunctionType(double, [])
    module = ir.Module(name="arithmetic")
    function = ir.Function(module, function_type, name="main")
    entry_block = function.append_basic_block(name="entry")
    builder = ir.IRBuilder(entry_block)

    def visit(node):
        if isinstance(node, NumberNode):
            return ir.Constant(double, node.value)
        elif isinstance(node, AddNode):
            return builder.fadd(visit(node.left), visit(node.right), name="addtmp")
        elif isinstance(node, SubNode):
            return builder.fsub(visit(node.left), visit(node.right), name="subtmp")
        elif isinstance(node, MulNode):
            return builder.fmul(visit(node.left), visit(node.right), name="multmp")
        elif isinstance(node, DivNode):
            return builder.fdiv(visit(node.left), visit(node.right), name="divtmp")
        else:
            raise ValueError("Invalid node type")

    result = visit(ast)
    builder.ret(result)

    return module

def compile_ast():
    module = generate_code(ast)
    return str(module)
