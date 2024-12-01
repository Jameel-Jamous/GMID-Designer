from src.LineTokenizer import *
import unittest as ut

comments = "# This is a comment"
spaces = "          " # 10 spaces
compound1 = "NMOS @ gmid 10"
compound2 = "x = 5 + 1"
compound3 = "x = y / z"

class TestLineTokenizer(ut.TestCase):
    def testInit(self) -> None:
        theTokenizer = LineTokenizer(comments)
        self.assertEqual(theTokenizer.line, comments,"LineTokenizer: line not initialized correctly")
        self.assertEqual(theTokenizer.idx, 0, "LineTokenizer: idx not initialized correctly") 

    def testCurrent(self) -> None:
        theTokenizer = LineTokenizer(comments)
        current_char = theTokenizer.current()
        self.assertEqual(current_char, '#', "LineTokenizer: current character did not match with the line character")
        self.assertEqual(theTokenizer.idx, 0, "LineTokenizer: current character was consumed when not consume was not called")

    def testCurrentOverflow(self) -> None:
        theTokenizer = LineTokenizer(comments)
        theTokenizer.idx = len(comments)
        current_char = theTokenizer.current()
        self.assertIsNone(current_char, "LineTokenizer: self.current did not return None on an invalid idx")
    
    def testConsume(self) -> None:
        theTokenizer = LineTokenizer(comments)
        current_char = theTokenizer.consume()
        self.assertEqual(current_char, '#', "LineTokenizer: consume did not return the current character")
        self.assertEqual(theTokenizer.idx, 1, "LineTokenizer: consume did not consume the current character")
        self.assertEqual(theTokenizer.current(), ' ', "LineTokenizer: consume did not consume the current character")

    def testTokenizeWhiteSpace(self) -> None:
        tokens = []
        theTokenizer = LineTokenizer(spaces)
        tokens = theTokenizer.tokenize()
        self.assertEqual(tokens, [], "LineTokenizer: Whitespace was tokenized")

    def testTokenizeComments(self) -> None:
        tokens = []
        theTokenizer = LineTokenizer(comments)
        tokens = theTokenizer.tokenize()
        self.assertEqual(tokens, [], "LineTokenizer: Comment was tokenized")

    def testTokenizeIdentifier(self) -> None:
        tokens = []
        correct_kind = 0
        correct_value = 0
        for key in BASEKEYWORDS:
            identifier = key[:-1]
            tokens = LineTokenizer(identifier).tokenize()
            if tokens[0].kind == "IDENTIFIER":
                correct_kind += 1 

            if tokens[0].value == identifier:
                correct_value += 1

        self.assertEqual(correct_kind, len(BASEKEYWORDS), "LineTokenizer: Identifier: Incorrect kind were tokenized")
        self.assertEqual(correct_value, len(BASEKEYWORDS), "LineTokenizer: Identifier: Incorrect values were tokenized")
        
    def testTokenizeKeywords(self) -> None:
        tokens = []
        correct_kind = 0
        correct_value = 0
        for key in BASEKEYWORDS:
            identifier = key
            tokens = LineTokenizer(identifier).tokenize()
            if tokens[0].kind == "KEYWORD":
                correct_kind += 1 

            if tokens[0].value == identifier:
                correct_value += 1

        self.assertEqual(correct_kind, len(BASEKEYWORDS), "LineTokenizer: Keyword: Incorrect kind were tokenized")
        self.assertEqual(correct_value, len(BASEKEYWORDS), "LineTokenizer: Keyword: Incorrect values were tokenized")
    
    def testTokenizeString(self) -> None:
        testString = "\"This is a test string\""
        tokens = LineTokenizer(testString).tokenize()
        self.assertEqual(tokens[0].kind, "STRING", "LineTokenizer: String: Incorrect kind were tokenized")
        self.assertEqual(tokens[0].value, "This is a test string", "LineTokenizer: String: Incorrect values were tokenized")
        testString1 = "'This is another test string'"
        tokens = LineTokenizer(testString1).tokenize()
        self.assertEqual(tokens[0].kind, "STRING", "LineTokenizer: String: Incorrect kind were tokenized")
        self.assertEqual(tokens[0].value, "This is another test string", "LineTokenizer: String: Incorrect values were tokenized")
 
    def testTokenizeString2(self) -> None:
        testString = "\"# This is a test string\""
        tokens = LineTokenizer(testString).tokenize()
        self.assertEqual(tokens[0].kind, "STRING", "LineTokenizer: String: Incorrect kind were tokenized")
        self.assertEqual(tokens[0].value, "# This is a test string", "LineTokenizer: String: Incorrect values were tokenized")
        testString1 = "\" This is another test string\""
        tokens = LineTokenizer(testString1).tokenize()
        self.assertEqual(tokens[0].kind, "STRING", "LineTokenizer: String: Incorrect kind were tokenized")
        self.assertEqual(tokens[0].value, " This is another test string", "LineTokenizer: String: Incorrect values were tokenized")
 
    def testTokenizeNumbers(self) -> None:
        testNumber = "321"
        tokens = LineTokenizer(testNumber).tokenize()
        self.assertEqual(tokens[0].kind, "NUMBER", "LineTokenizer: Number: Incorrect kind were tokenized")
        self.assertEqual(tokens[0].value, testNumber, "LineTokenizer: Number: Incorrect values were tokenized")
        testNumber1 = "321u"
        tokens = LineTokenizer(testNumber1).tokenize()
        self.assertEqual(tokens[0].kind, "NUMBER", "LineTokenizer: Number: Incorrect kind were tokenized")
        self.assertEqual(tokens[0].value, testNumber1, "LineTokenizer: Number: Incorrect values were tokenized")
 
    def testTokenizeBinaryOp(self):
        tokens = []
        correct_kind = 0
        correct_value = 0
        for key in BASEBOPERATORS:
            identifier = key
            tokens = LineTokenizer(identifier).tokenize()
            if tokens[0].kind == "BINOP":
                correct_kind += 1 

            if tokens[0].value == identifier:
                correct_value += 1
            

        self.assertEqual(correct_kind, len(BASEBOPERATORS), f"LineTokenizer: Binary Op : Incorrect kind were tokenized")
        self.assertEqual(correct_value, len(BASEBOPERATORS), "LineTokenizer: Binary Op: Incorrect values were tokenized")

    def testTokenizeCompounds(self):
        tokens = LineTokenizer(compound1).tokenize()    
        correct = [Token("KEYWORD", "NMOS"), Token("BINOP", "@"), Token("KEYWORD", "gmid"), Token("NUMBER", "10")]
        passed = 0
        for i in range(len(correct)):
            if tokens[i] == correct[i]:
                passed += 1

        self.assertEqual(passed, len(correct), "LineTokenizer: Incorrect Objects were tokenized")
        self.assertEqual(len(correct), len(tokens), "LineTokenizer: tokenized and correct dont match")
        print(tokens)

    def testTokenizeCompounds(self):
        tokens = LineTokenizer(compound2).tokenize()    
        correct = [Token("IDENTIFIER", "x"), Token("BINOP", "="), Token("NUMBER", "5"), Token("BINOP", "+"), Token("NUMBER", "1")]
        passed = 0
        for i in range(len(tokens)):
            if tokens[i] == correct[i]:
                passed += 1
        self.assertEqual(passed, len(correct), "LineTokenizer: Incorrect Objects were tokenized")
        self.assertEqual(len(correct), len(tokens), "LineTokenizer: tokenized and correct dont match")
        
        tokens = LineTokenizer(compound3).tokenize()    
        correct = [Token("IDENTIFIER", "x"), Token("BINOP", "="), Token("IDENTIFIER", "y"), Token("BINOP", "/"), Token("IDENTIFIER", "z")]
        passed = 0
        for i in range(len(correct)):
            if tokens[i] == correct[i]:
                passed += 1
        self.assertEqual(passed, len(correct), "LineTokenizer: Incorrect Objects were tokenized")
        self.assertEqual(len(correct), len(tokens), "LineTokenizer: tokenized and correct dont match")
        
        tokens = LineTokenizer("y = -5 - -5").tokenize()    
        correct = [Token("IDENTIFIER", "y"), Token("BINOP", "="), Token("NUMBER", "-5"), Token("BINOP", "-"), Token("NUMBER", "-5")]
        passed = 0
        for i in range(len(correct)):
            if tokens[i] == correct[i]:
                print(tokens[i])
                passed += 1
        self.assertEqual(passed, len(correct), "LineTokenizer: Incorrect Objects were tokenized")
        self.assertEqual(len(correct), len(tokens), "LineTokenizer: tokenized and correct dont match")

    def testTokenizeErrors(self):
        incorrectChars = "$"
        with self.assertRaises(SyntaxError, msg="LineTokenizer: Exception not raised when incorrect chars were tokenized"):
            LineTokenizer(incorrectChars).tokenize()
