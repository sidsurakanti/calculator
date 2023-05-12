from tokens import Token


class Lexer:
  __operators = {
                 "+": "ADD",
                 "-": "SUB",
                 "*": "MUL",
                 "/": "DIV",
                 "(": "LPAREN",
                 ")": "RPAREN"
                }
  
  def __init__(self, expression):
    self.expression = iter(expression)
    self.current = None
    self.next()

  def next(self):
    "Iterate thru expression"
    try:
      self.current = next(self.expression)
    except StopIteration:
      self.current = None
  
  def lexer(self):
    while self.current is not None:
      # ignore whitespace chars
      if self.current.isspace():
        self.next()

      # if current char is a digit
      elif self.current.isdigit():
        num = ""
        # check next chars to see if they're part of the number
        while  (self.current is not None) and (self.current.isdigit() or self.current == "."):
          num += self.current
          self.next()

        # tokenize number (ref. tokens.py)
        yield Token("NUMBER", float(num))

      # if operator found > tokenize operator
      elif self.current in ("+", "-", "*", "/"):
        operator = self.current 
        self.next()
        yield Token(self.__operators[operator], operator)

      # deal with parenthesis 
      elif self.current in ("(", ")"):
        paren = self.current
        self.next()
        yield Token(self.__operators[paren], paren)

      else:
        raise SyntaxError("Invalid Syntax")






