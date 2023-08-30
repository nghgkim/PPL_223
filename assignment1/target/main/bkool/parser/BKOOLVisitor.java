// Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link BKOOLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface BKOOLVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(BKOOLParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#class_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass_decl(BKOOLParser.Class_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#class_mem}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass_mem(BKOOLParser.Class_memContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#class_mem_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass_mem_list(BKOOLParser.Class_mem_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#class_mem_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass_mem_decl(BKOOLParser.Class_mem_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#attr_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttr_decl(BKOOLParser.Attr_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#const_attr_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConst_attr_decl(BKOOLParser.Const_attr_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#static_attr_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatic_attr_decl(BKOOLParser.Static_attr_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#static_const_attr_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatic_const_attr_decl(BKOOLParser.Static_const_attr_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#attr_decl_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttr_decl_list(BKOOLParser.Attr_decl_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#attr_decl_unit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttr_decl_unit(BKOOLParser.Attr_decl_unitContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#method_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethod_decl(BKOOLParser.Method_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#param_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam_list(BKOOLParser.Param_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#param_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam_decl(BKOOLParser.Param_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#param}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam(BKOOLParser.ParamContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#idlist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdlist(BKOOLParser.IdlistContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#constructor_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstructor_decl(BKOOLParser.Constructor_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#class_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass_type(BKOOLParser.Class_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#decl_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecl_type(BKOOLParser.Decl_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#primitive_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitive_type(BKOOLParser.Primitive_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#array_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_type(BKOOLParser.Array_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStmt(BKOOLParser.StmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#block_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock_stmt(BKOOLParser.Block_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#local_var_decls}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLocal_var_decls(BKOOLParser.Local_var_declsContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#local_var_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLocal_var_decl(BKOOLParser.Local_var_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#var_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_decl(BKOOLParser.Var_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#const_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConst_decl(BKOOLParser.Const_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#decl_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecl_list(BKOOLParser.Decl_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#decl_unit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecl_unit(BKOOLParser.Decl_unitContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#stmts}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStmts(BKOOLParser.StmtsContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#assign_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssign_stmt(BKOOLParser.Assign_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#lhs}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLhs(BKOOLParser.LhsContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#lhs_unit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLhs_unit(BKOOLParser.Lhs_unitContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#lhs_member_access_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLhs_member_access_expr(BKOOLParser.Lhs_member_access_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#lhs_index_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLhs_index_expr(BKOOLParser.Lhs_index_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#if_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_stmt(BKOOLParser.If_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#if_then_else_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_then_else_stmt(BKOOLParser.If_then_else_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#if_then_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_then_stmt(BKOOLParser.If_then_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#for_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_stmt(BKOOLParser.For_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#break_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreak_stmt(BKOOLParser.Break_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#continue_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinue_stmt(BKOOLParser.Continue_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#return_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturn_stmt(BKOOLParser.Return_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#method_invocation_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethod_invocation_stmt(BKOOLParser.Method_invocation_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(BKOOLParser.ExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr1(BKOOLParser.Expr1Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr2(BKOOLParser.Expr2Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr3(BKOOLParser.Expr3Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr4(BKOOLParser.Expr4Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr5}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr5(BKOOLParser.Expr5Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr6}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr6(BKOOLParser.Expr6Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr7}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr7(BKOOLParser.Expr7Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr8}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr8(BKOOLParser.Expr8Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr9}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr9(BKOOLParser.Expr9Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr10}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr10(BKOOLParser.Expr10Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr11}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr11(BKOOLParser.Expr11Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr12}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr12(BKOOLParser.Expr12Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#method_call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethod_call(BKOOLParser.Method_callContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#expr_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr_list(BKOOLParser.Expr_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#literal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral(BKOOLParser.LiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#arrlit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArrlit(BKOOLParser.ArrlitContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKOOLParser#literal_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral_list(BKOOLParser.Literal_listContext ctx);
}