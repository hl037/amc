# Generated from amachine.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,4,0,39,8,0,11,0,
        12,0,40,5,0,43,8,0,10,0,12,0,46,9,0,1,1,1,1,1,1,1,1,1,1,3,1,53,8,
        1,1,2,1,2,4,2,57,8,2,11,2,12,2,58,1,3,1,3,4,3,63,8,3,11,3,12,3,64,
        1,3,1,3,5,3,69,8,3,10,3,12,3,72,9,3,1,3,4,3,75,8,3,11,3,12,3,76,
        1,4,1,4,1,5,1,5,4,5,83,8,5,11,5,12,5,84,1,5,1,5,1,5,4,5,90,8,5,11,
        5,12,5,91,1,6,1,6,1,6,3,6,97,8,6,1,6,1,6,3,6,101,8,6,1,6,1,6,3,6,
        105,8,6,1,6,1,6,3,6,109,8,6,5,6,111,8,6,10,6,12,6,114,9,6,1,6,1,
        6,1,6,4,6,119,8,6,11,6,12,6,120,1,7,1,7,1,8,1,8,1,8,4,8,128,8,8,
        11,8,12,8,129,1,9,4,9,133,8,9,11,9,12,9,134,1,9,1,9,4,9,139,8,9,
        11,9,12,9,140,1,10,1,10,1,10,1,10,1,11,1,11,3,11,149,8,11,1,12,5,
        12,152,8,12,10,12,12,12,155,9,12,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,163,8,13,1,13,3,13,166,8,13,1,14,1,14,3,14,170,8,14,1,15,1,15,
        1,15,3,15,175,8,15,1,16,1,16,1,16,3,16,180,8,16,1,16,1,16,3,16,184,
        8,16,1,16,1,16,3,16,188,8,16,1,16,1,16,3,16,192,8,16,5,16,194,8,
        16,10,16,12,16,197,9,16,1,16,1,16,1,17,1,17,1,17,0,0,18,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,3,2,0,12,12,14,14,2,0,
        8,8,14,15,1,0,14,15,219,0,44,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,
        60,1,0,0,0,8,78,1,0,0,0,10,80,1,0,0,0,12,93,1,0,0,0,14,122,1,0,0,
        0,16,124,1,0,0,0,18,138,1,0,0,0,20,142,1,0,0,0,22,148,1,0,0,0,24,
        153,1,0,0,0,26,165,1,0,0,0,28,169,1,0,0,0,30,174,1,0,0,0,32,176,
        1,0,0,0,34,200,1,0,0,0,36,43,3,2,1,0,37,39,5,16,0,0,38,37,1,0,0,
        0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,36,
        1,0,0,0,42,38,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,1,1,0,0,0,46,44,1,0,0,0,47,53,3,4,2,0,48,53,3,6,3,0,49,53,3,10,
        5,0,50,53,3,12,6,0,51,53,3,16,8,0,52,47,1,0,0,0,52,48,1,0,0,0,52,
        49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,3,1,0,0,0,54,56,5,6,0,
        0,55,57,5,16,0,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,0,58,59,
        1,0,0,0,59,5,1,0,0,0,60,70,5,7,0,0,61,63,5,16,0,0,62,61,1,0,0,0,
        63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,5,
        17,0,0,67,69,3,8,4,0,68,62,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,
        71,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,73,75,5,16,0,0,74,73,1,0,
        0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,7,1,0,0,0,78,79,
        5,15,0,0,79,9,1,0,0,0,80,82,5,5,0,0,81,83,5,16,0,0,82,81,1,0,0,0,
        83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,
        17,0,0,87,89,3,30,15,0,88,90,5,16,0,0,89,88,1,0,0,0,90,91,1,0,0,
        0,91,89,1,0,0,0,91,92,1,0,0,0,92,11,1,0,0,0,93,94,5,13,0,0,94,96,
        5,1,0,0,95,97,5,17,0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,
        98,100,3,14,7,0,99,101,5,17,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,
        112,1,0,0,0,102,104,5,2,0,0,103,105,5,17,0,0,104,103,1,0,0,0,104,
        105,1,0,0,0,105,106,1,0,0,0,106,108,3,14,7,0,107,109,5,17,0,0,108,
        107,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,102,1,0,0,0,111,
        114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,
        112,1,0,0,0,115,116,5,3,0,0,116,118,3,18,9,0,117,119,5,16,0,0,118,
        117,1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,
        13,1,0,0,0,122,123,7,0,0,0,123,15,1,0,0,0,124,125,5,13,0,0,125,127,
        3,18,9,0,126,128,5,16,0,0,127,126,1,0,0,0,128,129,1,0,0,0,129,127,
        1,0,0,0,129,130,1,0,0,0,130,17,1,0,0,0,131,133,5,16,0,0,132,131,
        1,0,0,0,133,134,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,136,
        1,0,0,0,136,137,5,17,0,0,137,139,3,20,10,0,138,132,1,0,0,0,139,140,
        1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,19,1,0,0,0,142,143,3,
        22,11,0,143,144,3,24,12,0,144,145,3,30,15,0,145,21,1,0,0,0,146,147,
        7,1,0,0,147,149,5,17,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,23,
        1,0,0,0,150,152,3,26,13,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,
        1,0,0,0,153,154,1,0,0,0,154,25,1,0,0,0,155,153,1,0,0,0,156,157,5,
        10,0,0,157,166,5,17,0,0,158,159,5,11,0,0,159,166,5,17,0,0,160,162,
        5,9,0,0,161,163,3,34,17,0,162,161,1,0,0,0,162,163,1,0,0,0,163,164,
        1,0,0,0,164,166,5,17,0,0,165,156,1,0,0,0,165,158,1,0,0,0,165,160,
        1,0,0,0,166,27,1,0,0,0,167,170,3,34,17,0,168,170,3,30,15,0,169,167,
        1,0,0,0,169,168,1,0,0,0,170,29,1,0,0,0,171,175,3,32,16,0,172,175,
        5,12,0,0,173,175,5,13,0,0,174,171,1,0,0,0,174,172,1,0,0,0,174,173,
        1,0,0,0,175,31,1,0,0,0,176,177,5,13,0,0,177,179,5,1,0,0,178,180,
        5,17,0,0,179,178,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,183,
        3,28,14,0,182,184,5,17,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,195,
        1,0,0,0,185,187,5,2,0,0,186,188,5,17,0,0,187,186,1,0,0,0,187,188,
        1,0,0,0,188,189,1,0,0,0,189,191,3,28,14,0,190,192,5,17,0,0,191,190,
        1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,185,1,0,0,0,194,197,
        1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,195,
        1,0,0,0,198,199,5,3,0,0,199,33,1,0,0,0,200,201,7,2,0,0,201,35,1,
        0,0,0,30,40,42,44,52,58,64,70,76,84,91,96,100,104,108,112,120,129,
        134,140,148,153,162,165,169,174,179,183,187,191,195
    ]

