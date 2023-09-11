
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
# from Utils import Utils
from StaticError import *

class Utils:
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class GetEnv(BaseVisitor, Utils):
    def __init__(self):
        self.globalEnv = {}

    def visitProgram(self, ast, o):
        o = self.globalEnv
        for x in ast.decl:
            self.visit(x, o)
        return o

    def visitClassDecl(self, ast, o):
        env = {}
        env['current'] = ast.classname.name
        env['global'] = o

        if ast.parentname is not None:
            if env['global'].get(ast.parentname.name) is not None:
                env['parent'] = ast.parentname.name
            else:
                raise Undeclared(Class(), ast.parentname.name)
        else:
            env['parent'] = None

        name = ast.classname.name
        if o.get(name) is not None:
            raise Redeclared(Class(), name)
        o[name] = {}
        for mem in ast.memlist:
            self.visit(mem, o[name])

    def visitAttributeDecl(self, ast, o):
        if type(ast.kind) is Instance:
            self.visit(ast.decl, ('Instance', o))
        else:
            self.visit(ast.decl, ('Static', o))

    def visitVarDecl(self, ast, o):
        kind, env = o
        name = ast.variable.name

        if env.get(name) is not None:
            raise Redeclared(Attribute(), name)

        env[name] = ('Mutable', self.visit(ast.varType, env), kind)

    def visitConstDecl(self, ast, o):
        kind, env = o
        name = ast.constant.name

        if env.get(name) is not None:
            raise Redeclared(Attribute(), name)

        env[name] = ('Immutable', self.visit(ast.constType, env), kind)

    def visitMethodDecl(self, ast, o):
        if type(ast.kind) is Static:
            kind = 'Static'
        else:
            kind = 'Instance'

        name = ast.name.name

        if o.get(name) is not None:
            raise Redeclared(Method(), name)

        param = map(lambda x: self.visit(x, (None, {})), ast.param)

        if ast.returnType is not None:
            o[name] = ('Method', self.visit(ast.returnType, o), kind, param)
        else:
            o[name] = ('Method', None, kind, param)

    def visitIntType(self, ast, param):
        return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self, ast, param):
        env = self.globalEnv
        if ast.classname.name in env:
            return ClassType(ast.classname)
        raise Undeclared(Class(), ast.classname.name)

class Util:
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    def isNotConst(expType):
        return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]

