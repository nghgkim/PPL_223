# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("$\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\2\2\6\2\4\6")
        buf.write("\b\2\3\3\2\4\5\2!\2\13\3\2\2\2\4\21\3\2\2\2\6\34\3\2\2")
        buf.write("\2\b!\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13")
        buf.write("\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3")
        buf.write("\3\2\2\2\21\22\7\3\2\2\22\23\7\6\2\2\23\27\7\7\2\2\24")
        buf.write("\26\5\6\4\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33\7\b\2")
        buf.write("\2\33\5\3\2\2\2\34\35\7\6\2\2\35\36\7\n\2\2\36\37\5\b")
        buf.write("\5\2\37 \7\t\2\2 \7\3\2\2\2!\"\t\2\2\2\"\t\3\2\2\2\4\r")
        buf.write("\27")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'integer'", "'void'", "<INVALID>", 
                     "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "ID", 
                      "LP", "RP", "SEMI", "COLON", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_memdecl = 2
    RULE_bkooltype = 3

    ruleNames =  [ "program", "classdecl", "memdecl", "bkooltype" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    ID=4
    LP=5
    RP=6
    SEMI=7
    COLON=8
    WS=9
    ERROR_CHAR=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.classdecl()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.T__0):
                    break

            self.state = 13
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def memdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MemdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MemdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = BKOOLParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(BKOOLParser.T__0)
            self.state = 16
            self.match(BKOOLParser.ID)
            self.state = 17
            self.match(BKOOLParser.LP)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.ID:
                self.state = 18
                self.memdecl()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_memdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemdecl" ):
                return visitor.visitMemdecl(self)
            else:
                return visitor.visitChildren(self)




    def memdecl(self):

        localctx = BKOOLParser.MemdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(BKOOLParser.ID)
            self.state = 27
            self.match(BKOOLParser.COLON)
            self.state = 28
            self.bkooltype()
            self.state = 29
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BkooltypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(BKOOLParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bkooltype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBkooltype" ):
                return visitor.visitBkooltype(self)
            else:
                return visitor.visitChildren(self)




    def bkooltype(self):

        localctx = BKOOLParser.BkooltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bkooltype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INTTYPE or _la==BKOOLParser.VOIDTYPE):
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





