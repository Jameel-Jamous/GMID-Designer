class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
    
    def peek(self):
        return self.tokens[self.idx] if self.idx < len(self.tokens) else None
    
    def consume(self, expected_kind=None):
        current = self.peek()
        if current and (expected_kind is None or current[0] == expected_kind):
            self.idx += 1
            ret = current
        else:
            raise SyntaxError(f"Expected {expected_kind}, got {current}")
        return ret 

    def parse(self):
        token = self.consume()
        if token[0] == "IDENTIFIER" and self.peek() and self.peek()[0] == "ASSIGN":
            var_name = token[1]
            self.consume("ASSIGN")
            expr = self.parse_expression()
            return ("assign", var_name, expr)
        elif token[0] == "PRINT":
            expr = self.parse_expression()
            return ("print", expr)
        elif token[0] == "IF":
            condition = self.parse_expression()
            self.consume("THEN")
            body = []
            while self.peek() and self.peek()[0] != "END":
                body.append(self.parse())
            self.consume("END")
            return ("if", condition, body)
        elif token[0] == "WHILE":
            condition = self.parse_expression()
            self.consume("DO")
            body = []
            while self.peek() and self.peek()[0] != "END":
                body.append(self.parse())
            self.consume("END")
            return ("while", condition, body)
        else:
            raise SyntaxError("Invalid statement")

    
    def parse_expression(self):
        left = self.consume("NUMBER" if self.peek()[0] == "NUMBER" else "IDENTIFIER")
        while self.peek() and self.peek()[0] == "OP":
            op = self.consume("OP")[1]
            right = self.consume("NUMBER")
            left = ("binop", op, left, right)
        return left