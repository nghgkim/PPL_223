from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program([self.visit(decl) for decl in ctx.class_decl()])

    ### Class Declaration ###

    def visitClass_decl(self, ctx: BKOOLParser.Class_declContext):
        classname = Id(ctx.ID(0).getText())
        parentname = Id(ctx.ID(1).getText()) if ctx.EXTENDS() else None
        memlist = self.visit(ctx.class_mem())
        return ClassDecl(classname, memlist, parentname)

    def visitClass_mem(self, ctx: BKOOLParser.Class_memContext):
        return self.visit(ctx.class_mem_list())

    def visitClass_mem_list(self, ctx: BKOOLParser.Class_mem_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.class_mem_decl()) + self.visit(ctx.class_mem_list())

    def visitClass_mem_decl(self, ctx: BKOOLParser.Class_mem_declContext):
        return self.visitChildren(ctx)

    def visitAttr_decl(self, ctx: BKOOLParser.Attr_declContext):
        kind = Instance()
        varType = self.visit(ctx.decl_type())
        lst = self.visit(ctx.attr_decl_list())
        return list(AttributeDecl(kind, VarDecl(variable, varType, varInit)) for (variable, varInit) in lst)

    def visitConst_attr_decl(self, ctx: BKOOLParser.Const_attr_declContext):
        kind = Instance()
        constType = self.visit(ctx.decl_type())
        lst = self.visit(ctx.attr_decl_list())
        return list(AttributeDecl(kind, ConstDecl(constant, constType, value)) for (constant, value) in lst)

    def visitStatic_attr_decl(self, ctx: BKOOLParser.Static_attr_declContext):
        kind = Static()
        varType = self.visit(ctx.decl_type())
        lst = self.visit(ctx.attr_decl_list())
        return list(AttributeDecl(kind, VarDecl(variable, varType, varInit)) for (variable, varInit) in lst)

    def visitStatic_const_attr_decl(self, ctx: BKOOLParser.Static_const_attr_declContext):
        kind = Static()
        constType = self.visit(ctx.decl_type())
        lst = self.visit(ctx.attr_decl_list())
        return list(AttributeDecl(kind, ConstDecl(constant, constType, value)) for (constant, value) in lst)

    def visitAttr_decl_list(self, ctx: BKOOLParser.Attr_decl_listContext):
        variable, varInit = self.visit(ctx.attr_decl_unit())
        if ctx.getChildCount() == 1:
            return [(variable, varInit)]
        else:
            return [(variable, varInit)] + self.visit(ctx.attr_decl_list())

    def visitAttr_decl_unit(self, ctx: BKOOLParser.Attr_decl_unitContext):
        variable = Id(ctx.ID().getText())
        varInit = self.visit(ctx.expr()) if ctx.expr() else None
        return (variable, varInit)

    def visitMethod_decl(self, ctx: BKOOLParser.Method_declContext):
        kind = Static() if ctx.STATIC() else Instance()
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.param_list())
        returnType = self.visit(ctx.class_type())
        body = self.visit(ctx.block_stmt())
        return [MethodDecl(kind, name, param, returnType, body)]

    def visitConstructor_decl(self, ctx: BKOOLParser.Constructor_declContext):
        kind = Instance()
        name = Id("<init>")
        param = self.visit(ctx.param_list())
        returnType = None
        body = self.visit(ctx.block_stmt())
        return [MethodDecl(kind, name, param, returnType, body)]

    def visitParam_list(self, ctx: BKOOLParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.param_decl())

    def visitParam_decl(self, ctx: BKOOLParser.Param_declContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        else:
            return self.visit(ctx.param()) + self.visit(ctx.param_decl())

    def visitParam(self, ctx: BKOOLParser.ParamContext):
        varType = self.visit(ctx.decl_type())
        idlist = self.visit(ctx.idlist())
        return [VarDecl(variable, varType) for variable in idlist]

    def visitIdlist(self, ctx: BKOOLParser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())

    ### Statement ###

    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        return self.visitChildren(ctx)

    def visitBlock_stmt(self, ctx: BKOOLParser.Block_stmtContext):
        decl = self.visit(ctx.local_var_decls()) if ctx.local_var_decls() else []
        stmt = self.visit(ctx.stmts()) if ctx.stmts() else []
        return Block(decl, stmt)

    def visitAssign_stmt(self, ctx: BKOOLParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.expr())
        return Assign(lhs, exp)

    def visitIf_stmt(self, ctx: BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)

    def visitIf_then_stmt(self, ctx: BKOOLParser.If_then_stmtContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.stmt())
        return If(expr, thenStmt)

    def visitIf_then_else_stmt(self, ctx: BKOOLParser.If_then_else_stmtContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.stmt(0))
        elseStmt = self.visit(ctx.stmt(1))
        return If(expr, thenStmt, elseStmt)

    def visitFor_stmt(self, ctx: BKOOLParser.For_stmtContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        loop = self.visit(ctx.stmt())
        up = True if ctx.TO() else False
        return For(id, expr1, expr2, up, loop)

    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: BKOOLParser.Continue_stmtContext):
        return Continue()

    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        return Return(self.visit(ctx.expr()))

    def visitMethod_invocation_stmt(self, ctx: BKOOLParser.Method_invocation_stmtContext):
        obj = self.visit(ctx.expr())
        method, param = self.visit(ctx.method_call())
        return CallStmt(obj, method, param)

    def visitLocal_var_decls(self, ctx: BKOOLParser.Local_var_declsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.local_var_decl())
        else:
            return self.visit(ctx.local_var_decl()) + self.visit(ctx.local_var_decls())

    def visitLocal_var_decl(self, ctx: BKOOLParser.Local_var_declContext):
        return self.visitChildren(ctx)

    def visitVar_decl(self, ctx: BKOOLParser.Var_declContext):
        varType = self.visit(ctx.decl_type())
        lst = self.visit(ctx.decl_list())
        return list(VarDecl(variable, varType, varInit) for (variable, varInit) in lst)

    def visitConst_decl(self, ctx:BKOOLParser.Const_declContext):
        constType = self.visit(ctx.decl_type())
        lst = self.visit(ctx.decl_list())
        return list(ConstDecl(constant, constType, value) for (constant, value) in lst)

    def visitDecl_list(self, ctx: BKOOLParser.Decl_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl_unit())
        else:
            return self.visit(ctx.decl_unit()) + self.visit(ctx.decl_list())

    def visitDecl_unit(self, ctx: BKOOLParser.Decl_unitContext):
        variable = Id(ctx.ID().getText())
        varInit = self.visit(ctx.expr()) if ctx.expr() else None
        return [[variable, varInit]]

    def visitStmts(self, ctx: BKOOLParser.StmtsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        else:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmts())

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        return self.visitChildren(ctx)

    def visitLhs_unit(self, ctx: BKOOLParser.Lhs_unitContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitChildren(ctx)

    def visitLhs_member_access_expr(self, ctx: BKOOLParser.Lhs_member_access_exprContext):
        obj = self.visit(ctx.expr11())
        if ctx.ID():
            fieldname = Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname)
        else:
            method, param = self.visit(ctx.method_call())
            return CallExpr(obj, method, param)

    def visitLhs_index_expr(self, ctx: BKOOLParser.Lhs_index_exprContext):
        arr = self.visit(ctx.expr10())
        idx = self.visit(ctx.expr())
        return ArrayCell(arr, idx)

    ### Type ###

    def visitClass_type(self, ctx: BKOOLParser.Class_typeContext):
        if ctx.VOID():
            return VoidType()
        else:
            return self.visit(ctx.decl_type())

    def visitDecl_type(self, ctx: BKOOLParser.Decl_typeContext):
        if ctx.ID(): return ClassType(Id(ctx.ID().getText()))
        elif ctx.primitive_type(): return self.visit(ctx.primitive_type())
        else: return self.visit(ctx.array_type())

    def visitPrimitive_type(self, ctx: BKOOLParser.Primitive_typeContext):
        if ctx.INT(): return IntType()
        elif ctx.FLOAT(): return FloatType()
        elif ctx.STRING(): return StringType()
        else: return BoolType()

    def visitArray_type(self, ctx: BKOOLParser.Array_typeContext):
        eleType = ClassType(Id(ctx.ID().getText())) if ctx.ID() else self.visit(ctx.primitive_type())
        size = int(ctx.INTLIT().getText())
        return ArrayType(size, eleType)

    ### Expression ###

    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        return self.visit(ctx.expr1())

    def visitExpr1(self, ctx: BKOOLParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            return BinaryOp(op, left, right)

    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr3(0))
            right = self.visit(ctx.expr3(1))
            return BinaryOp(op, left, right)

    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(op, left, right)

    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(op, left, right)

    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr5())
            right = self.visit(ctx.expr6())
            return BinaryOp(op, left, right)

    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.expr6())
            right = self.visit(ctx.expr7())
            return BinaryOp(op, left, right)

    def visitExpr7(self, ctx: BKOOLParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.expr7())
            return UnaryOp(op, body)

    def visitExpr8(self, ctx: BKOOLParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.expr8())
            return UnaryOp(op, body)

    def visitExpr9(self, ctx: BKOOLParser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            arr = self.visit(ctx.expr10())
            idx = self.visit(ctx.expr())
            return ArrayCell(arr, idx)

    def visitExpr10(self, ctx: BKOOLParser.Expr10Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            obj = self.visit(ctx.expr10())
            if ctx.ID():
                fieldname = Id(ctx.ID().getText())
                return FieldAccess(obj, fieldname)
            else:
                method, param = self.visit(ctx.method_call())
                return CallExpr(obj, method, param)

    def visitExpr11(self, ctx: BKOOLParser.Expr11Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        else:
            classname = Id(ctx.ID().getText())
            param = self.visit(ctx.expr_list()) if ctx.expr_list() else []
            return NewExpr(classname, param)

    def visitExpr12(self, ctx: BKOOLParser.Expr12Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.NIL():
            return NullLiteral()
        else:
            return self.visit(ctx.literal())

    def visitMethod_call(self, ctx: BKOOLParser.Method_callContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        return method, param

    def visitExpr_list(self, ctx: BKOOLParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())

    ### Literal ###

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        else:
            return self.visit(ctx.arrlit())

    def visitArrlit(self, ctx: BKOOLParser.ArrlitContext):
        return ArrayLiteral(self.visit(ctx.literal_list()))

    def visitLiteral_list(self, ctx: BKOOLParser.Literal_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.literal())]
        else:
            return [self.visit(ctx.literal())] + self.visit(ctx.literal_list())