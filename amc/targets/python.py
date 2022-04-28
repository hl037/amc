"""
Pour python, on serialize l'IR, et celle-ci est interprétée
"""

import typing as th
from ..ir import *

import pickle

TEMPLATE0 = '''
import pickle
from runtime import Interpreter


machine = pickle.loads( '''

TEMPLATE1 = ''')

Interpreter.cli_main()
'''




class PythonTarget(object):
  """
  Compile the ir to python
  """
  
  def dump(self, amachine:AMachine, f:th.IO):
    f.write(TEMPLATE0)
    f.write(repr(pickle.dumps(amachine)))
    f.write(TEMPLATE1)
    
