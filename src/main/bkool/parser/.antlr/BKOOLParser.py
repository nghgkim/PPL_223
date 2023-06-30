# Generated from /Users/nguyenkim/Downloads/assignment1/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\13\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2\3")
        buf.write("\3\2\24\25\2\b\2\6\3\2\2\2\4\b\3\2\2\2\6\7\3\2\2\2\7\3")
        buf.write("\3\2\2\2\b\t\t\2\2\2\t\5\3\2\2\2\2")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'boolean'", 
                     "'break'", "'class'", "'continue'", "'do'", "'else'", 
                     "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
                     "'then'", "'for'", "'return'", "'true'", "'false'", 
                     "'void'", "'nil'", "'this'", "'final'", "'static'", 
                     "'to'", "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", 
                     "'||'", "'&&'", "'!'", "'^'", "':='", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "LINE_CMT", "BLOCK_CMT", "BOOLEAN", "BREAK", 
                      "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", 
                      "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                      "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                      "TO", "DOWNTO", "ADDOP", "SUBOP", "MULOP", "FLOAT_DIV", 
                      "INTEGER_DIV", "MOD", "NOT_EQUAL", "EQUAL", "LESS", 
                      "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", "OR", 
                      "AND", "NOT", "CONCATENATION", "ASSIGN", "LSB", "RSB", 
                      "LP", "RP", "LB", "RB", "SEMI_COLONE", "COLON", "DOT", 
                      "COMMA", "INT_LIT", "FLOAT_LIT", "STR_LIT", "ID", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_bool_lit = 1

    ruleNames =  [ "program", "bool_lit" ]

    EOF = Token.EOF
    LINE_CMT=1
    BLOCK_CMT=2
    BOOLEAN=3
    BREAK=4
    CLASS=5
    CONTINUE=6
    DO=7
    ELSE=8
    EXTENDS=9
    FLOAT=10
    IF=11
    INT=12
    NEW=13
    STRING=14
    THEN=15
    FOR=16
    RETURN=17
    TRUE=18
    FALSE=19
    VOID=20
    NIL=21
    THIS=22
    FINAL=23
    STATIC=24
    TO=25
    DOWNTO=26
    ADDOP=27
    SUBOP=28
    MULOP=29
    FLOAT_DIV=30
    INTEGER_DIV=31
    MOD=32
    NOT_EQUAL=33
    EQUAL=34
    LESS=35
    GREATER=36
    LESS_OR_EQUAL=37
    GREATER_OR_EQUAL=38
    OR=39
    AND=40
    NOT=41
    CONCATENATION=42
    ASSIGN=43
    LSB=44
    RSB=45
    LP=46
    RP=47
    LB=48
    RB=49
    SEMI_COLONE=50
    COLON=51
    DOT=52
    COMMA=53
    INT_LIT=54
    FLOAT_LIT=55
    STR_LIT=56
    ID=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

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


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_lit




    def bool_lit(self):

        localctx = BKOOLParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
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





