'''
Keyword Dictionary
'''
BASEKEYWORDS = {
    "all",
    "gmid",
    "labels",
    "NMOS",
    "PMOS",
    "print",
    "size",
    "load",
}

'''
Binary Operator Dictionary:
'''
BASEBOPERATORS = {
    "=",
    "+",
    "-",
    "*",
    "/",
    "%",
    "@",
    "?", 
    ">", 
    "<", 
    ">=", 
    "<=", 
    ">>"
}

'''
Unary Operators Dictionary:
'''
BASEUOPERATORS = {
    
}

'''
Supported SIUNITS
'''
SIUNITS = {
    "y" : 1e-24,
    "z" : 1e-21,
    "a" : 1e-18,
    "f" : 1e-15,
    "p" : 1e-12,
    "n" : 1e-9,
    "u" : 1e-6,
    "m" : 1e-3,
    "k" : 1e3,
    "M" : 1e6,
    "G" : 1e9,
    "T" : 1e12,
    "P" : 1e15,
    "E" : 1e18,
    "Z" : 1e21,
    "Y" : 1e24
}

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

    def __eq__(self, aToken) -> bool:
        return ((self.kind == aToken.kind) and (self.value == aToken.value))
        
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