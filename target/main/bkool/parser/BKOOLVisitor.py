# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#not_void_type.
    def visitNot_void_type(self, ctx:BKOOLParser.Not_void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#void_type.
    def visitVoid_type(self, ctx:BKOOLParser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#prim_type.
    def visitPrim_type(self, ctx:BKOOLParser.Prim_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_type.
    def visitArr_type(self, ctx:BKOOLParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_lit.
    def visitBool_lit(self, ctx:BKOOLParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_lit.
    def visitArr_lit(self, ctx:BKOOLParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_decl.
    def visitArr_decl(self, ctx:BKOOLParser.Arr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_val.
    def visitArr_val(self, ctx:BKOOLParser.Arr_valContext):
        return self.visitChildren(ctx)



del BKOOLParser