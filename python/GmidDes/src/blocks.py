'''
Blocks for Tokens
'''
class Token():
    """A class that represents a single token"""
    def __init__(self, kind, value) -> None:
        self.kind = kind
        self.value = value

    def __repr__(self) -> str:
        return f"Token({self.kind}, {repr(self.value)})"

    def toStr(self):
        return f"Token({self.kind}, {repr(self.value)})"
'''
Blocks for Parser
'''
class Node:
    """A Base class for all nodes in AST""" 
    pass

class AssignmentNode(Node):
    def __init__(self, var_name, expression) -> None:
        self.var_name = var_name
        self.expression = expression
    
class PrintNode(Node):
    def __init__(self, expression) -> None:
        self.expression = expression

class BinaryOpNode(Node):
    def __init__(self, operator, larg, rarg) -> None:
        self.operator = operator
        self.larg = larg
        self.rarg = rarg

class NumberNode(Node):
    def __init__(self, value) -> None:
        self.value = value

class IdentifierNode(Node):
    def __init__(self, name) -> None:
        self.name = name