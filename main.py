import parser
from lexer import Lexer
from _parser import Parser
from _interpreter import Interpreter
from colorama import Fore, Style

print('\nType "quit" to quit the program')
while True:
  print(Fore.GREEN + ">>>" + Style.RESET_ALL, end=" ")
  expression = input()
  if "quit" in expression:
    break
  lexer = Lexer(expression)
  tokens = lexer.lexer()
  results = Parser(tokens)
  results = results.parse()
  interpreter = Interpreter(results)
  print("\n".join(map(str, [*interpreter.run()])))
 
