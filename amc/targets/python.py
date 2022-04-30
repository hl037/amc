"""
Pour python, on serialize l'IR, et celle-ci est interprétée
"""

import typing as th
from ..ir import *


class PythonTarget(object):
  """
  Compile the ir to python
  """
  def __init__(self):
    self.amachine = None #type: AMachine
    self.states = None # type: list[State]
    self.state_index = {} # type: dict[State, int]
  
  def dump(self, amachine:AMachine, f:th.IO, name):
    self.amachine = amachine
    pp = PrettyPrinter(f)
    pp.write('''
from amc.ir import *
from amc.runtime import *

''')
    self.states = []
    self.state_index = {}
    self.decl_pass()
    self.dump_pass(pp)
    self.dump_symbols(pp)
    self.dump_init_state(pp)
    pp.write(f'''
machine = AMachine(symbols, states, init_state)

cli = CLI(machine)
cli.entry_point({repr(name)})
''')

  def dump_symbols(self, pp:PrettyPrinter):
    pp.write('symbols = [')
    pp.nl()
    for s in self.amachine.symbols :
      pp.write(repr(s))
      pp.write(',')
      pp.nl()
    pp<<1
    pp.write(']')
    pp.nl()
    pp.nl()

  def dump_init_state(self, pp:PrettyPrinter):
    pp.write('init_state = ')
    self.dump_stateref(pp, self.amachine.init_state)

  def decl_pass(self):
    self.visitStateRef(self.amachine.init_state)

  def visitState(self, state:State):
    if state in self.state_index or state is State.ACCEPT or state is State.REJECT:
      return
    i = len(self.states)
    self.states.append(state)
    self.state_index[state] = i
    for r in state.rules.values() :
      self.visitStateRef(r.finalState)
    if state.default_rule :
      self.visitStateRef(state.default_rule.finalState)

  def visitStateRef(self, rs:StateReference):
    if isinstance(rs, StatePlaceholder) :
      return
    elif isinstance(rs, StateReference) :
      self.visitState(rs.state)
      for a in rs.args :
        if isinstance(a, StateReference) :
          self.visitStateRef(a)
    else :
      raise RuntimeError('Unknown StateReference type')

  def dump_pass(self, pp:PrettyPrinter):
    self.dump_states(pp)
    self.dump_rules(pp)

  def dump_states(self, pp:PrettyPrinter):
    pp.write('states = [')
    pp.nl()
    pp>>1
    for s in self.states :
      self.dump_state(pp, s)
      pp.write(',')
      pp.nl()
    pp<<1
    pp.write(']')
    pp.nl()
    pp.nl()
  

  def dump_state(self, pp:PrettyPrinter, s:State):
    pp.write(f'State({repr(s.name)}, {repr(s.args)}, {{}}, {repr(s.default_symbol_name)}, None)')

  def target_state(self, s:State):
    if s is State.ACCEPT :
      return 'State.ACCEPT'
    elif s is State.REJECT :
      return 'State.REJECT'
    else :
      return f'states[{self.state_index[s]}]'
      

  def dump_rules(self, pp:PrettyPrinter):
    for s in self.states :
      pp.write(f'{self.target_state(s)}.rules = {{')
      pp.nl()
      pp>>1
      for symb, r in s.rules.items() :
        pp.write(f'{repr(symb)} : ')
        self.dump_rule(pp, r)
        pp.write(',')
        pp.nl()
      pp<<1
      pp.write('}')
      pp.nl()
      if s.default_rule :
        pp.write(f'{self.target_state(s)}.default_rule = ')
        self.dump_rule(pp, s.default_rule)
      pp.nl()
      pp.nl()

  
  def dump_rule(self, pp:PrettyPrinter, r:DynRule):
    pp.write('DynRule(')
    self.dump_actions(pp, r.actions)
    pp.write(',')
    self.dump_stateref(pp, r.finalState)
    pp.write(')')

  def dump_actions(self, pp:PrettyPrinter, acts:list[Action]):
    pp.write('[')
    for a in acts :
      self.dump_action(pp, a)
      pp.write(',')
    pp.write(']')
  
  def dump_action(self, pp:PrettyPrinter, a:Action):
    if a is Action.LEFT :
      pp.write('Action.LEFT')
    elif a is Action.RIGHT :
      pp.write('Action.RIGHT')
    elif isinstance(a, ActionPrint) :
      pp.write(f'ActionPrint({repr(a.symbol)})')
    elif isinstance(a, DynPrint) :
      pp.write(f'DynPrint({repr(a.dyn_symbol)})')
    else :
      raise RuntimeError('Unknown Action type')

  def dump_stateref(self, pp:PrettyPrinter, sr:StateReference):
    if isinstance(sr, StatePlaceholder) :
      pp.write(f'StatePlaceholder({repr(sr.ph_name)})')
    elif isinstance(sr, StaticStateReference) :
      pp.write(f'StaticStateReference({self.target_state(sr.state)}, ')
      if not sr.args :
        pp.write('tuple()')
      else :
        pp.write('(')
        for a in sr.args :
          if isinstance(a, str) :
            pp.write(repr(a))
          else :
            self.dump_stateref(pp, a)
          pp.write(',')
        pp.write(')')
      pp.write(')')
    else :
      raise RuntimeError('Unknown StateReference type')
        
    

    