class amachineParser ( Parser ):

    grammarFileName = "amachine.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "<INVALID>", "'init'", 
                     "<INVALID>", "'symbols'", "'...'", "'P:'", "'<-'", 
                     "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "COMMENT", "INIT", "INCLUDE", "SYMBOLS", "DEFAULT", 
                      "PRINT", "LEFT", "RIGHT", "T_STATE_NAME", "STATE_NAME", 
                      "T_SYMBOL_NAME", "SYMBOL_NAME", "NL", "WS" ]

    RULE_body = 0
    RULE_stmt = 1
    RULE_include = 2
    RULE_symbols = 3
    RULE_symbol_decl = 4
    RULE_initial = 5
    RULE_m_function_decl = 6
    RULE_t_decl = 7
    RULE_am_state_decl = 8
    RULE_am_state_rules = 9
    RULE_am_state_rule = 10
    RULE_am_state_rule_symbol = 11
    RULE_am_state_rule_actions = 12
    RULE_am_state_rule_action = 13
    RULE_name = 14
    RULE_am_state = 15
    RULE_m_function = 16
    RULE_symbol = 17

    ruleNames =  [ "body", "stmt", "include", "symbols", "symbol_decl", 
                   "initial", "m_function_decl", "t_decl", "am_state_decl", 
                   "am_state_rules", "am_state_rule", "am_state_rule_symbol", 
                   "am_state_rule_actions", "am_state_rule_action", "name", 
                   "am_state", "m_function", "symbol" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    COMMENT=4
    INIT=5
    INCLUDE=6
    SYMBOLS=7
    DEFAULT=8
    PRINT=9
    LEFT=10
    RIGHT=11
    T_STATE_NAME=12
    STATE_NAME=13
    T_SYMBOL_NAME=14
    SYMBOL_NAME=15
    NL=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amachineParser.StmtContext)
            else:
                return self.getTypedRuleContext(amachineParser.StmtContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.NL)
            else:
                return self.getToken(amachineParser.NL, i)

        def getRuleIndex(self):
            return amachineParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = amachineParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << amachineParser.INIT) | (1 << amachineParser.INCLUDE) | (1 << amachineParser.SYMBOLS) | (1 << amachineParser.STATE_NAME) | (1 << amachineParser.NL))) != 0):
                self.state = 42
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [amachineParser.INIT, amachineParser.INCLUDE, amachineParser.SYMBOLS, amachineParser.STATE_NAME]:
                    self.state = 36
                    self.stmt()
                    pass
                elif token in [amachineParser.NL]:
                    self.state = 38 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 37
                            self.match(amachineParser.NL)

                        else:
                            raise NoViableAltException(self)
                        self.state = 40 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include(self):
            return self.getTypedRuleContext(amachineParser.IncludeContext,0)


        def symbols(self):
            return self.getTypedRuleContext(amachineParser.SymbolsContext,0)


        def initial(self):
            return self.getTypedRuleContext(amachineParser.InitialContext,0)


        def m_function_decl(self):
            return self.getTypedRuleContext(amachineParser.M_function_declContext,0)


        def am_state_decl(self):
            return self.getTypedRuleContext(amachineParser.Am_state_declContext,0)


        def getRuleIndex(self):
            return amachineParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = amachineParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.include()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.symbols()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.initial()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.m_function_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.am_state_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(amachineParser.INCLUDE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.NL)
            else:
                return self.getToken(amachineParser.NL, i)

        def getRuleIndex(self):
            return amachineParser.RULE_include

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude" ):
                return visitor.visitInclude(self)
            else:
                return visitor.visitChildren(self)




    def include(self):

        localctx = amachineParser.IncludeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(amachineParser.INCLUDE)
            self.state = 56 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 55
                    self.match(amachineParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 58 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOLS(self):
            return self.getToken(amachineParser.SYMBOLS, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.WS)
            else:
                return self.getToken(amachineParser.WS, i)

        def symbol_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amachineParser.Symbol_declContext)
            else:
                return self.getTypedRuleContext(amachineParser.Symbol_declContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.NL)
            else:
                return self.getToken(amachineParser.NL, i)

        def getRuleIndex(self):
            return amachineParser.RULE_symbols

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbols" ):
                return visitor.visitSymbols(self)
            else:
                return visitor.visitChildren(self)




    def symbols(self):

        localctx = amachineParser.SymbolsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_symbols)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(amachineParser.SYMBOLS)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 61
                        self.match(amachineParser.NL)
                        self.state = 64 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==amachineParser.NL):
                            break

                    self.state = 66
                    self.match(amachineParser.WS)
                    self.state = 67
                    self.symbol_decl() 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 74 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 73
                    self.match(amachineParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 76 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Symbol_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL_NAME(self):
            return self.getToken(amachineParser.SYMBOL_NAME, 0)

        def getRuleIndex(self):
            return amachineParser.RULE_symbol_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol_decl" ):
                return visitor.visitSymbol_decl(self)
            else:
                return visitor.visitChildren(self)




    def symbol_decl(self):

        localctx = amachineParser.Symbol_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_symbol_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(amachineParser.SYMBOL_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INIT(self):
            return self.getToken(amachineParser.INIT, 0)

        def WS(self):
            return self.getToken(amachineParser.WS, 0)

        def am_state(self):
            return self.getTypedRuleContext(amachineParser.Am_stateContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.NL)
            else:
                return self.getToken(amachineParser.NL, i)

        def getRuleIndex(self):
            return amachineParser.RULE_initial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitial" ):
                return visitor.visitInitial(self)
            else:
                return visitor.visitChildren(self)




    def initial(self):

        localctx = amachineParser.InitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initial)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(amachineParser.INIT)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.match(amachineParser.NL)
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==amachineParser.NL):
                    break

            self.state = 86
            self.match(amachineParser.WS)
            self.state = 87
            self.am_state()
            self.state = 89 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 88
                    self.match(amachineParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 91 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class M_function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE_NAME(self):
            return self.getToken(amachineParser.STATE_NAME, 0)

        def t_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amachineParser.T_declContext)
            else:
                return self.getTypedRuleContext(amachineParser.T_declContext,i)


        def am_state_rules(self):
            return self.getTypedRuleContext(amachineParser.Am_state_rulesContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.WS)
            else:
                return self.getToken(amachineParser.WS, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.NL)
            else:
                return self.getToken(amachineParser.NL, i)

        def getRuleIndex(self):
            return amachineParser.RULE_m_function_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitM_function_decl" ):
                return visitor.visitM_function_decl(self)
            else:
                return visitor.visitChildren(self)




    def m_function_decl(self):

        localctx = amachineParser.M_function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_m_function_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(amachineParser.STATE_NAME)
            self.state = 94
            self.match(amachineParser.T__0)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==amachineParser.WS:
                self.state = 95
                self.match(amachineParser.WS)


            self.state = 98
            self.t_decl()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==amachineParser.WS:
                self.state = 99
                self.match(amachineParser.WS)


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==amachineParser.T__1:
                self.state = 102
                self.match(amachineParser.T__1)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==amachineParser.WS:
                    self.state = 103
                    self.match(amachineParser.WS)


                self.state = 106
                self.t_decl()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==amachineParser.WS:
                    self.state = 107
                    self.match(amachineParser.WS)


                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(amachineParser.T__2)
            self.state = 116
            self.am_state_rules()
            self.state = 118 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 117
                    self.match(amachineParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 120 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_STATE_NAME(self):
            return self.getToken(amachineParser.T_STATE_NAME, 0)

        def T_SYMBOL_NAME(self):
            return self.getToken(amachineParser.T_SYMBOL_NAME, 0)

        def getRuleIndex(self):
            return amachineParser.RULE_t_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_decl" ):
                return visitor.visitT_decl(self)
            else:
                return visitor.visitChildren(self)




    def t_decl(self):

        localctx = amachineParser.T_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_t_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not(_la==amachineParser.T_STATE_NAME or _la==amachineParser.T_SYMBOL_NAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Am_state_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE_NAME(self):
            return self.getToken(amachineParser.STATE_NAME, 0)

        def am_state_rules(self):
            return self.getTypedRuleContext(amachineParser.Am_state_rulesContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.NL)
            else:
                return self.getToken(amachineParser.NL, i)

        def getRuleIndex(self):
            return amachineParser.RULE_am_state_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAm_state_decl" ):
                return visitor.visitAm_state_decl(self)
            else:
                return visitor.visitChildren(self)




    def am_state_decl(self):

        localctx = amachineParser.Am_state_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_am_state_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(amachineParser.STATE_NAME)
            self.state = 125
            self.am_state_rules()
            self.state = 127 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 126
                    self.match(amachineParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 129 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Am_state_rulesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.WS)
            else:
                return self.getToken(amachineParser.WS, i)

        def am_state_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amachineParser.Am_state_ruleContext)
            else:
                return self.getTypedRuleContext(amachineParser.Am_state_ruleContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.NL)
            else:
                return self.getToken(amachineParser.NL, i)

        def getRuleIndex(self):
            return amachineParser.RULE_am_state_rules

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAm_state_rules" ):
                return visitor.visitAm_state_rules(self)
            else:
                return visitor.visitChildren(self)




    def am_state_rules(self):

        localctx = amachineParser.Am_state_rulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_am_state_rules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 132 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 131
                        self.match(amachineParser.NL)
                        self.state = 134 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==amachineParser.NL):
                            break

                    self.state = 136
                    self.match(amachineParser.WS)
                    self.state = 137
                    self.am_state_rule()

                else:
                    raise NoViableAltException(self)
                self.state = 140 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Am_state_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def am_state_rule_symbol(self):
            return self.getTypedRuleContext(amachineParser.Am_state_rule_symbolContext,0)


        def am_state_rule_actions(self):
            return self.getTypedRuleContext(amachineParser.Am_state_rule_actionsContext,0)


        def am_state(self):
            return self.getTypedRuleContext(amachineParser.Am_stateContext,0)


        def getRuleIndex(self):
            return amachineParser.RULE_am_state_rule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAm_state_rule" ):
                return visitor.visitAm_state_rule(self)
            else:
                return visitor.visitChildren(self)




    def am_state_rule(self):

        localctx = amachineParser.Am_state_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_am_state_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.am_state_rule_symbol()
            self.state = 143
            self.am_state_rule_actions()
            self.state = 144
            self.am_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Am_state_rule_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(amachineParser.WS, 0)

        def DEFAULT(self):
            return self.getToken(amachineParser.DEFAULT, 0)

        def T_SYMBOL_NAME(self):
            return self.getToken(amachineParser.T_SYMBOL_NAME, 0)

        def SYMBOL_NAME(self):
            return self.getToken(amachineParser.SYMBOL_NAME, 0)

        def getRuleIndex(self):
            return amachineParser.RULE_am_state_rule_symbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAm_state_rule_symbol" ):
                return visitor.visitAm_state_rule_symbol(self)
            else:
                return visitor.visitChildren(self)




    def am_state_rule_symbol(self):

        localctx = amachineParser.Am_state_rule_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_am_state_rule_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << amachineParser.DEFAULT) | (1 << amachineParser.T_SYMBOL_NAME) | (1 << amachineParser.SYMBOL_NAME))) != 0):
                self.state = 146
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << amachineParser.DEFAULT) | (1 << amachineParser.T_SYMBOL_NAME) | (1 << amachineParser.SYMBOL_NAME))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self.match(amachineParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Am_state_rule_actionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def am_state_rule_action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amachineParser.Am_state_rule_actionContext)
            else:
                return self.getTypedRuleContext(amachineParser.Am_state_rule_actionContext,i)


        def getRuleIndex(self):
            return amachineParser.RULE_am_state_rule_actions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAm_state_rule_actions" ):
                return visitor.visitAm_state_rule_actions(self)
            else:
                return visitor.visitChildren(self)




    def am_state_rule_actions(self):

        localctx = amachineParser.Am_state_rule_actionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_am_state_rule_actions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << amachineParser.PRINT) | (1 << amachineParser.LEFT) | (1 << amachineParser.RIGHT))) != 0):
                self.state = 150
                self.am_state_rule_action()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Am_state_rule_actionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(amachineParser.LEFT, 0)

        def WS(self):
            return self.getToken(amachineParser.WS, 0)

        def RIGHT(self):
            return self.getToken(amachineParser.RIGHT, 0)

        def PRINT(self):
            return self.getToken(amachineParser.PRINT, 0)

        def symbol(self):
            return self.getTypedRuleContext(amachineParser.SymbolContext,0)


        def getRuleIndex(self):
            return amachineParser.RULE_am_state_rule_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAm_state_rule_action" ):
                return visitor.visitAm_state_rule_action(self)
            else:
                return visitor.visitChildren(self)




    def am_state_rule_action(self):

        localctx = amachineParser.Am_state_rule_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_am_state_rule_action)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [amachineParser.LEFT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(amachineParser.LEFT)
                self.state = 157
                self.match(amachineParser.WS)
                pass
            elif token in [amachineParser.RIGHT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(amachineParser.RIGHT)
                self.state = 159
                self.match(amachineParser.WS)
                pass
            elif token in [amachineParser.PRINT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(amachineParser.PRINT)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==amachineParser.T_SYMBOL_NAME or _la==amachineParser.SYMBOL_NAME:
                    self.state = 161
                    self.symbol()


                self.state = 164
                self.match(amachineParser.WS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self):
            return self.getTypedRuleContext(amachineParser.SymbolContext,0)


        def am_state(self):
            return self.getTypedRuleContext(amachineParser.Am_stateContext,0)


        def getRuleIndex(self):
            return amachineParser.RULE_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = amachineParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_name)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [amachineParser.T_SYMBOL_NAME, amachineParser.SYMBOL_NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.symbol()
                pass
            elif token in [amachineParser.T_STATE_NAME, amachineParser.STATE_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.am_state()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Am_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def m_function(self):
            return self.getTypedRuleContext(amachineParser.M_functionContext,0)


        def T_STATE_NAME(self):
            return self.getToken(amachineParser.T_STATE_NAME, 0)

        def STATE_NAME(self):
            return self.getToken(amachineParser.STATE_NAME, 0)

        def getRuleIndex(self):
            return amachineParser.RULE_am_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAm_state" ):
                return visitor.visitAm_state(self)
            else:
                return visitor.visitChildren(self)




    def am_state(self):

        localctx = amachineParser.Am_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_am_state)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.m_function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(amachineParser.T_STATE_NAME)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(amachineParser.STATE_NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class M_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE_NAME(self):
            return self.getToken(amachineParser.STATE_NAME, 0)

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amachineParser.NameContext)
            else:
                return self.getTypedRuleContext(amachineParser.NameContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(amachineParser.WS)
            else:
                return self.getToken(amachineParser.WS, i)

        def getRuleIndex(self):
            return amachineParser.RULE_m_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitM_function" ):
                return visitor.visitM_function(self)
            else:
                return visitor.visitChildren(self)




    def m_function(self):

        localctx = amachineParser.M_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_m_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(amachineParser.STATE_NAME)
            self.state = 177
            self.match(amachineParser.T__0)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==amachineParser.WS:
                self.state = 178
                self.match(amachineParser.WS)


            self.state = 181
            self.name()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==amachineParser.WS:
                self.state = 182
                self.match(amachineParser.WS)


            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==amachineParser.T__1:
                self.state = 185
                self.match(amachineParser.T__1)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==amachineParser.WS:
                    self.state = 186
                    self.match(amachineParser.WS)


                self.state = 189
                self.name()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==amachineParser.WS:
                    self.state = 190
                    self.match(amachineParser.WS)


                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            self.match(amachineParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_SYMBOL_NAME(self):
            return self.getToken(amachineParser.T_SYMBOL_NAME, 0)

        def SYMBOL_NAME(self):
            return self.getToken(amachineParser.SYMBOL_NAME, 0)

        def getRuleIndex(self):
            return amachineParser.RULE_symbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = amachineParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==amachineParser.T_SYMBOL_NAME or _la==amachineParser.SYMBOL_NAME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





