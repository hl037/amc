from pathlib import Path
import sys
import click

from .parsing.ast import ASTBuilder
from .parsing.amachineParser import amachineParser
from .parsing.ast import ASTBuilder, PrettyPrinter

from . import parse, buildAST, buildIR


@click.group()
def main():
  pass

@main.command(name="pp")
@click.argument('input', type=click.Path('r'))
@click.option('--debug', '-g', is_flag=True)
def pp(input, debug):
  path = Path(input).resolve()
  try :
    with open(path, 'r') as f :
      tree = parse(f)
    builder = ASTBuilder(path.parent)
    ast = builder.visit(tree)
    pp = PrettyPrinter(sys.stdout)
    ast.prettyprint(pp)
  except :
    if debug :
      import pdb; pdb.xpm()
    raise
  
@main.command(name="ast")
@click.argument('input', type=click.Path('r'))
@click.option('--debug', '-g', is_flag=True)
def ast(input, debug):
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
    if debug :
      import pdb; pdb.xpm()
    raise

@main.command(name='compile-python')
@click.argument('input', type=click.Path('r'))
@click.option('--debug', '-g', is_flag=True)
def compilePython(input, debug):
  path = Path(input).resolve()
  try :
    with open(path, 'r') as f :
      m = buildIR(f, path)
    from .targets.python import PythonTarget
    t = PythonTarget()
    t.dump(m, sys.stdout)
  except :
    if debug :
      import pdb; pdb.xpm()
    raise


  
  
  

if __name__ == "__main__" :
  main()

