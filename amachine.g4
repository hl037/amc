
grammar amachine;

body : (stmt | NL+)*;

stmt
  : include
  | symbols
  | initial
  | m_function_decl
  | am_state_decl
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
  : INIT NL+ WS am_state NL+
  ;

m_function_decl
  : STATE_NAME '(' WS? t_decl WS? (',' WS? t_decl WS?)* ')' am_state_rules NL+
  ;

t_decl
  : T_STATE_NAME
  | T_SYMBOL_NAME
  ;

am_state_decl
  : STATE_NAME am_state_rules NL+
  ;

am_state_rules
  : (NL+ WS am_state_rule)+
  ;

am_state_rule
  : am_state_rule_symbol am_state_rule_actions am_state
  ;

am_state_rule_symbol
  : ((DEFAULT | T_SYMBOL_NAME | SYMBOL_NAME) WS)?
  ;

am_state_rule_actions
  : am_state_rule_action*
  ;

am_state_rule_action
  : LEFT WS
  | RIGHT WS
  | PRINT symbol? WS
  ;

name
  : symbol
  | am_state
  ;

am_state
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





COMMENT : WS* '#)' (~[\n])* -> skip;
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

SYMBOL_NAME : '_' | ('\\(' | '\\)' | '\\\\' | ~[ \t\nA-Z_()] )('\\(' | '\\)' | '\\\\' | ~[ \t\n(),] )* ; // Tous les symboles sauf ceux qui peuvent poser problème (les parenthèse sont échappée)


NL : (WS? '\n')+;
WS : [ \t]+;

