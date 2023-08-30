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


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_mem.
    def visitClass_mem(self, ctx:BKOOLParser.Class_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_mem_list.
    def visitClass_mem_list(self, ctx:BKOOLParser.Class_mem_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_mem_decl.
    def visitClass_mem_decl(self, ctx:BKOOLParser.Class_mem_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attr_decl.
    def visitAttr_decl(self, ctx:BKOOLParser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#const_attr_decl.
    def visitConst_attr_decl(self, ctx:BKOOLParser.Const_attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#static_attr_decl.
    def visitStatic_attr_decl(self, ctx:BKOOLParser.Static_attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#static_const_attr_decl.
    def visitStatic_const_attr_decl(self, ctx:BKOOLParser.Static_const_attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attr_decl_list.
    def visitAttr_decl_list(self, ctx:BKOOLParser.Attr_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attr_decl_unit.
    def visitAttr_decl_unit(self, ctx:BKOOLParser.Attr_decl_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_list.
    def visitParam_list(self, ctx:BKOOLParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_decl.
    def visitParam_decl(self, ctx:BKOOLParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor_decl.
    def visitConstructor_decl(self, ctx:BKOOLParser.Constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl_type.
    def visitDecl_type(self, ctx:BKOOLParser.Decl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_var_decls.
    def visitLocal_var_decls(self, ctx:BKOOLParser.Local_var_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#local_var_decl.
    def visitLocal_var_decl(self, ctx:BKOOLParser.Local_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#const_decl.
    def visitConst_decl(self, ctx:BKOOLParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl_list.
    def visitDecl_list(self, ctx:BKOOLParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl_unit.
    def visitDecl_unit(self, ctx:BKOOLParser.Decl_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmts.
    def visitStmts(self, ctx:BKOOLParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs_unit.
    def visitLhs_unit(self, ctx:BKOOLParser.Lhs_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs_member_access_expr.
    def visitLhs_member_access_expr(self, ctx:BKOOLParser.Lhs_member_access_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs_index_expr.
    def visitLhs_index_expr(self, ctx:BKOOLParser.Lhs_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_then_else_stmt.
    def visitIf_then_else_stmt(self, ctx:BKOOLParser.If_then_else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_then_stmt.
    def visitIf_then_stmt(self, ctx:BKOOLParser.If_then_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invocation_stmt.
    def visitMethod_invocation_stmt(self, ctx:BKOOLParser.Method_invocation_stmtContext):
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


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr12.
    def visitExpr12(self, ctx:BKOOLParser.Expr12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_call.
    def visitMethod_call(self, ctx:BKOOLParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx:BKOOLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrlit.
    def visitArrlit(self, ctx:BKOOLParser.ArrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal_list.
    def visitLiteral_list(self, ctx:BKOOLParser.Literal_listContext):
        return self.visitChildren(ctx)



del BKOOLParser