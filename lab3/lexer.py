import re

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f'Token({self.type}, {self.value})'
        return f'Token({self.type})'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.keywords = {'if', 'else', 'while', 'for', 'break', 'continue', 'return', 'elif', 'in'}
        self.separators = {'(', ')', '{', '}', ',', ';', ':'}
        self.operators = {'+', '-', '*', '/', '>', '<', '%'}
        self.comments_pattern = re.compile(r'#.*?$', re.DOTALL)

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def tokenize_string(self):
        quote_char = self.current_char
        self.advance()
        string_literal = ''
        while self.current_char is not None and self.current_char != quote_char:
            string_literal += self.current_char
            self.advance()
        if self.current_char != quote_char:
            raise ValueError("Unclosed string literal")
        self.advance()
        return Token('LITERAL', string_literal)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha() or self.current_char == '_' or self.current_char == '$':
                identifier = self.current_char
                self.advance()
                while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
                    identifier += self.current_char
                    self.advance()
                if identifier in self.keywords:
                    return Token('KEYWORD', identifier)
                return Token('IDENTIFIER', identifier)

            if self.current_char.isdigit():
                literal = ''
                while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
                    literal += self.current_char
                    self.advance()
                return Token('LITERAL', literal)

            if self.current_char == '"' or self.current_char == "'":
                return self.tokenize_string()

            if self.current_char in self.separators:
                separator = self.current_char
                self.advance()
                return Token('SEPARATOR', separator)

            if self.current_char == '!':
                if self.text[self.pos:self.pos+2] == '!=':
                    self.advance()
                    self.advance()
                    return Token('OPERATOR', '!=')

            if self.current_char == '=':
                if self.text[self.pos:self.pos+2] == '==':
                    self.advance()
                    self.advance()
                    return Token('OPERATOR', '==')
                self.advance()
                return Token('OPERATOR', '=')

            if self.current_char in self.operators:
                operator = self.current_char
                self.advance()
                return Token('OPERATOR', operator)

            match = self.comments_pattern.match(self.text, self.pos)
            if match:
                comment = match.group(0)
                self.pos += len(comment)
                break

            self.advance()
            return Token('UNKNOWN')

        return Token('EOF')

    @staticmethod
    def check_parentheses(text):
        stack = []
        opening_parentheses = {'(', '[', '{'}
        closing_parentheses = {')', ']', '}'}
        parentheses_pairs = {'(': ')', '[': ']', '{': '}'}

        for char in text:
            if char in opening_parentheses:
                stack.append(char)
            elif char in closing_parentheses:
                if not stack or parentheses_pairs[stack.pop()] != char:
                    raise ValueError(f"Unmatched closing parenthesis: '{char}'")

        if stack:
            raise ValueError(f"Unmatched opening parenthesis: '{stack[-1]}'")


while True:
    try:
        text = input('Input line of code>')
        Lexer.check_parentheses(text)
    except EOFError:
        break
    if not text:
        continue
    lexer = Lexer(text)
    token = lexer.get_next_token()
    while token.type != 'EOF':
        print(token)
        token = lexer.get_next_token()

"""
if 37 == 29:
elif number != 2
var = 23 * number / 24
else:
for i in range(30)
if "2sdsafsd" < "21dfasrwr":
if (1 != 29:
"""