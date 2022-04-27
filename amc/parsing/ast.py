import typing as th
from pathlib import Path
from io import StringIO

from .amachineVisitor import amachineVisitor
from .amachineParser import amachineParser

class PrettyPrinter(object):
  """
  class to handle pretty printing of the AST and its configuration
  """
  def __init__(self, output:th.IO=None, indent='  ', space=' ', nl='\n', align=True, parent=None):
    if output is None :
      output = StringIO()
    self.output = output
    self.indent = indent
    self.space = space
    self.nl_char = nl
    self.align = align
    self.parent = parent
    
    self.indent_level = 0
    self.isLineStart = True
    

  def __rshift__(self, val):
    self.indent_level += val

  def __lshift__(self, val):
    self.indent_level -= val

  def ws(self):
    self.output.write(self.space)

  def nl(self):
    self.output.write(self.nl_char)
    self.isLineStart = True

  def _writeIndent(self):
    self.output.write(self.indent * self.indent_level)

  def write(self, val, size=0):
    if self.isLineStart :
      self._writeIndent()
      self.isLineStart = False
    self.output.write(val)
    if (r := size - len(val)) > 0 :
      ws_cont = r // len(self.space)
      single_s_count = r % len(self.space)
      self.output.write(' ' * single_s_count)
      self.output.write(self.space * ws_cont)

  def buffer(self):
    return PrettyPrinter(None, indent=self.indent, space=self.space, nl=self.nl_char, align=self.align, parent=self)

  def commit(self, size=0):
    assert self.parent is not None
    self.parent.write(self.output.getvalue(), size)

  def __len__(self):
    assert self.parent is not None
    return len(self.output.getvalue())

class ASTNode(object):
  """
  An ASTNode
  """
  def prettyprint(self, pp:PrettyPrinter):
    raise NotImplementedError()
    
  def print_ast(self, pp:PrettyPrinter):
    raise NotImplementedError()

class ASTAbstractSymbol(ASTNode):
  """
  Un symbol ou la notion de case "vide" (fin de la bande)
  """
  pass

class ASTSymbol(ASTAbstractSymbol):
  """
  Un symbol (cette classe permet de gérer les parenthèse et les backslash)
  """
  def __init__(self, escaped_name:str):
    self.name = self.unescape(escaped_name)

  def escape(self, n:str):
    return n.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

  def unescape(self, n:str):
    return n.replace('\\\\', '\\$').replace('\\(', '(').replace('\\)', ')').replace('\\$', '\\')

  def prettyprint(self, pp:PrettyPrinter):
    pp.write(self.name)

  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTSymbol({self.name})')

class ASTNoSymbol(ASTAbstractSymbol):
  def prettyprint(self, pp:PrettyPrinter):
    pass # Le symbol vide est représenté par l'absence de caractère

  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTNoSymbol()')


class ASTInclude(ASTNode):
  """
  Inclusion d'un autre fichier
  """
  def __init__(self, path:Path):
    self.path = path

  def prettyprint(self, pp:PrettyPrinter):
    pp.write(f'include({self.path})')
    pp.nl()
    
  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTInclude({self.path})')

class ASTSymbols(ASTNode):
  """
  Liste de symbols
  """
  def __init__(self, symbols:list[ASTSymbol]):
    self.symbols = symbols

  def prettyprint(self, pp:PrettyPrinter):
    pp.write('symbols')
    pp.nl()
    pp>>1
    for s in self.symbols :
      s.prettyprint(pp)
      pp.nl()
    pp<<1
    
  def print_ast(self, pp:PrettyPrinter):
    pp.write('ASTSymbols(')
    pp.nl()
    pp>>1
    for s in self.symbols :
      s.print_ast(pp)
      pp.write(',')
      pp.nl()
    pp<<1
    pp.write(')')


class ASTInitial(ASTNode):
  """
  Référence vers l'état initial
  """
  def __init__(self, initial:'ASTAbstractStateReference'):
    self.initial = initial
  
  def prettyprint(self, pp:PrettyPrinter):
    pp.write('init')
    pp.nl()
    pp>>1
    self.initial.prettyprint(pp)
    pp.nl()
    pp<<1
    
  def print_ast(self, pp:PrettyPrinter):
    pp.write('ASTInitial(')
    pp.nl()
    pp>>1
    self.initial.print_ast(pp)
    pp.nl()
    pp<<1
    pp.write(')')

