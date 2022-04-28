from collections import defaultdict

from .ast import *

from ..ir import *

from .. import parse, buildAST

class UnknownRootExpressionType(RuntimeError):
  pass

class UnknownStateReferenceType(RuntimeError):
  pass

class UnknownRuleType(RuntimeError):
  pass

class UnknownActionType(RuntimeError):
  pass

class UnknownArgumentType(RuntimeError):
  pass

class NoInitialState(RuntimeError):
  def __init__(self):
    super().__init__('There is no initial state nor non-m-function state')

class MFunctionAlreadyDefined(RuntimeError):
  def __init__(self, mfuncdecl:ASTMFunctionDecl):
    a = ', '.join(
      'State' if t == ASTMFunctionDecl.ARG_STATE else 'Symbol'
      for t in mfuncdecl.signature
    )
    super().__init__(f'{mfuncdecl.name}({a})')

class StateAlreadyDefined(RuntimeError):
  def __init__(self, statedecl: ASTStateDecl):
    super().__init__(statedecl.name)



class MFunctionNotDefined(RuntimeError):
  def __init__(self, mfuncdecl:ASTMFunctionReference):
    a = ', '.join(
      'State' if t == ASTMFunctionDecl.ARG_STATE else 'Symbol'
      for t in mfuncdecl.signature
    )
    super().__init__(f'{mfuncdecl.name}({a})')

class StateNotDefined(RuntimeError):
  def __init__(self, statedecl: ASTStateReference):
    super().__init__(statedecl.name)

def stateNotDefined(state: ASTAbstractStateReference):
  if isinstance(state, ASTMFunctionReference) :
    return MFunctionNotDefined(state)
  else :
    return StateNotDefined(state)

class MultipleDefaultRules(RuntimeError):
  def __init__(self, state:State):
    super().__init__(f'In state {state.name}')


