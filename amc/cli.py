from pathlib import Path
import sys
import click

from .parsing.ast import ASTBuilder
from .parsing.amachineParser import amachineParser
from .parsing.ast import ASTBuilder, PrettyPrinter

from . import parse


@click.group()
def main():
  pass

@main.command(name="pp")
@click.argument('input', type=click.Path('r'))
def pp(input):
  path = Path(input).resolve()
  try :
    with open(path, 'r') as f :
      tree = parse(f)
    builder = ASTBuilder(path.parent)
    ast = builder.visit(tree)
    pp = PrettyPrinter(sys.stdout)
    ast.prettyprint(pp)
  except :
    #import pdb; pdb.xpm()
    raise
  
@main.command(name="ast")
@click.argument('input', type=click.Path('r'))
def ast(input):
  path = Path(input).resolve()
  try :
    with open(path, 'r') as f :
      tree = parse(f)
    builder = ASTBuilder(path.parent)
    ast = builder.visit(tree)
    pp = PrettyPrinter(sys.stdout)
    ast.print_ast(pp)
    pp.nl()
  except :
    #import pdb; pdb.xpm()
    raise
  
  

if __name__ == "__main__" :
  main()