class ASTAbstractAction(ASTNode):
  """
  Une action de la tête de lecture
  """
  pass

class ASTActionPrint(ASTAbstractAction):
  """
  Action d'écriture
  """
  def __init__(self, symbol:ASTSymbol):
    self.symbol = symbol
    
  def prettyprint(self, pp:PrettyPrinter):
    pp.write('P:')
    self.symbol.prettyprint(pp)

  def print_ast(self, pp:PrettyPrinter):
    pp.write('ASTActionPrint(')
    self.symbol.print_ast(pp)
    pp.write(')')



class ASTActionLeft(ASTAbstractAction):
  """
  Action de déplacement de la tête de lecture vers la gauche
  """
  def prettyprint(self, pp:PrettyPrinter):
    pp.write('<-')
    
  def print_ast(self, pp:PrettyPrinter):
    pp.write('ASTActionLeft()')

class ASTActionRight(ASTAbstractAction):
  """
  Action de déplacemnet de la tête de lecture vers la droite
  """
  def prettyprint(self, pp:PrettyPrinter):
    pp.write('->')
    
  def print_ast(self, pp:PrettyPrinter):
    pp.write('ASTActionRight()')

class ASTAbstractStateReference(ASTNode):
  """
  Une référence vers un état de la machine de turing
  """
  pass

