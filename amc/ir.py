"""
Ce fhichier contient la représentation intermédiaire d'une machine de turing avec m-fonction.
Cette représentation peut ensuite être simplifiée en une machine de turing sans m-fonction.
L'interpréteur python utilise cette ir, et la transpilation vers python ne fait que recréer cette ir
avant d'appeler le runtime
"""

from .parsing.ast import *


class IRNode(object):
  """
  Un noeud de la représentation intermédiaire (Stocke la traduction de context vers les noeuds fils)
  """
  def bind(self, ctx:'Context') -> 'IRNode':
    raise NotImplementedError()

  def instanciate(self, ctx:'Context'={}) -> 'FinalIRNode':
    raise NotImplementedError()

Context = dict[str, IRNode]

class FinalIRNode(IRNode):
  """
  Marqueur pour dire qu'un IRNode n'est pas dynamique
  """
  def bind(self, ctx:Context) -> IRNode:
    return self

  def instanciate(self, ctx:Context={}) -> 'FinalIRNode':
    return self
    

    
class Dyn(object):
  """
  Un noeud dynamique
  """
  class Bound(IRNode):
    """
    
    """
    def __init__(self, target:'Dyn', ctx:Context):
      self.target = target
      self.ctx = ctx

    def bind(self, ctx):
      ctx = {**self.ctx, **ctx}
      return Bound(self.target, ctx)

    def instanciate(self, ctx:Context):
      ctx = {**self.ctx, **ctx}
      return self.target.instanciate(ctx)
      
      
  def __init__(self):
    self.ctx = {}

  def bind(self, ctx:dict[str, IRNode]):
    return self.Bound(self, ctx)

  def instanciate(self, ctx):
    return self


class Action(IRNode):
  """
  Action sur la bande
  """
  pass

class FinalAction(FinalIRNode, Action):
  pass

Action.LEFT = FinalAction()
Action.RIGHT = FinalAction()

class ActionPrint(FinalAction):
  """
  Écriture sur la bande
  """
  def __init__(self, symbol:str):
    self.symbol = symbol

class DynPrint(Dyn, Action):
  """
  Un print avec un symbol synamique
  """
  def __init__(self, dyn_symbol:str):
    super().__init__()
    self.dyn_symbol = dyn_symbol

  def instanciate(self, ctx:Context):
    return ActionPrint(ctx[self.dyn_symbol])

class Rule(FinalIRNode):
  """
  Un règle
  """
  def __init__(self, actions:list[FinalAction], finalState:'State'):
    self.actions = actions
    self._finalState = finalState

  @property
  def finalState(self):
    return self._finalState.instanciate()

class DynRule(Dyn, IRNode):
  """
  
  """
  def __init__(self, actions:list[FinalAction], finalState:'State'):
    self.actions = actions
    self.finalState = finalState

  def instanciate(self, ctx:Context={}) -> FinalIRNode:
    return Rule([ a.instanciate(ctx) for a in self.actions ], self.finalState.bind(ctx))

  

class State(Dyn, IRNode):
  """
  État de la machine de turing ou mfunction selon si args est None ou pas
  """
  class Bound(Dyn.Bound):
    @property
    def name(self):
      name_args = ', '.join(f'{a}={getname(self.target.ctx[a])}')
      return f'{self.target.name}({name_args})'

  def __init__(self, name:str, args:None|tuple[str], rules:dict[str, DynRule], default_symbol_name:str=None, default_rule:DynRule=None):
    self.name = name
    if args is None :
      args = tuple()
    self.args = args
    self.rules = rules
    self.default_symbol_name = default_symbol_name
    self.default_rule = default_rule
  
  def instanciate(self, ctx:Context={}) -> FinalIRNode:
    if self.args is None :
      return self
    scope = { ctx[a] for a in self.args }
    name_args = ', '.join(f'{a}={getname(ctx[a])}')
    return State(
      f'{name}({name_args})',
      None,
      { scope.get(s, s): r.bind(scope) for s, r in self.rules },
      self.default_symbol_name,
      self.default_rule.bind(scope)
    )

  def instanciate_rule(self, symbol) -> Rule:
    r = self.rules.get(symbol)
    if r is None :
      if self.default_rule is None :
        return Rule([], State.REJECT)
      symb = self.default_symbol_name
      if symb is None :
        symb = '...'
      return self.default_rule.instanciate({symb: symbol})
    else :
      return r.instanciate()
        
      
    
State.ACCEPT = State('ACCEPT()', None, [], None, None )
State.REJECT = State('REJECT()', None, [], None, None )
    
def getname(a:str|State|State.Bound):
  if isinstance(a, str) :
    return a
  return a.name



class AMachine(object):
  """
  Machine de turing
  """
  def __init__(self, symbols:list[str]=[], states:list[State]=[], init_state:State=None):
    self.symbols = symbols
    self.states = states
    self.init_state = init_state



