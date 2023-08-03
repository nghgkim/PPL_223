# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("A\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\6\5,\n\5\r\5\16\5-\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\6\n9\n\n\r\n\16\n:\3\n\3\n\3\13\3\13\3\13\2\2")
        buf.write("\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\4")
        buf.write("\4\2C\\c|\5\2\13\f\17\17\"\"\2B\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27")
        buf.write("\3\2\2\2\5\35\3\2\2\2\7%\3\2\2\2\t+\3\2\2\2\13/\3\2\2")
        buf.write("\2\r\61\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\238\3\2\2")
        buf.write("\2\25>\3\2\2\2\27\30\7e\2\2\30\31\7n\2\2\31\32\7c\2\2")
        buf.write("\32\33\7u\2\2\33\34\7u\2\2\34\4\3\2\2\2\35\36\7k\2\2\36")
        buf.write("\37\7p\2\2\37 \7v\2\2 !\7g\2\2!\"\7i\2\2\"#\7g\2\2#$\7")
        buf.write("t\2\2$\6\3\2\2\2%&\7x\2\2&\'\7q\2\2\'(\7k\2\2()\7f\2\2")
        buf.write(")\b\3\2\2\2*,\t\2\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.")
        buf.write("\3\2\2\2.\n\3\2\2\2/\60\7}\2\2\60\f\3\2\2\2\61\62\7\177")
        buf.write("\2\2\62\16\3\2\2\2\63\64\7=\2\2\64\20\3\2\2\2\65\66\7")
        buf.write("<\2\2\66\22\3\2\2\2\679\t\3\2\28\67\3\2\2\29:\3\2\2\2")
        buf.write(":8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\b\n\2\2=\24\3\2\2\2>")
        buf.write("?\13\2\2\2?@\b\13\3\2@\26\3\2\2\2\5\2-:\4\b\2\2\3\13\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    LP = 5
    RP = 6
    SEMI = 7
    COLON = 8
    WS = 9
    ERROR_CHAR = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'integer'", "'void'", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "LP", "RP", "SEMI", "COLON", "WS", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "LP", "RP", "SEMI", 
                  "COLON", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[9] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