class ASTMFunctionReference(ASTAbstractStateReference):
  """
  Une référence vers une m-fonction
  """
  def __init__(self, name:str, args:list[ASTAbstractStateReference|ASTSymbol]):
    self.name = name
    self.args = args

  def prettyprint(self, pp:PrettyPrinter):
    pp.write(self.name)
    pp.write('(')
    for a in self.args[:-1] :
      a.prettyprint(pp)
      pp.write(',')
      pp.ws()
    if self.args :
      self.args[-1].prettyprint(pp)
    pp.write(')')

  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTMFunctionReference({self.name},')
    pp.nl()
    pp>>1
    for a in self.args :
      a.print_ast(pp)
      pp.write(',')
      pp.nl()
    pp<<1
    pp.write(')')

class ASTStateReference(ASTAbstractStateReference):
  """
  Une référence vers un état classique
  """
  def __init__(self, name:str):
    self.name = name

  def prettyprint(self, pp:PrettyPrinter):
    pp.write(self.name)

  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTStateReference({self.name})')

class ASTAbstractRule(ASTNode):
  """
  Une règle d'un état (actions selon le symbole de la bande). Peut être soit une règle directe, soit une règle générique
  """
  def prettyprint(self, pp0:PrettyPrinter, pp1:PrettyPrinter=None, pp2:PrettyPrinter=None):
    if pp1 is None :
      pp1 = pp0
    if pp2 is None :
      pp2 = pp0
    self._prettyprint(pp0, pp1, pp2)

class ASTRule(ASTAbstractRule):
  """
  Une règle directe
  """
  def __init__(self, symbol:ASTAbstractSymbol, actions:list[ASTAbstractAction], final_state:ASTAbstractStateReference):
    self.symbol = symbol
    self.actions = actions
    self.final_state = final_state

  def _prettyprint(self, pp0:PrettyPrinter, pp1:PrettyPrinter, pp2:PrettyPrinter):
    if self.symbol :
      self.symbol.prettyprint(pp0)
      pp0.ws()
    if self.actions :
      for a in self.actions :
        a.prettyprint(pp1)
        pp1.ws()
    self.final_state.prettyprint(pp2)
    pp2.nl()

  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTRule(')
    pp.nl()
    pp>>1
    if self.symbol :
      self.symbol.print_ast(pp)
      pp.write(',')
      pp.nl()
    for a in self.actions :
      a.print_ast(pp)
      pp.write(',')
      pp.nl()
    self.final_state.print_ast(pp)
    pp.nl()
    pp<<1
    pp.write(')')

class ASTGenericRule(ASTNode):
  """
  Une règle générique, par défaut, ou qui capture le symbol
  """
  def __init__(self, symbol_name:ASTSymbol, actions:list[ASTAbstractAction], final_state:ASTAbstractStateReference):
    self.symbol_name = symbol_name
    self.actions = actions
    self.final_state = final_state

  def _prettyprint(self, pp0:PrettyPrinter, pp1:PrettyPrinter, pp2:PrettyPrinter):
    if self.symbol_name :
      self.symbol.prettyprint(pp0)
      pp0.ws()
    if self.actions :
      for a in self.actions :
        a.prettyprint(pp1)
        pp1.ws()
    self.final_state.prettyprint(pp2)
    pp2.nl()

  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTGenericRule(')
    pp.nl()
    pp>>1
    if self.symbol :
      self.symbol.print_ast(pp)
      pp.write(',')
      pp.nl()
    for a in self.actions :
      a.print_ast(pp)
      pp.write(',')
      pp.nl()
    self.final_state.print_ast(pp)
    pp.nl()
    pp<<1
    pp.write(')')

def _printrules(rules:list[ASTAbstractRule], pp:PrettyPrinter):
  if pp.align :
    pps = [ (pp.buffer(), pp.buffer(), pp.buffer()) for _ in rules ]
    for r, ppargs in zip(rules, pps) :
      r.prettyprint(*ppargs)
    shifts = [ max( len(ppa[i]) for ppa in pps ) for i in range(3) ]
    for r, ppargs in zip(rules, pps) :
      for s, ppa in zip(shifts, ppargs) :
        ppa.commit(s)
      pp.nl()
  else :
    for r in rules :
      r.prettyprint(pp)
      pp.nl()

class ASTMFunctionDecl(ASTNode):
  """
  M-fonction qui permet de générer des états à la volée
  """
  ARG_STATE = 0
  ARG_SYMBOL = 1
  def __init__(self, name:str, args:list[ASTAbstractStateReference|ASTSymbol], rules:list[ASTRule]):
    self.name = name
    self.args = args
    self.rules = rules
    self.signature = tuple( self.ARG_SYMBOL if isinstance(a, ASTSymbol) else self.ARG_STATE for a in args )

  def prettyprint(self, pp:PrettyPrinter):
    pp.write(self.name)
    pp.write('(')
    for a in self.args[:-1] :
      a.prettyprint(pp)
      pp.write(',')
      pp.ws()
    if self.args :
      self.args[-1].prettyprint(pp)
    pp.write(')')
    pp.nl()
    pp>>1
    _printrules(self.rules, pp)
    pp<<1

  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTMFunctionDecl({self.name}')
    pp.nl()
    pp>>1
    for a in self.args :
      a.print_ast(pp)
      pp.write(',')
      pp.nl()
    for r in self.rules :
      r.print_ast(pp)
      pp.write(',')
      pp.nl()
    pp<<1
    pp.write(')')

class ASTStateDecl(ASTNode):
  """
  État d'une machine de turring
  """
  def __init__(self, name:str, rules:list[ASTRule]):
    self.name = name
    self.rules = rules
    
  def prettyprint(self, pp:PrettyPrinter):
    pp.write(self.name)
    pp.nl()
    pp>>1
    _printrules(self.rules, pp)
    pp<<1
    
  def print_ast(self, pp:PrettyPrinter):
    pp.write(f'ASTStateDecl({self.name}')
    pp.nl()
    pp>>1
    for r in self.rules :
      r.print_ast(pp)
      pp.write(',')
      pp.nl()
    pp<<1
    pp.write(')')


class ASTAMachine(ASTNode):
  """
  Racine de l'AST
  """
  def __init__(self, exprs:list[ASTNode]):
    self.exprs = exprs

  def prettyprint(self, pp:PrettyPrinter):
    for expr in self.exprs :
      expr.prettyprint(pp)
      pp.nl()

  def print_ast(self, pp:PrettyPrinter):
    pp.write('ASTAMachine(')
    pp.nl()
    pp>>1
    for expr in self.exprs :
      expr.print_ast(pp)
      pp.write(',')
      pp.nl()
    pp<<1
    pp.write(')')


class ASTBuilder(amachineVisitor):
  """
  Build and ast from a parsetree
  """
  def __init__(self, base_path:Path):
    self.base_path = base_path

  def visit(self, tree) -> ASTNode:
    return super().visit(tree)[0]
  
  def defaultResult(self):
    return []
  
  def aggregateResult(self, aggregate, next_result):
    aggregate.extend(next_result)
    return aggregate

  def visitBody(self, ctx:amachineParser.BodyContext):
    nodes = super().visitBody(ctx)
    return ASTAMachine(nodes),
  
  def visitInclude(self, ctx:amachineParser.IncludeContext):
    inc = str(ctx.INCLUDE())
    start = 'include('
    assert inc.startswith(start) and inc[-1] == ')'
    return ASTInclude((self.base_path / inc[len(start):-1]).resolve().absolute()),
  
  def visitSymbols(self, ctx:amachineParser.SymbolsContext):
    symbols = super().visitSymbols(ctx)
    return ASTSymbols(symbols),

  def visitSymbol_decl(self, ctx:amachineParser.Symbol_declContext):
    return ASTSymbol(str(ctx.SYMBOL_NAME())),

  def visitInitial(self, ctx:amachineParser.InitialContext):
    ref, = super().visitInitial(ctx)
    return ASTInitial(ref),
  
  def visitM_function_decl(self, ctx:amachineParser.M_function_declContext):
    children = self.visitChildren(ctx)
    args = children[:-1]
    rules = children[-1]
    return ASTMFunctionDecl(str(ctx.STATE_NAME()), args, rules),

  def visitT_decl(self, ctx:amachineParser.T_declContext):
    s = ctx.T_STATE_NAME()
    if s is not None :
      return ASTStateReference(str(s)),
    s = ctx.T_SYMBOL_NAME()
    if s is not None :
      return ASTSymbol(str(s)),

    
  def visitAm_state_decl(self, ctx:amachineParser.Am_state_declContext):
    children = super().visitAm_state_decl(ctx)
    rules = children[-1]
    name = ctx.STATE_NAME()
    return ASTStateDecl(str(name), rules),

  
  def visitAm_state_rules(self, ctx:amachineParser.Am_state_rulesContext):
    return super().visitAm_state_rules(ctx),
  
  def visitAm_state_rule(self, ctx:amachineParser.Am_state_ruleContext):
    return ASTRule(*super().visitAm_state_rule(ctx)),

  def visitAm_state_rule_symbol(self, ctx:amachineParser.Am_state_rule_symbolContext):
    s = ctx.DEFAULT()
    if s:
      return ASTSymbol('...'),
    s = ctx.T_SYMBOL_NAME()
    if s:
      return ASTSymbol(str(s)),
    s = ctx.SYMBOL_NAME()
    if s :
      return ASTSymbol(str(s)),
    return ASTNoSymbol(),
  
  def visitAm_state_rule_actions(self, ctx:amachineParser.Am_state_rule_actionsContext):
    return super().visitAm_state_rule_actions(ctx),
  
  def visitAm_state_rule_action(self, ctx:amachineParser.Am_state_rule_actionContext):
    s = ctx.LEFT()
    if s :
      return ASTActionLeft(),
    s = ctx.RIGHT()
    if s :
      return ASTActionRight(),
    symb = super().visitAm_state_rule_action(ctx)
    if symb :
      symb, = symb
    else :
      symb = ASTNoSymbol()
    return ASTActionPrint(symb),

  
  def visitAm_state(self, ctx:amachineParser.Am_stateContext):
    m_function =  self.visitChildren(ctx)
    if m_function :
      return m_function
    s = ctx.T_STATE_NAME()
    if s is None :
      s = ctx.STATE_NAME()
    return ASTStateReference(str(s)),

  def visitM_function(self, ctx:amachineParser.M_functionContext):
    args = super().visitM_function(ctx)
    s = ctx.STATE_NAME()
    return ASTMFunctionReference(str(s), args),
    
  def visitSymbol(self, ctx:amachineParser.SymbolContext):
    s = ctx.T_SYMBOL_NAME()
    if s is None :
      s = ctx.SYMBOL_NAME()
    return ASTSymbol(str(s)),




