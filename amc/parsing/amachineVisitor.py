# Generated from amachine.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .amachineParser import amachineParser
else:
    from amachineParser import amachineParser

# This class defines a complete generic visitor for a parse tree produced by amachineParser.

class amachineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by amachineParser#body.
    def visitBody(self, ctx:amachineParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#stmt.
    def visitStmt(self, ctx:amachineParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#include.
    def visitInclude(self, ctx:amachineParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#symbols.
    def visitSymbols(self, ctx:amachineParser.SymbolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#symbol_decl.
    def visitSymbol_decl(self, ctx:amachineParser.Symbol_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#initial.
    def visitInitial(self, ctx:amachineParser.InitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#m_function_decl.
    def visitM_function_decl(self, ctx:amachineParser.M_function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#t_decl.
    def visitT_decl(self, ctx:amachineParser.T_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#am_state_decl.
    def visitAm_state_decl(self, ctx:amachineParser.Am_state_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#am_state_rules.
    def visitAm_state_rules(self, ctx:amachineParser.Am_state_rulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#am_state_rule.
    def visitAm_state_rule(self, ctx:amachineParser.Am_state_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#am_state_rule_symbol.
    def visitAm_state_rule_symbol(self, ctx:amachineParser.Am_state_rule_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#am_state_rule_actions.
    def visitAm_state_rule_actions(self, ctx:amachineParser.Am_state_rule_actionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#am_state_rule_action.
    def visitAm_state_rule_action(self, ctx:amachineParser.Am_state_rule_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#name.
    def visitName(self, ctx:amachineParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#am_state.
    def visitAm_state(self, ctx:amachineParser.Am_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#m_function.
    def visitM_function(self, ctx:amachineParser.M_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by amachineParser#symbol.
    def visitSymbol(self, ctx:amachineParser.SymbolContext):
        return self.visitChildren(ctx)



del amachineParser