class IRBuilder(object):
  """
  Constuit une représentation intermédiaire de la machine de turing 
  """
  @classmethod
  def build(cls, ast:ASTAMachine, base_path:Path):
    builder = cls(base_path)
    return builder.visit(ast)

  def __init__(self, base_path:Path):
    self.base_paths = [base_path]

  @property
  def base_path(self):
    return self.base_paths[0]

  def push_base_path(self, base_path):
    self.base_paths.append(base_path)

  def pop_base_path(self):
    return self.base_paths.pop()

  def visit(self, ast:ASTAMachine):
    self.symbols = []
    self.includes = []
    self.inits = []
    self.mfunctions = []
    self.states = [] # type: list[ASTStateDecl]

    self.symbol_cache = set()
    self.state_cache = defaultdict(lambda: {}) # type: defaultdict[str, dict[tuple[int], tuple(State, ASTNode)]]
    self.referenced_states = defaultdict(lambda: set()) # type: defaultdict[str, set[tuple[int]]] # Utilisé pour supprimer les états non accessibles
    self.init_ref = None # type: ASTAbstractStateReference
    self.init_state = None
    
    self.include_pass(ast)
    self.decl_pass()
    self.link_pass()
    return self.create_machine()

  def reference(self, decl):
    self.referenced_states[decl.name].add(decl.signature)

  def is_referenced(self, decl):
    return decl.signature in self.referenced_states[decl.name]
    

  def include_pass(self, ast):
    """
    Effectue tous les includes en DFS afin de correctement ordonner les expressions
    """
    for e in ast.exprs :
      if isinstance(e, ASTInclude) :
        self.visitInclude(e)
      elif isinstance(e, ASTSymbols) :
        self.symbols.append(e)
      elif isinstance(e, ASTInitial) :
        self.inits.append(e)
      elif isinstance(e, ASTMFunctionDecl) :
        self.mfunctions.append(e)
      elif isinstance(e, ASTStateDecl) :
        self.states.append(e)
      else :
        raise UnknownRootExpressionType()

  def visitInclude(self, e:ASTInclude):
    new_file = (self.base_path / e.path).resolve()
    if not new_file.exists() :
      new_file = new_file.with_name(f'{new_file.name}.amachine')
    self.push_base_path(new_file.parent)
    with open(new_file, 'r') as f:
      ast = buildAST(f, self.base_path)
    self.include_pass(ast)
  
  def decl_pass(self):
    """
    Passe répertoriant toutes les déclarations qui permettront de résoudre les états
    et les m-fonction (ainsi que vérifier le type de leurs arguments)
    dans les passes ultérieures
    """
    for symbol_decl in self.symbols :
      self.visitSymbols(symbol_decl)

    for mfunc_decl in self.mfunctions :
      self.visit1MFunctionDecl(mfunc_decl)
      
    for state_decl in self.states :
      self.visit1StateDecl(state_decl)

    if self.inits :
      self.visitInitial(self.inits[-1])
    
  def visitSymbols(self, symbols:ASTSymbols):
    self.symbol_cache.update( s.name for s in symbols.symbols )

  def visit1MFunctionDecl(self, mfuncdecl:ASTMFunctionDecl):
    d = self.state_cache[mfuncdecl.name]
    mf2 = d.get(mfuncdecl.signature, None)
    if mf2 is not None :
      raise MFunctionAlreadyDefined(mf2)
    d[mfuncdecl.signature] = State(
      mfuncdecl.name,
      [ a.name for a in mfuncdecl.args ],
      [], None, None
    ), mfuncdecl

  def visit1StateDecl(self, statedecl:ASTStateDecl):
    d = self.state_cache[statedecl.name]
    mf2 = d.get(None, None)
    if mf2 is not None :
      raise StateAlreadyDefined(mf2)
    d[statedecl.signature] = State(
      statedecl.name,
      None,
      [], None, None
    ), statedecl

  def visitInitial(self, initial:ASTInitial):
    self.init_ref = initial.initial
    
  def link_pass(self):
    if self.init_ref :
      self.init_state, init_decl = self.resolveState(self.init_ref)
    else :
      if not self.states :
        raise NoInitialState()
      init_decl = self.states[-1]
      self.init_state, _ = self.state_cache[init_decl.name][init_decl.signature]
    self.visitState(self.init_state, init_decl)

  def visitState(self, state:State, decl:ASTStateDecl|ASTMFunctionDecl):
    if self.is_referenced(decl) :
      return
    self.reference(decl)
    for r in decl.rules : # type: ASTAbstractRule
      self.visitRule(state, r)

  def resolveState(self, ref:ASTAbstractStateReference):
    try :
      state, decl = self.state_cache[ref.name][ref.signature]
    except :
      raise stateNotDefined(ref)
    if isinstance(ref, ASTStateReference) :
      self.visitState(state, decl)
      return state, decl
    elif isinstance(ref, ASTMFunctionReference) :
      for a in ref.args :
        if isinstance(a, ASTAbstractStateReference) :
          self.resolveState(a)
        elif isinstance(a, ASTSymbol) :
          if not a.is_generic :
            self.symbol_cache.add(a)
        else :
          raise UnknownArgumentType(a)
      return state, decl
    else :
      raise UnknownStateReferenceType(ref)

  def visitRule(self, state:State, rule_decl:ASTRule):
    if not isinstance(rule_decl, ASTRule) :
      raise UnknownRuleType()
    symb = rule_decl.symbol
    name = symb.name
    if symb.is_generic and symb.name not in state.args:
      if state.default_rule is not None :
        raise MultipleDefaultRules(state)
      final_state, _ = self.resolveState(rule_decl.final_state)
      actions = [ self.visitAction(a) for a in rule_decl.actions ]
      state.default_rule = DynRule(actions, final_state)
      state.default_symbol_name = name
      return
    if name is not None :
      self.symbol_cache.add(name)
    final_state, _ = self.resolveState(rule_decl.final_state)
    actions = [ self.visitAction(a) for a in rule_decl.actions ]
    state.rules[name] = DynRule(actions, final_state)

  def visitAction(self, act:ASTAbstractAction):
    if isinstance(act, ASTActionLeft) :
      return Action.LEFT
    elif isinstance(act, ASTActionRight) :
      return Action.RIGHT
    elif isinstance(act, ASTActionPrint) :
      if act.symbol.is_generic() :
        return DynPrint(act.symbol.name)
      else :
        return ActionPrint(act.symbol.name)
    else :
      raise UnknownActionType()

  def create_machine(self):
    return AMachine(
      symbols=sorted(self.symbol_cache),
      states=sorted(
        (
          self.state_cache[name][signature][0]
          for name, s in self.referenced_states.items() for signature in s
        ), key=lambda s: (not s.args, s.name, len(s.args))
      ),
      init_state=self.init_state
    )

