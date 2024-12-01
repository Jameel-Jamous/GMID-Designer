from src.blocks import Token, BASEKEYWORDS, BASEBOPERATORS, SIUNITS

class LineTokenizer():
    """A class that tokenizes a line of code"""
    def __init__(self, line) -> None:
        self.line = line
        self.idx = 0

    def current(self) -> str:
        """Returns the current character w/o consumption"""
        ret = None
        if self.idx < len(self.line):
            ret = self.line[self.idx]
        return ret
    
    def consume(self) -> str:
        """Consumes and returns the current character."""
        char = self.current()
        self.idx += 1
        return char
    
    def skip_comment(self):
        """Skips comments"""
        while self.current() and self.current() != '\n':
            self.consume()

    def peek(self) -> str:
        """Returns the next character w/o consumption"""
        ret = ""
        if (self.idx+1) < len(self.line):
            ret = self.line[self.idx + 1]
        return ret

    # Consider renaming this to: getValueFor() or valueHandler()
    def tokenize_identifier(self, support_for=""):
        """Handles identifiers or keywords or strings"""
        identifier = ""
        if support_for == "STRING":
            while self.current():
                identifier += self.consume() 
        elif support_for == "NUMBER":
            while self.current() and ((self.current().isdigit()) or (self.current() in SIUNITS) or (self.current() == '-')):
                identifier += self.consume()
        # TO DO: Think of a better implementation; In the case for multi-char binops, 
        # it only passes the tests because both chars of the symbols is in the dict.
        # What if you had a multi-char binop that wasn't in the dict (e.g. '<!')?
        elif support_for == "BINOP": 
            while self.current() and ((self.current() in BASEBOPERATORS) and not (self.current() == "-" and self.peek() != " ")):
                identifier += self.consume()
        else:
            while self.current() and (self.current().isalnum() or self.current() == '_'):
                identifier += self.consume()
        return identifier
    
    def tokenize(self):
        """Tokenizes the entire line"""
        tokens = []
        while self.idx < len(self.line):
            char = self.current()
            
            # Tokenize Whitespace
            if char.isspace():
                self.consume()
                continue
            
            # Tokenize Identifiers or Keywords
            if char.isalpha() or char == '_':
                identifier = self.tokenize_identifier()
                if identifier in BASEKEYWORDS:
                    tokens.append(Token('KEYWORD', identifier))
                else:
                    tokens.append(Token('IDENTIFIER', identifier))
                continue

            # Tokenize Strings
            if char == "\"" or char == "'":
                self.consume()
                string = self.tokenize_identifier("STRING") 
                tokens.append(Token('STRING', string[:-1]))
                continue
            
            # Tokenize Numbers
            if char.isdigit() or (char == "-" and self.peek().isdigit()):
                if char == "-" and self.peek() != " ":
                    self.consume()
                nums = self.tokenize_identifier("NUMBER")
                tokens.append(Token('NUMBER', nums))
                continue
              
            # Tokenize Binary Op  
            if (char in BASEBOPERATORS) and not (char == "-" and self.peek() != " "):
                binop = self.tokenize_identifier("BINOP")
                tokens.append(Token('BINOP', binop))
                continue

            # Tokenize Comments
            if char == "#":
                self.skip_comment()
                continue
            
            raise SyntaxError(f"Unexpected Char: {char}")

        return tokens