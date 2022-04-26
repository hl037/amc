
grammar amachine;

body : (stmt | NL+)*;

stmt
  : include
  | symbols
  | initial
  | m_function_decl
  | state_decl
  ;

include
  : INCLUDE NL+
  ;

symbols
  : SYMBOLS (NL+ WS symbol_decl)* NL+
  ;

symbol_decl
  : SYMBOL_NAME
  ;

initial
  : INIT NL+ WS state NL+
  ;

m_function_decl
  : STATE_NAME '(' WS? t_decl WS? (',' WS? t_decl WS?)* ')' state_rules NL+
  ;

t_decl
  : T_STATE_NAME
  | T_SYMBOL_NAME
  ;

state_decl
  : STATE_NAME state_rules NL+
  ;

state_rules
  : (NL+ WS state_rule)+
  ;

state_rule
  : state_rule_symbol state_rule_actions state
  ;

state_rule_symbol
  : ((DEFAULT | T_SYMBOL_NAME | SYMBOL_NAME) WS)?
  ;

state_rule_actions
  : state_rule_action*
  ;

state_rule_action
  : LEFT WS
  | RIGHT WS
  | PRINT symbol? WS
  ;

name
  : symbol
  | state
  ;

state
  : m_function
  | T_STATE_NAME
  | STATE_NAME
  ;

m_function
  : (T_STATE_NAME | STATE_NAME) '(' WS? name WS? (',' WS? name WS?)* ')'
  ;

symbol
  : T_SYMBOL_NAME
  | SYMBOL_NAME
  ;





COMMENT : WS* '#(' (~[\n])* -> skip;
INIT : 'init';
INCLUDE : 'include(' (~')')+ ')';
SYMBOLS : 'symbols';

DEFAULT : '...';

PRINT : 'P:' ;
LEFT : '<-' ;
RIGHT : '->' ;

T_STATE_NAME : '_' STATE_NAME;

STATE_NAME : [A-Z] (~[ \t\n():,])*;

T_SYMBOL_NAME : '_' SYMBOL_NAME;

SYMBOL_NAME : ('\\(' | '\\)' | '\\\\' | ~[ \t\nA-Z_()] )('\\(' | '\\)' | '\\\\' | ~[ \t\n(),] )* ; // Tous les symboles sauf ceux qui peuvent poser problème (les parenthèse sont échappée)


NL : (WS? '\n')+;
WS : [ \t]+;

