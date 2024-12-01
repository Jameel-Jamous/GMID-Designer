class Interpreter:
    def __init__(self):
        self.variables = {}
        
    def eval(self, node):
        if node[0] == "assign":
            _, var_name, expr = node
            self.variables[var_name] = self.eval(expr)
        elif node[0] == "print":
            _, expr = node
            print(self.eval(expr))
        elif node[0] == "binop":
            _, op, left, right = node
            left_val = int(left[1]) if left[0] == "NUMBER" else self.variables[left[1]]
            right_val = int(right[1]) if right[0] == "NUMBER" else self.variables[right[1]]
            return self.apply_operator(op, left_val, right_val)
        elif node[0] == "NUMBER":
            return int(node[1])
        elif node[0] == "IDENTIFIER":
            return self.variables[node[1]]
        else:
            raise SyntaxError(f"Unknown node type: {node[0]}")
    
    def apply_operator(self, op, left, right):
        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right
        elif op == "/":
            return left / right
        else:
            raise SyntaxError(f"Unknown operator: {op}")