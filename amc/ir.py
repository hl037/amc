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
      return self.__class__(self.target, ctx)

    def instanciate(self, ctx:Context={}):
      ctx = {**self.ctx, **ctx}
      return self.target.instanciate(ctx)
      
      
  def __init__(self):
    self.ctx = {}

  def bind(self, ctx:dict[str, IRNode]):
    return self.Bound(self, ctx)

class Action(IRNode):
  """
  Action sur la bande
  """
  pass

class FinalAction(FinalIRNode, Action):
  def __repr__(self):
    if self is Action.LEFT :
      return '<Action <- >'
    elif self is Action.RIGHT :
      return '<Action -> >'

Action.LEFT = FinalAction()
Action.RIGHT = FinalAction()

class ActionPrint(FinalAction):
  """
  Écriture sur la bande
  """
  def __init__(self, symbol:str):
    self.symbol = symbol

  def __repr__(self):
    return f'<Action P:{self.symbol}>'

class DynPrint(Dyn, Action):
  """
  Un print avec un symbol synamique
  """
  def __init__(self, dyn_symbol:str):
    super().__init__()
    self.dyn_symbol = dyn_symbol

  def instanciate(self, ctx:Context):
    return ActionPrint(ctx[self.dyn_symbol])

class StateReference(Dyn, IRNode):
  """
  Référence vers un état (stocke aussi la traduction de context)
  """
  class Bound(Dyn.Bound):
    @property
    def name(self):
      return self.target.name

class Rule(FinalIRNode):
  """
  Un règle
  """
  def __init__(self, actions:list[FinalAction], finalState:StateReference):
    self.actions = actions
    self._finalState = finalState

  @property
  def finalState(self):
    return self._finalState.instanciate()

class DynRule(Dyn, IRNode):
  """
  
  """
  def __init__(self, actions:list[FinalAction], finalState:StateReference):
    self.actions = actions
    self.finalState = finalState

  def instanciate(self, ctx:Context={}) -> FinalIRNode:
    return Rule([ a.instanciate(ctx) for a in self.actions ], self.finalState.bind(ctx))

class StatePlaceholder(StateReference):
  """
  Un placeholder pour un état
  """
  def __init__(self, ph_name:str):
    self.ph_name = ph_name

  def instanciate(self, ctx:Context):
    rv = ctx.get(self.ph_name, None)
    if rv is None :
      raise RuntimeError('Oops, placeholder not in context. Should have been caught at ir building time')
    while isinstance(rv, (Dyn.Bound, StateReference)) :
      rv = rv.instanciate()
    return rv

  @property
  def name(self):
    return self.ph_name


class StaticStateReference(StateReference):
    
  def __init__(self, state:'State', args:tuple[StateReference|str]):
    self.state = state
    self.args = args

  def instanciate(self, ctx:Context={}):
    return self.state.instanciate({
      name: (
        (
          ctx[a]
          if is_generic(a) else
          a
        )
        if isinstance(a, str) else
        a.bind(ctx)
      )
      for name, a in zip(self.state.args, self.args)
    })

  @property
  def name(self):
    name_args = ', '.join(f'{name}={getname(a)}' for name, a in zip(self.state.args, self.args) )
    return f'{self.state.name}({name_args})'
    
  

class State(Dyn, IRNode):
  """
  État de la machine de turing ou mfunction selon si args est None ou pas
  """
  class Bound(Dyn.Bound):
    @property
    def name(self):
      name_args = ', '.join(f'{a}={getname(self.ctx[a])}' for a in self.target.args)
      return f'{self.target.name}({name_args})'

  def __init__(self, name:str, args:tuple[str], rules:dict[str, DynRule], default_symbol_name:str=None, default_rule:DynRule=None):
    self.name = name
    if args is None :
      args = tuple()
    self.args = args
    self.rules = rules
    self.default_symbol_name = default_symbol_name
    self.default_rule = default_rule
    
  def instanciate(self, ctx:Context={}) -> FinalIRNode:
    if not len(self.args) :
      return self
    scope = { a: ctx[a] for a in self.args }
    name_args = ', '.join(f'{a}={getname(ctx[a])}' for a in self.args)
    return State(
      f'{self.name}({name_args})',
      tuple(),
      { scope.get(s, s): r.bind(scope) for s, r in self.rules.items() },
      self.default_symbol_name,
      self.default_rule.bind(scope) if self.default_rule is not None else None
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
        
  def __repr__(self):
    return f'<State "{self.name}">'
    
State.ACCEPT = State('ACCEPT()', None, {}, None, None )
State.REJECT = State('REJECT()', None, {}, None, None )
    
def getname(a:str|State|State.Bound):
  if isinstance(a, str) :
    return a
  return a.name



class AMachine(object):
  """
  Machine de turing
  """
  def __init__(self, symbols:list[str]=[], states:list[State]=[], init_state:StateReference=None):
    self.symbols = symbols
    self.states = states
    self.init_state = init_state



