import click
from functools import reduce

from .ir import *

class StopMachine(Exception):
  pass


class Interpreter(object):
  """
  Interpreteur de machine de turing
  """
  ACCEPT = 1
  REJECT = 0
  STOPPED = -1
  def __init__(self, machine: AMachine, tape:list[str], initpos=0):
    self.head = initpos
    self.tape = tape
    self.previous_state = None
    self.state = machine.init_state.instanciate()
    self.print_cb = None
    self.action_cb = None
    self.state_cb = None
    self.cur_act = None
    self.keep_unused_tape = False
    if self.head < 0 :
      self.tape[:0] = [''] * (-self.head)
      self.head = 0
    if len(self.tape) <= self.head :
      self.tape[len(self.tape):] = [''] * (self.head - len(self.tape) + 1)
      

  def read_tape(self):
    if self.head < 0 or self.head >= len(self.tape) :
      return None
    return self.tape[self.head]

  def write_tape(self, symbol:str):
    self.tape[self.head] = symbol

  def perform_actions(self, actions:list[Action]):
    for a in actions :
      self.cur_act = a
      if a == Action.LEFT :
        if not self.keep_unused_tape and self.head == len(self.tape) -1 and not self.tape[-1]:
          del self.tape[-1]
        self.head -= 1
        if self.head < 0 :
          self.tape[:0] = [''] * (-self.head)
          self.head = 0
      elif a == Action.RIGHT :
        if not self.keep_unused_tape and self.head == 0 and not self.tape[0]:
          del self.tape[0]
        else :
          self.head += 1
        if len(self.tape) <= self.head :
          self.tape[len(self.tape):] = [''] * (self.head - len(self.tape) + 1)
      else :
        assert isinstance(a, ActionPrint)
        self.write_tape(a.symbol)
        if self.print_cb:
          self.print_cb(self)
      if self.action_cb:
        self.action_cb(self)

  def execute(self):
    try:
      self.previous_state = None
      while True :
        if self.state is State.ACCEPT:
          return self.ACCEPT
        elif self.state is State.REJECT :
          return self.REJECT
        r = self.state.instanciate_rule(self.read_tape())
        self.perform_actions(r.actions)
        self.previous_state = self.state
        self.state = r.finalState.instanciate()
        if self.state_cb :
          self.state_cb(self)
    except StopMachine:
      return self.STOPPED


class CLI(object):
  """
  Interface ligne de commande pour l'interpréteur
  """
  def __init__(self, machine:AMachine):
    self.machine = machine
    self.before = 10
    self.after = 10

  @staticmethod
  def decorator(f):
    return reduce(lambda x, y: y(x), reversed((
      click.option('--keep-tape', '-k', is_flag=True, help='Keep unused tape (permits to watch the space usage of the machine)'),
      click.option('--print-print', '-p', is_flag=True, help='Print state on print action'),
      click.option('--print-action', '-a', is_flag=True, help='Print state on any action'),
      click.option('--print-state', '-t', is_flag=True, help='Print state on state end'),
      click.option('--halt-print', is_flag=True, help='Halt on prints'),
      click.option('--halt-action', is_flag=True, help='Halt on any action'),
      click.option('--halt-state', is_flag=True, help='Halt on state end'),
      click.option('--file-tape', '-f', help='The tape is imported from a space-separated file'),
      click.option('--string-tape', '-s', default=None, help='The tape is imported from a space separated string passed as argument'),
      click.option('--file-chars-tape', '-i', default=None, help='The tape is imported from a file split by chars'),
      click.option('--chars-tape', '-c', default=None, help='The tape is imported from an argument string split by chars'),
      click.option('--before', type=int, help='cell count to display before current position', default=50),
      click.option('--after', type=int, help='cell count to display after current position', default=50),
      f
    )))

  def print_machine(self, interp:Interpreter, halt, reason=None):
    print(reason)
    pos = interp.head
    start = pos - self.before
    if start < 0:
      start = None
    end = min(len(interp.tape), pos+self.after)
    printed = [ s if s else ' ' for s in interp.tape[start:end] ]
    before_count = min(pos, self.before)
    sizes = [len(s)+1 for s in printed]
    print(f'[{pos-before_count}]')
    print('|'.join(printed))
    print((' ' * sum( s for s in sizes[:before_count] ) + '^' * (sizes[before_count] - 1)))
    print(f'[...{len(interp.tape) - end} more]')
    print(f'STATE : {interp.state.name}')
    a = interp.cur_act
    if a is None :
      pass
    elif a == Action.LEFT :
      print('ACTION : <-')
    elif a == Action.RIGHT :
      print('ACTION : ->')
    else :
      print(f'ACTION : print({a.symbol})')
    print()
    if halt :
      try :
        input()
      except KeyboardInterrupt as e:
        raise StopMachine() from e
      

  def main(self,
    keep_tape,
    print_print,
    print_action,
    print_state,
    halt_print,
    halt_action,
    halt_state,
    file_tape,
    string_tape,
    file_chars_tape,
    chars_tape,
    before,
    after,
  ):
    self.before = before
    self.after = after
    if file_tape is not None :
      with open(file_tape, 'r') as f :
        tape = f.read().split()
    elif string_tape is not None :
      tape = string_tape.split()
    elif file_chars_tape is not None :
      with open(file_chars_tape, 'r') as f :
        tape = list(f.read())
    elif chars_tape is not None :
      tape = list(chars_tape)
    else :
      raise RuntimeError('No tape provided')
    i = Interpreter(self.machine, tape)
    if print_print :
      i.print_cb = lambda i: self.print_machine(i, halt_print, 'PRINT')
    if print_action :
      i.action_cb = lambda i: self.print_machine(i, halt_action, 'ACTION')
    if print_state :
      i.state_cb = lambda i: self.print_machine(i, halt_state, 'STATE')
    i.keep_unused_tape = keep_tape
    res = i.execute()
    print()
    if res == Interpreter.ACCEPT :
      print('ACCEPTED !')
    elif res == Interpreter.REJECT :
      print('REJECTED !')
      if i.previous_state :
        print(f'Rejected at state : {i.previous_state.name}')
    elif res == Interpreter.STOPPED :
      print('STOPPED')
    else:
      print(f'ENDED with result {res}')
    print(f'STATE : {i.state.name}')
    print('|'.join(s if s else '' for s in i.tape))

  def entry_point(self, name):
    @click.command(name=name)
    @self.decorator
    def f(*args, **kwargs):
      self.main(*args, **kwargs)
    f()
    
