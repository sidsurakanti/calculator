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
    "iterate to next char in expression"
    try:
      self.current = next(self.expression)
    except StopIteration:
      self.current = None
  
  def lexer(self):
    while self.current is not None:
      if self.current.isspace():
        self.next()

      # if current char is a digit
      elif self.current.isdigit():
        num = ""

        # when current char is a digit, add it to a string
        while  (self.current is not None) and (self.current.isdigit() or self.current == "."):
          num += self.current
          self.next()

        # convert number into a token object (ref. tokens.py)
        yield Token("NUMBER", float(num))

      # if current char is an operator
      elif self.current in ("+", "-", "*", "/"):
        operator = self.current 
        self.next()
        yield Token(self.__operators[operator], operator)

      # if current char is a parenthesis
      elif self.current in ("(", ")"):
        paren = self.current
        self.next()
        yield Token(self.__operators[paren], paren)
    
      else:
        raise SyntaxError("Invalid Syntax")






