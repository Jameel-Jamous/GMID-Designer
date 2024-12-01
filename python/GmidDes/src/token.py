import re 

def tokenize(line):
    token_specification = [
        ("NUMBER", r'\d+'),
        ("IDENTIFIER", r'[a-zA-z_]\w*'),
        ("ASSIGN", r'='),
        ("OP", r'[+\-*/]'),
        ("GMID", r'gmid'),
        ("WHITESPACE", r'\s+'),
        ("MISMATCH", r'.'),
    ]
    
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    tokens = []
    for match in re.finditer(token_regex, line):
        theKind = match.lastgroup
        theValue = match.group()
        if theKind == "WHITESPACE":
            continue
        elif theKind == "MISMATCH":
            raise SyntaxError(f"Unexpected Charcter: {theValue}")
        tokens.append((theKind, theValue))