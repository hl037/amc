import typing as th
from antlr4 import InputStream, CommonTokenStream

from .parsing.amachineLexer import amachineLexer
from .parsing.amachineParser import amachineParser

def parse(f:th.IO):
  data = f.read()
  input = InputStream(data)
  lexer = amachineLexer(input)
  stream = CommonTokenStream(lexer)
  parser = amachineParser(stream)
  return parser.body()



  

