from lexer import Lexer
from _parser import Parser
from interpreter import Interpreter

from colorama import Fore, Style


print('\nType "quit" to exit calculator')

while True:
  # get input
  print(Fore.BLUE + ">>>" + Style.RESET_ALL, end=" ")
  expression = input()

  if "quit" == expression.lower():
    break

  # get results
  tokens = Lexer(expression).lexer()
  results = Parser(tokens).parse()
  interpreter = Interpreter(results)

  # display results
  print("\n".join(map(str, [*interpreter.run()])))
 
