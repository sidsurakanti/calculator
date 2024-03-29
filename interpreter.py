import nodes
from number import Number


class Interpreter:
  def __init__(self, nodes):
    self.nodes = nodes

  def run(self):
    for node in self.nodes:
      yield self.visit(node)

  def visit(self, node):
    # if node is a number value return final result
    if type(node) is nodes.NumberNode:
      result = Number(node.value)
      return int(result) if str(result).isdigit() else result

    # recursively take left and right values of a operator nodes 
    # to perform binary operations
    if type(node) is nodes.OperatorNode:
      left = self.visit(node.left)
      right = self.visit(node.right)
      types = {
               "ADD": left.__add__,
               "SUB": left.__sub__, 
               "MUL": left.__mul__, 
               "DIV": left.__div__,
              }
      return types[node.operator.type](right)
