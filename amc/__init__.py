from pathlib import Path
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

def buildAST(f:th.IO, path:Path):
  pt = parse(f)
  from .parsing import ast
  return ast.ASTBuilder.build(pt, path.parent)

def buildIR(f:th.IO, path:Path):
  from .parsing import irbuilder
  _ast = buildAST(f, path)
  return irbuilder.IRBuilder.build(_ast, path.parent)




  