class StaticChecker(BaseVisitor, Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self, ast, o):
        o = GetEnv().visit(ast, None)
        return [self.visit(decl, o) for decl in ast.decl]

    def visitClassDecl(self, ast, o):
        env = {}
        env['current'] = ast.classname.name
        env['global'] = o

        if ast.parentname is not None:
            if env['global'].get(ast.parentname.name) is not None:
                env['parent'] = ast.parentname.name
            else:
                raise Undeclared(Class(), ast.parentname.name)
        else:
            env['parent'] = None

        for mem in ast.memlist:
            self.visit(mem, env)

    def visitAttributeDecl(self, ast, o):
        env = o
        if type(ast.decl) is VarDecl:
            self.visit(ast.decl, (Variable(), env))
        if type(ast.decl) is ConstDecl:
            self.visit(ast.decl, (Constant(), env))

    def visitMethodDecl(self, ast, o):
        env = {}
        env['global'] = o['global']
        env['local'] = [{}]
        env['current'] = o['current']
        env['parent'] = o['parent']

        paramList = []
        for param in ast.param:
            paramList = paramList + [self.visit(param, (Parameter(), env))]

        decls = ast.body.decl
        stmts = ast.body.stmt
        for decl in decls:
            if type(decl) is VarDecl:
                self.visit(decl, (Variable(), env))
            else:
                self.visit(decl, (Constant(), env))

        for stmt in stmts:
            if type(stmt) is not Return:
                self.visit(stmt, (False, env))
            else:
                typeMethod = self.visit(ast.returnType, o)
                self.visit(stmt, (typeMethod, env))

    def visitBlock(self, ast, o):
        env1, env2 = o
        env = {}
        env['global'] = env2['global']
        env['local'] = [{}] + env2['local']
        env['current'] = env2['current']
        env['parent'] = env2['parent']

        decls = ast.decl
        stmts = ast.stmt
        for decl in decls:
            if type(decl) is VarDecl:
                self.visit(decl, (Variable(), env))
            else:
                self.visit(decl, (Constant(), env))

        stmtList = []
        for stmt in stmts:
            stmtList = stmtList + [self.visit(stmt, (env1, env))]

    def visitVarDecl(self, ast: VarDecl, o: object):
        kind, env = o
        name = ast.variable.name
        typeOfVar = self.visit(ast.varType, env)
        if ast.varInit is not None:
            value = self.visit(ast.varInit, env)
            if value[0] == 'Mutable' or value[0] == 'Immutable' or value[0] == 'Method':
                if Util.isNotAccess(ast.varInit):
                    raise Undeclared(Identifier(), ast.varInit.name)
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:
                raise Redeclared(kind, name)
            env['local'][0][name] = ('Var', typeOfVar, None)

    def visitConstDecl(self, ast: ConstDecl, o: object):
        kind, env = o
        name = ast.constant.name
        if ast.value is None:
            raise IllegalConstantExpression(ast.value)
        if Util.isNotConst(ast.value):
            raise IllegalConstantExpression(ast.value)

        valueCheck = self.visit(ast.value, (True, env))
        if valueCheck[0] == 'Mutable' or valueCheck[0] == 'Immutable' or valueCheck[0] == 'Method':
            if Util.isNotAccess(ast.value):
                raise Undeclared(Identifier(), ast.value.name)
        if valueCheck[0] == 'Var' or valueCheck[0] == 'Mutable':
            raise IllegalConstantExpression(ast.value)
        value = self.visit(ast.value, env)[1]
        typeOfConst = self.visit(ast.constType, o)
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:
                raise Redeclared(kind, name)
        if type(typeOfConst) is ArrayType and type(value) is ArrayType:
            if typeOfConst.size != value.size:
                raise TypeMismatchInConstant(ast)
            if type(typeOfConst.eleType) is not type(value.eleType):
                if not (type(typeOfConst.eleType) is FloatType and type(value.eleType) is IntType):
                    raise TypeMismatchInConstant(ast)
        if type(value) is not type(typeOfConst):
            if not (type(typeOfConst) is FloatType and type(value) is IntType):
                raise TypeMismatchInConstant(ast)
        if env.get('local') is not None:
            env['local'][0][name] = ('const', typeOfConst, None)

    def visitId(self, ast: Id, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if env.get('local') is not None:
            for local in env['local']:
                if ast.name in local:
                    return local[ast.name]
        if ast.name in env['global'][env['current']]:
            return env['global'][env['current']][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ast.name]
        raise Undeclared(Identifier(), ast.name)

    def visitAssign(self, ast, o):
        inLoop, env = o
        lhs = self.visit(ast.lhs, env)
        exp = self.visit(ast.exp, env)

        kindlhs = lhs[0]
        typeLhs = lhs[1]
        typeExp = exp[1]
        if kindlhs == 'const' or kindlhs == 'Immutable':
            raise CannotAssignToConstant(ast)
        if lhs[0] == 'Mutable' or lhs[0] == 'Immutable' or lhs[0] == 'Method':
            if Util.isNotAccess(ast.lhs):
                raise Undeclared(Identifier(), ast.lhs.name)
        if exp[0] == 'Mutable' or exp[0] == 'Immutable' or exp[0] == 'Method':
            if Util.isNotAccess(ast.exp):
                raise Undeclared(Identifier(), ast.exp.name)
        if type(typeLhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(typeLhs) is ArrayType and type(typeExp) is ArrayType:
            if typeLhs.size != typeExp.size:
                raise TypeMismatchInStatement(ast)
            if type(typeLhs.eleType) is not type(typeExp.eleType):
                if not (type(typeLhs.eleType) is FloatType and type(typeExp.eleType) is IntType):
                    raise TypeMismatchInStatement(ast)
        if not ((type(typeLhs) is type(typeExp)) or (type(typeLhs) is FloatType and type(typeExp) is IntType)):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast: If, o):
        inLoop, env = o
        condType = self.visit(ast.expr, env)
        if condType[0] == 'Mutable' or condType[0] == 'Immutable' or condType[0] == 'Method':
            if Util.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        if type(condType[1]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, (inLoop, env))
        self.visit(ast.elseStmt, (inLoop, env))

    def visitFor(self, ast: For, o):
        inLoop, env = o

        idType = self.visit(ast.id, env)
        exp1Type = self.visit(ast.expr1, env)
        exp2Type = self.visit(ast.expr2, env)

        if idType[0] == 'Mutable' or idType[0] == 'Immutable' or idType[0] == 'Method':
            if Util.isNotAccess(ast.id):
                raise Undeclared(Identifier(), ast.id.name)
        if exp1Type[0] == 'Mutable' or exp1Type[0] == 'Immutable' or exp1Type[0] == 'Method':
            if Util.isNotAccess(ast.expr1):
                raise Undeclared(Identifier(), ast.expr1.name)
        if exp2Type[0] == 'Mutable' or exp2Type[0] == 'Immutable' or exp2Type[0] == 'Method':
            if Util.isNotAccess(ast.expr2):
                raise Undeclared(Identifier(), ast.expr2.name)
        if idType[0] == 'const' or idType[0] == 'Immutable':
            raise CannotAssignToConstant(ast.expr1)
        if False in [type(x) is IntType for x in [exp1Type[1], exp2Type[1]]]:
            raise TypeMismatchInStatement(ast)
        if Util.isNaNType(idType[1]):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, (True, env))

    def visitContinue(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitBreak(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitReturn(self, ast, o):
        typeMethod, env = o
        typeReturn = self.visit(ast.expr, o)
        if typeReturn[0] == 'Mutable' or typeReturn[0] == 'Immutable' or typeReturn[0] == 'Method':
            if Util.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        if type(typeMethod) is not type(typeReturn[1]):
            if not (type(typeMethod) is FloatType and type(typeReturn[1]) is IntType):
                raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast: BinaryOp, o):
        if type(o) is tuple:
            if Util.isNotConst(ast.left):
                raise IllegalConstantExpression(ast)
            if Util.isNotConst(ast.right):
                raise IllegalConstantExpression(ast)
            lType = self.visit(ast.left, o)
            rType = self.visit(ast.right, o)
            if lType[0] == 'Var' or lType[0] == 'Mutable':
                raise IllegalConstantExpression(ast)
            if rType[0] == 'Var' or rType[0] == 'Mutable':
                raise IllegalConstantExpression(ast)
        else:
            lType = self.visit(ast.left, o)
            rType = self.visit(ast.right, o)
        if lType[0] == 'Mutable' or lType[0] == 'Immutable' or lType[0] == 'Method':
            if Util.isNotAccess(ast.left):
                raise Undeclared(Identifier(), ast.left.name)
        if rType[0] == 'Mutable' or rType[0] == 'Immutable' or rType[0] == 'Method':
            if Util.isNotAccess(ast.right):
                raise Undeclared(Identifier(), ast.right.name)
        op = str(ast.op)
        if op in ["+", "-", "*"]:
            if Util.isNaNType(lType[1]) or Util.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            if type(lType[1]) is FloatType or type(rType[1]) is FloatType:
                return (None, FloatType(), None)
            return (None, IntType(), None)
        if op in ["/"]:
            if Util.isNaNType(lType[1]) or Util.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            return (None, FloatType(), None)
        if op in ["\\", "%"]:
            if not (type(lType[1]) is IntType) or not (type(rType[1]) is IntType):
                raise TypeMismatchInExpression(ast)
            return (None, IntType(), None)
        if op in ["==", "!="]:
            if type(lType[1]) is type(rType[1]):
                if (type(lType[1]) is IntType) or (type(rType[1]) is BoolType):
                    return (None, BoolType(), None)
            raise TypeMismatchInExpression(ast)
        if op in [">", "<", ">=", "<="]:
            if Util.isNaNType(lType[1]) or Util.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            return (None, BoolType(), None)
        if op in ["&&", "||"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is BoolType:
                    return (None, BoolType(), None)
            raise TypeMismatchInExpression(ast)
        if op in ["^"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is StringType:
                    return (None, StringType(), None)
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, o):
        if type(o) is tuple:
            if Util.isNotConst(ast.body):
                raise IllegalConstantExpression(ast.body)
            exp = self.visit(ast.body, o)
            if exp[0] == 'Var' or exp[0] == "Mutable":
                raise IllegalConstantExpression(ast.body)
            expType = exp
        else:
            expType = self.visit(ast.body, o)
        if expType[0] == 'Mutable' or expType[0] == 'Immutable' or expType[0] == 'Method':
            if Util.isNotAccess(ast.body):
                raise Undeclared(Identifier(), ast.body.name)
        op = str(ast.op)
        if (op == '-' and Util.isNaNType(expType[1])) or (op == '!' and type(expType[1]) is not BoolType):
            raise TypeMismatchInExpression(ast)
        return (None, expType[1], None)

    def visitArrayCell(self, ast, o):
        arrType = self.visit(ast.arr, o)
        idxType = self.visit(ast.idx, o)
        if type(idxType[1]) is not IntType or type(arrType[1]) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        return (None, arrType[1], None)

    def visitCallExpr(self, ast, o):
        if type(ast.obj) is SelfLiteral:
            method = self.handleAccess(
                ast.method, (Method(), o, o['current']))
            if fieldname[2] == 'Static':
                raise IllegalMemberAccess(ast)
        else:
            try:
                nameClass = self.visit(ast.obj,  o)
            except:
                if ast.obj.name in o['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInExpression(ast)
                method = self.handleAccess(
                    ast.method, (Method(), o, nameClass[1].classname.name))
                if method[2] == 'Static':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is VoidType:
                    raise TypeMismatchInExpression(ast)
                if method[0] != 'Method':
                    raise TypeMismatchInExpression(ast)
            if type(nameClass) is str:
                method = self.handleAccess(
                    ast.method, (Method(), o, nameClass))
                if method[2] == 'Instance':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is VoidType:
                    raise TypeMismatchInExpression(ast)
                if method[0] != 'Method':
                    raise TypeMismatchInExpression(ast)
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
            if len(paramCall) != len(method[3]):
                raise TypeMismatchInExpression(ast)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(method[3][i][1]):
                    if not (type(method[3][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInExpression(ast)
        return (None, method[1], None)

    def visitCallStmt(self, ast, o):
        inLoop, env = o
        if type(ast.obj) is SelfLiteral:
            method = self.handleAccess(ast.method, (Method(), o, env['current']))
            if method[2] == 'Static':
                raise IllegalMemberAccess(ast)
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
        else:
            try:
                nameClass = self.visit(ast.obj,  env)
            except:
                if ast.obj.name in env['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInStatement(ast)
                method = self.handleAccess(
                    ast.method, (Method(), env, nameClass[1].classname.name))
                if method[2] == 'Static':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                if method[0] != 'Method':
                    raise TypeMismatchInStatement(ast)
            if type(nameClass) is str:
                method = self.handleAccess(
                    ast.method, (Method(), env, nameClass))
                if method[2] == 'Instance':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                if method[0] != 'Method':
                    raise TypeMismatchInStatement(ast)
            paramCall = map(lambda x: self.visit(x, env), ast.param)
            if len(paramCall) != len(method[3]):
                raise TypeMismatchInStatement(ast)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(method[3][i][1]):
                    if not (type(method[3][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInStatement(ast)

    def visitFieldAccess(self, ast, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if type(ast.obj) is SelfLiteral:
            fieldname = self.handleAccess(
                ast.fieldname, (Attribute(), env, env['current']))
            if fieldname[2] == 'Static':
                raise IllegalMemberAccess(ast)
        else:
            try:
                nameClass = self.visit(ast.obj,  env)
            except:
                if ast.obj.name in env['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInExpression(ast)
                fieldname = self.handleAccess(
                    ast.fieldname, (Attribute(), env, nameClass[1].classname.name))
                if fieldname[2] == 'Static':
                    raise IllegalMemberAccess(ast)
                if fieldname[0] == 'Method':
                    raise TypeMismatchInExpression(ast)
            if type(nameClass) is str:
                fieldname = self.handleAccess(
                    ast.fieldname, (Attribute(), env, nameClass))

                if fieldname[2] == 'Instance':
                    raise IllegalMemberAccess(ast)
                if fieldname[0] == 'Method':
                    raise TypeMismatchInExpression(ast)
        return (fieldname[0], fieldname[1], None)

    def handleAccess(self, ast, o):
        kind, env, name = o
        if ast.name in env['global'][name]:
            return env['global'][name][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ast.name]
        raise Undeclared(kind, ast.name)

    def visitNewExpr(self, ast, o):
        env = o
        if ast.classname.name in env['global']:
            classType = (None, ClassType(ast.classname), None)
        else:
            raise Undeclared(Class(), ast.classname.name)
        if (len(ast.param) != 0):
            if "<init>" in env['global'][ast.classname.name]:
                constructor = env['global'][ast.classname.name]["<init>"]
            else:
                raise Undeclared(Method(), "<init>")
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
            if len(paramCall) != len(constructor[3]):
                raise TypeMismatchInExpression(ast)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(constructor[3][i][1]):
                    if not (type(constructor[3][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInExpression(ast)
        return classType

    def visitIntLiteral(self, ast, param):
        return (None, IntType(), None)

    def visitFloatLiteral(self, ast, param):
        return (None, FloatType(), None)

    def visitBooleanLiteral(self, ast, param):
        return (None, BoolType(), None)

    def visitStringLiteral(self, ast, param):
        return (None, StringType(), None)

    def visitNullLiteral(self, ast, param):
        return (None, NullLiteral(), None)

    def visitSelfLiteral(self, ast, param):
        return (None, SelfLiteral(), None)

    def visitArrayLiteral(self, ast, param):
        temp = list(map(lambda x: self.visit(x, param), ast.value))
        default = temp[0][1]
        for typeOfElement in temp:
            if type(typeOfElement[1]) is not type(default):
                raise IllegalArrayLiteral(ast)
        return (None,  ArrayType(len(temp), default), None)


    def visitIntType(self, ast, param):
        return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self, ast, o):
        env = o
        if ast.classname.name in env['global']:
            return ast
        raise Undeclared(Class(), ast.classname.name)