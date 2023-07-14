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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01ab\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3g\n\3")
        buf.write("\3\3\3\3\7\3k\n\3\f\3\16\3n\13\3\3\3\3\3\3\4\3\4\5\4t")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5|\n\5\3\5\3\5\3\6\3\6")
        buf.write("\5\6\u0082\n\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\5\n\u0091\n\n\3\n\3\n\3\n\3\n\3\n\5\n\u0098")
        buf.write("\n\n\5\n\u009a\n\n\3\13\5\13\u009d\n\13\3\13\3\13\5\13")
        buf.write("\u00a1\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00ad\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00b4")
        buf.write("\n\f\3\r\3\r\3\16\3\16\3\16\5\16\u00bb\n\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00cd\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u00d4\n\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u00dc\n\25\f\25\16\25\u00df\13\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u00e7\n\26\f\26\16\26\u00ea\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\7\27\u00f2\n\27\f\27\16\27\u00f5")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00fd\n\30\f")
        buf.write("\30\16\30\u0100\13\30\3\31\3\31\3\31\5\31\u0105\n\31\3")
        buf.write("\32\3\32\3\32\5\32\u010a\n\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u0112\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u011a\n\34\3\34\5\34\u011d\n\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0124\n\34\3\34\5\34\u0127\n\34\7\34\u0129")
        buf.write("\n\34\f\34\16\34\u012c\13\34\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0132\n\35\3\35\3\35\5\35\u0136\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\5\36\u0140\n\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0149\n\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \5 \u0152\n \3!\3!\5!\u0156\n!\3!\3!\3\"\5\"\u015b")
        buf.write("\n\"\3\"\7\"\u015e\n\"\f\"\16\"\u0161\13\"\3\"\7\"\u0164")
        buf.write("\n\"\f\"\16\"\u0167\13\"\3#\3#\5#\u016b\n#\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\3$\5$\u0177\n$\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\5)\u018e\n")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\5*\u019c\n*\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3,\5,\u01a7\n,\3-\3-\3-\2\7(*,.\66")
        buf.write(".\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVX\2\n\6\2\5\5\f\f\16\16\20\20\3")
        buf.write("\2%(\3\2#$\3\2)*\3\2\35\36\3\2\37\"\3\2\33\34\3\28;\2")
        buf.write("\u01b7\2]\3\2\2\2\4b\3\2\2\2\6s\3\2\2\2\b{\3\2\2\2\n\u0081")
        buf.write("\3\2\2\2\f\u0085\3\2\2\2\16\u0088\3\2\2\2\20\u008b\3\2")
        buf.write("\2\2\22\u0099\3\2\2\2\24\u00ac\3\2\2\2\26\u00b3\3\2\2")
        buf.write("\2\30\u00b5\3\2\2\2\32\u00ba\3\2\2\2\34\u00bc\3\2\2\2")
        buf.write("\36\u00be\3\2\2\2 \u00c0\3\2\2\2\"\u00c5\3\2\2\2$\u00cc")
        buf.write("\3\2\2\2&\u00d3\3\2\2\2(\u00d5\3\2\2\2*\u00e0\3\2\2\2")
        buf.write(",\u00eb\3\2\2\2.\u00f6\3\2\2\2\60\u0104\3\2\2\2\62\u0109")
        buf.write("\3\2\2\2\64\u0111\3\2\2\2\66\u0113\3\2\2\28\u012d\3\2")
        buf.write("\2\2:\u013f\3\2\2\2<\u0148\3\2\2\2>\u0151\3\2\2\2@\u0153")
        buf.write("\3\2\2\2B\u015f\3\2\2\2D\u016a\3\2\2\2F\u0170\3\2\2\2")
        buf.write("H\u0178\3\2\2\2J\u0181\3\2\2\2L\u0184\3\2\2\2N\u0187\3")
        buf.write("\2\2\2P\u018d\3\2\2\2R\u019b\3\2\2\2T\u019d\3\2\2\2V\u01a6")
        buf.write("\3\2\2\2X\u01a8\3\2\2\2Z\\\5\4\3\2[Z\3\2\2\2\\_\3\2\2")
        buf.write("\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7\2\2\3a")
        buf.write("\3\3\2\2\2bc\7\7\2\2cf\7<\2\2de\7\13\2\2eg\7<\2\2fd\3")
        buf.write("\2\2\2fg\3\2\2\2gh\3\2\2\2hl\7\60\2\2ik\5\6\4\2ji\3\2")
        buf.write("\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2mo\3\2\2\2nl\3\2\2\2")
        buf.write("op\7\61\2\2p\5\3\2\2\2qt\5\b\5\2rt\5\24\13\2sq\3\2\2\2")
        buf.write("sr\3\2\2\2t\7\3\2\2\2u|\7\32\2\2v|\7\31\2\2wx\7\32\2\2")
        buf.write("x|\7\31\2\2yz\7\31\2\2z|\7\32\2\2{u\3\2\2\2{v\3\2\2\2")
        buf.write("{w\3\2\2\2{y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\5\n\6\2~\t")
        buf.write("\3\2\2\2\177\u0082\5\f\7\2\u0080\u0082\5\16\b\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0084\7\64\2\2\u0084\13\3\2\2\2\u0085\u0086\5\32\16\2")
        buf.write("\u0086\u0087\5\20\t\2\u0087\r\3\2\2\2\u0088\u0089\5\32")
        buf.write("\16\2\u0089\u008a\5\20\t\2\u008a\17\3\2\2\2\u008b\u008c")
        buf.write("\5\22\n\2\u008c\21\3\2\2\2\u008d\u0090\7<\2\2\u008e\u008f")
        buf.write("\7$\2\2\u008f\u0091\5$\23\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\7\67\2")
        buf.write("\2\u0093\u009a\5\22\n\2\u0094\u0097\7<\2\2\u0095\u0096")
        buf.write("\7$\2\2\u0096\u0098\5$\23\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u008d\3\2\2\2")
        buf.write("\u0099\u0094\3\2\2\2\u009a\23\3\2\2\2\u009b\u009d\7\32")
        buf.write("\2\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00a0")
        buf.write("\3\2\2\2\u009e\u00a1\5\32\16\2\u009f\u00a1\5\36\20\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\7<\2\2\u00a3\u00a4\7\62\2\2\u00a4\u00a5\5")
        buf.write("\26\f\2\u00a5\u00a6\7\63\2\2\u00a6\u00a7\5@!\2\u00a7\u00ad")
        buf.write("\3\2\2\2\u00a8\u00a9\7<\2\2\u00a9\u00aa\5\26\f\2\u00aa")
        buf.write("\u00ab\5@!\2\u00ab\u00ad\3\2\2\2\u00ac\u009c\3\2\2\2\u00ac")
        buf.write("\u00a8\3\2\2\2\u00ad\25\3\2\2\2\u00ae\u00af\5\30\r\2\u00af")
        buf.write("\u00b0\7\64\2\2\u00b0\u00b1\5\26\f\2\u00b1\u00b4\3\2\2")
        buf.write("\2\u00b2\u00b4\3\2\2\2\u00b3\u00ae\3\2\2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b4\27\3\2\2\2\u00b5\u00b6\5\22\n\2\u00b6\31")
        buf.write("\3\2\2\2\u00b7\u00bb\5\34\17\2\u00b8\u00bb\5 \21\2\u00b9")
        buf.write("\u00bb\5\"\22\2\u00ba\u00b7\3\2\2\2\u00ba\u00b8\3\2\2")
        buf.write("\2\u00ba\u00b9\3\2\2\2\u00bb\33\3\2\2\2\u00bc\u00bd\t")
        buf.write("\2\2\2\u00bd\35\3\2\2\2\u00be\u00bf\7\26\2\2\u00bf\37")
        buf.write("\3\2\2\2\u00c0\u00c1\5\34\17\2\u00c1\u00c2\7.\2\2\u00c2")
        buf.write("\u00c3\78\2\2\u00c3\u00c4\7/\2\2\u00c4!\3\2\2\2\u00c5")
        buf.write("\u00c6\7<\2\2\u00c6#\3\2\2\2\u00c7\u00c8\5&\24\2\u00c8")
        buf.write("\u00c9\t\3\2\2\u00c9\u00ca\5&\24\2\u00ca\u00cd\3\2\2\2")
        buf.write("\u00cb\u00cd\5&\24\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3")
        buf.write("\2\2\2\u00cd%\3\2\2\2\u00ce\u00cf\5(\25\2\u00cf\u00d0")
        buf.write("\t\4\2\2\u00d0\u00d1\5(\25\2\u00d1\u00d4\3\2\2\2\u00d2")
        buf.write("\u00d4\5(\25\2\u00d3\u00ce\3\2\2\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d4\'\3\2\2\2\u00d5\u00d6\b\25\1\2\u00d6\u00d7\5*\26")
        buf.write("\2\u00d7\u00dd\3\2\2\2\u00d8\u00d9\f\4\2\2\u00d9\u00da")
        buf.write("\t\5\2\2\u00da\u00dc\5*\26\2\u00db\u00d8\3\2\2\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de)\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\b\26\1")
        buf.write("\2\u00e1\u00e2\5,\27\2\u00e2\u00e8\3\2\2\2\u00e3\u00e4")
        buf.write("\f\4\2\2\u00e4\u00e5\t\6\2\2\u00e5\u00e7\5,\27\2\u00e6")
        buf.write("\u00e3\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9+\3\2\2\2\u00ea\u00e8\3\2\2")
        buf.write("\2\u00eb\u00ec\b\27\1\2\u00ec\u00ed\5.\30\2\u00ed\u00f3")
        buf.write("\3\2\2\2\u00ee\u00ef\f\4\2\2\u00ef\u00f0\t\7\2\2\u00f0")
        buf.write("\u00f2\5.\30\2\u00f1\u00ee\3\2\2\2\u00f2\u00f5\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4-\3\2\2")
        buf.write("\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\b\30\1\2\u00f7\u00f8")
        buf.write("\5\60\31\2\u00f8\u00fe\3\2\2\2\u00f9\u00fa\f\4\2\2\u00fa")
        buf.write("\u00fb\7,\2\2\u00fb\u00fd\5\60\31\2\u00fc\u00f9\3\2\2")
        buf.write("\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff/\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102")
        buf.write("\7+\2\2\u0102\u0105\5\60\31\2\u0103\u0105\5\62\32\2\u0104")
        buf.write("\u0101\3\2\2\2\u0104\u0103\3\2\2\2\u0105\61\3\2\2\2\u0106")
        buf.write("\u0107\t\6\2\2\u0107\u010a\5\62\32\2\u0108\u010a\5\64")
        buf.write("\33\2\u0109\u0106\3\2\2\2\u0109\u0108\3\2\2\2\u010a\63")
        buf.write("\3\2\2\2\u010b\u010c\5\66\34\2\u010c\u010d\7.\2\2\u010d")
        buf.write("\u010e\5$\23\2\u010e\u010f\7/\2\2\u010f\u0112\3\2\2\2")
        buf.write("\u0110\u0112\5\66\34\2\u0111\u010b\3\2\2\2\u0111\u0110")
        buf.write("\3\2\2\2\u0112\65\3\2\2\2\u0113\u0114\b\34\1\2\u0114\u0115")
        buf.write("\7<\2\2\u0115\u0116\7\66\2\2\u0116\u011c\7<\2\2\u0117")
        buf.write("\u0119\7\62\2\2\u0118\u011a\5<\37\2\u0119\u0118\3\2\2")
        buf.write("\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d")
        buf.write("\7\63\2\2\u011c\u0117\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\u012a\3\2\2\2\u011e\u011f\f\4\2\2\u011f\u0120\7\66\2")
        buf.write("\2\u0120\u0126\7<\2\2\u0121\u0123\7\62\2\2\u0122\u0124")
        buf.write("\5<\37\2\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125\u0127\7\63\2\2\u0126\u0121\3\2\2")
        buf.write("\2\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u011e")
        buf.write("\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012b\67\3\2\2\2\u012c\u012a\3\2\2\2\u012d")
        buf.write("\u012e\7\17\2\2\u012e\u012f\7<\2\2\u012f\u0131\7\62\2")
        buf.write("\2\u0130\u0132\5<\37\2\u0131\u0130\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\7\63\2\2\u0134")
        buf.write("\u0136\58\35\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u01369\3\2\2\2\u0137\u0138\7\62\2\2\u0138\u0139\5$\23")
        buf.write("\2\u0139\u013a\7\63\2\2\u013a\u0140\3\2\2\2\u013b\u0140")
        buf.write("\7<\2\2\u013c\u0140\5R*\2\u013d\u0140\7\30\2\2\u013e\u0140")
        buf.write("\7\27\2\2\u013f\u0137\3\2\2\2\u013f\u013b\3\2\2\2\u013f")
        buf.write("\u013c\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140;\3\2\2\2\u0141\u0142\5$\23\2\u0142\u0143\7\67\2")
        buf.write("\2\u0143\u0144\5<\37\2\u0144\u0149\3\2\2\2\u0145\u0146")
        buf.write("\5$\23\2\u0146\u0147\7\67\2\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u0141\3\2\2\2\u0148\u0145\3\2\2\2\u0149=\3\2\2\2\u014a")
        buf.write("\u0152\5@!\2\u014b\u0152\5D#\2\u014c\u0152\5F$\2\u014d")
        buf.write("\u0152\5H%\2\u014e\u0152\5J&\2\u014f\u0152\5L\'\2\u0150")
        buf.write("\u0152\5N(\2\u0151\u014a\3\2\2\2\u0151\u014b\3\2\2\2\u0151")
        buf.write("\u014c\3\2\2\2\u0151\u014d\3\2\2\2\u0151\u014e\3\2\2\2")
        buf.write("\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152?\3\2\2")
        buf.write("\2\u0153\u0155\7\60\2\2\u0154\u0156\5B\"\2\u0155\u0154")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0158\7\61\2\2\u0158A\3\2\2\2\u0159\u015b\7\31\2\2\u015a")
        buf.write("\u0159\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015e\5\n\6\2\u015d\u015a\3\2\2\2\u015e\u0161\3")
        buf.write("\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0165")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0164\5> \2\u0163\u0162")
        buf.write("\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166C\3\2\2\2\u0167\u0165\3\2\2\2\u0168")
        buf.write("\u016b\7<\2\2\u0169\u016b\5\64\33\2\u016a\u0168\3\2\2")
        buf.write("\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d")
        buf.write("\7-\2\2\u016d\u016e\5$\23\2\u016e\u016f\7\64\2\2\u016f")
        buf.write("E\3\2\2\2\u0170\u0171\7\r\2\2\u0171\u0172\5$\23\2\u0172")
        buf.write("\u0173\7\21\2\2\u0173\u0176\5> \2\u0174\u0175\7\n\2\2")
        buf.write("\u0175\u0177\5> \2\u0176\u0174\3\2\2\2\u0176\u0177\3\2")
        buf.write("\2\2\u0177G\3\2\2\2\u0178\u0179\7\22\2\2\u0179\u017a\7")
        buf.write("<\2\2\u017a\u017b\7-\2\2\u017b\u017c\5$\23\2\u017c\u017d")
        buf.write("\t\b\2\2\u017d\u017e\5$\23\2\u017e\u017f\7\t\2\2\u017f")
        buf.write("\u0180\5> \2\u0180I\3\2\2\2\u0181\u0182\7\6\2\2\u0182")
        buf.write("\u0183\7\64\2\2\u0183K\3\2\2\2\u0184\u0185\7\b\2\2\u0185")
        buf.write("\u0186\7\64\2\2\u0186M\3\2\2\2\u0187\u0188\7\23\2\2\u0188")
        buf.write("\u0189\5$\23\2\u0189\u018a\7\64\2\2\u018aO\3\2\2\2\u018b")
        buf.write("\u018e\7<\2\2\u018c\u018e\5$\23\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7")
        buf.write("\66\2\2\u0190\u0191\7<\2\2\u0191\u0192\7\62\2\2\u0192")
        buf.write("\u0193\5<\37\2\u0193\u0194\7\63\2\2\u0194\u0195\7\64\2")
        buf.write("\2\u0195Q\3\2\2\2\u0196\u019c\78\2\2\u0197\u019c\79\2")
        buf.write("\2\u0198\u019c\7:\2\2\u0199\u019c\7;\2\2\u019a\u019c\5")
        buf.write("T+\2\u019b\u0196\3\2\2\2\u019b\u0197\3\2\2\2\u019b\u0198")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("S\3\2\2\2\u019d\u019e\7\60\2\2\u019e\u019f\5V,\2\u019f")
        buf.write("\u01a0\7\61\2\2\u01a0U\3\2\2\2\u01a1\u01a2\5X-\2\u01a2")
        buf.write("\u01a3\7\67\2\2\u01a3\u01a4\5V,\2\u01a4\u01a7\3\2\2\2")
        buf.write("\u01a5\u01a7\5X-\2\u01a6\u01a1\3\2\2\2\u01a6\u01a5\3\2")
        buf.write("\2\2\u01a7W\3\2\2\2\u01a8\u01a9\t\t\2\2\u01a9Y\3\2\2\2")
        buf.write(",]fls{\u0081\u0090\u0097\u0099\u009c\u00a0\u00ac\u00b3")
        buf.write("\u00ba\u00cc\u00d3\u00dd\u00e8\u00f3\u00fe\u0104\u0109")
        buf.write("\u0111\u0119\u011c\u0123\u0126\u012a\u0131\u0135\u013f")
        buf.write("\u0148\u0151\u0155\u015a\u015f\u0165\u016a\u0176\u018d")
        buf.write("\u019b\u01a6")
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
                      "LP", "RP", "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", 
                      "INT_LIT", "BOOL_LIT", "FLOAT_LIT", "STR_LIT", "ID", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", 
                      "WS" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_member = 2
    RULE_attribute_decl = 3
    RULE_var_decl = 4
    RULE_immutable_attribute = 5
    RULE_mutable_attribute = 6
    RULE_attribute = 7
    RULE_idlist = 8
    RULE_method_decl = 9
    RULE_paralist = 10
    RULE_para_decl = 11
    RULE_data_type = 12
    RULE_not_void_type = 13
    RULE_void_type = 14
    RULE_arr_type = 15
    RULE_class_type = 16
    RULE_expr = 17
    RULE_expr1 = 18
    RULE_expr2 = 19
    RULE_expr3 = 20
    RULE_expr4 = 21
    RULE_expr5 = 22
    RULE_expr6 = 23
    RULE_expr7 = 24
    RULE_expr8 = 25
    RULE_expr9 = 26
    RULE_expr10 = 27
    RULE_expr11 = 28
    RULE_exprlist = 29
    RULE_stmt = 30
    RULE_block_stmt = 31
    RULE_mem_stmt = 32
    RULE_assignment_decl = 33
    RULE_if_stmt = 34
    RULE_for_stmt = 35
    RULE_break_stmt = 36
    RULE_continue_stmt = 37
    RULE_return_stmt = 38
    RULE_method_invocation_stmt = 39
    RULE_literal = 40
    RULE_arr_lit = 41
    RULE_arr_decl = 42
    RULE_arr_val = 43

    ruleNames =  [ "program", "class_decl", "member", "attribute_decl", 
                   "var_decl", "immutable_attribute", "mutable_attribute", 
                   "attribute", "idlist", "method_decl", "paralist", "para_decl", 
                   "data_type", "not_void_type", "void_type", "arr_type", 
                   "class_type", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "exprlist", "stmt", "block_stmt", "mem_stmt", 
                   "assignment_decl", "if_stmt", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "method_invocation_stmt", 
                   "literal", "arr_lit", "arr_decl", "arr_val" ]

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
    SEMI=50
    COLON=51
    DOT=52
    COMMA=53
    INT_LIT=54
    BOOL_LIT=55
    FLOAT_LIT=56
    STR_LIT=57
    ID=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61
    WS=62

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

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


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
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 88
                self.class_decl()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MemberContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MemberContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKOOLParser.CLASS)
            self.state = 97
            self.match(BKOOLParser.ID)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 98
                self.match(BKOOLParser.EXTENDS)
                self.state = 99
                self.match(BKOOLParser.ID)


            self.state = 102
            self.match(BKOOLParser.LP)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 103
                self.member()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = BKOOLParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(BKOOLParser.STATIC)

            elif la_ == 2:
                self.state = 116
                self.match(BKOOLParser.FINAL)

            elif la_ == 3:
                self.state = 117
                self.match(BKOOLParser.STATIC)
                self.state = 118
                self.match(BKOOLParser.FINAL)

            elif la_ == 4:
                self.state = 119
                self.match(BKOOLParser.FINAL)
                self.state = 120
                self.match(BKOOLParser.STATIC)


            self.state = 123
            self.var_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def immutable_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Immutable_attributeContext,0)


        def mutable_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Mutable_attributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 125
                self.immutable_attribute()
                pass

            elif la_ == 2:
                self.state = 126
                self.mutable_attribute()
                pass


            self.state = 129
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Immutable_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immutable_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutable_attribute" ):
                return visitor.visitImmutable_attribute(self)
            else:
                return visitor.visitChildren(self)




    def immutable_attribute(self):

        localctx = BKOOLParser.Immutable_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immutable_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.data_type()
            self.state = 132
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mutable_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mutable_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable_attribute" ):
                return visitor.visitMutable_attribute(self)
            else:
                return visitor.visitChildren(self)




    def mutable_attribute(self):

        localctx = BKOOLParser.Mutable_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mutable_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.data_type()
            self.state = 135
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(BKOOLParser.ID)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 140
                    self.match(BKOOLParser.EQUAL)
                    self.state = 141
                    self.expr()


                self.state = 144
                self.match(BKOOLParser.COMMA)
                self.state = 145
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(BKOOLParser.ID)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 147
                    self.match(BKOOLParser.EQUAL)
                    self.state = 148
                    self.expr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paralist(self):
            return self.getTypedRuleContext(BKOOLParser.ParalistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def void_type(self):
            return self.getTypedRuleContext(BKOOLParser.Void_typeContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 153
                    self.match(BKOOLParser.STATIC)


                self.state = 158
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                    self.state = 156
                    self.data_type()
                    pass
                elif token in [BKOOLParser.VOID]:
                    self.state = 157
                    self.void_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 160
                self.match(BKOOLParser.ID)
                self.state = 161
                self.match(BKOOLParser.LB)
                self.state = 162
                self.paralist()
                self.state = 163
                self.match(BKOOLParser.RB)
                self.state = 164
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(BKOOLParser.ID)
                self.state = 167
                self.paralist()
                self.state = 168
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Para_declContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paralist(self):
            return self.getTypedRuleContext(BKOOLParser.ParalistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = BKOOLParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paralist)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.para_decl()
                self.state = 173
                self.match(BKOOLParser.SEMI)
                self.state = 174
                self.paralist()
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Para_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_para_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_decl" ):
                return visitor.visitPara_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_decl(self):

        localctx = BKOOLParser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_para_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_void_type(self):
            return self.getTypedRuleContext(BKOOLParser.Not_void_typeContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = BKOOLParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_data_type)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.not_void_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.arr_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_void_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_not_void_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_void_type" ):
                return visitor.visitNot_void_type(self)
            else:
                return visitor.visitChildren(self)




    def not_void_type(self):

        localctx = BKOOLParser.Not_void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_not_void_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
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


    class Void_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_void_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoid_type" ):
                return visitor.visitVoid_type(self)
            else:
                return visitor.visitChildren(self)




    def void_type(self):

        localctx = BKOOLParser.Void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(BKOOLParser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_void_type(self):
            return self.getTypedRuleContext(BKOOLParser.Not_void_typeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = BKOOLParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.not_void_type()
            self.state = 191
            self.match(BKOOLParser.LSB)
            self.state = 192
            self.match(BKOOLParser.INT_LIT)
            self.state = 193
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(BKOOLParser.LESS_OR_EQUAL, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(BKOOLParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.expr1()
                self.state = 198
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.expr2(0)
                self.state = 205
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 206
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 214
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 215
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 216
                    self.expr3(0) 
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 227
                    self.expr4(0) 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def MULOP(self):
            return self.getToken(BKOOLParser.MULOP, 0)

        def FLOAT_DIV(self):
            return self.getToken(BKOOLParser.FLOAT_DIV, 0)

        def INTEGER_DIV(self):
            return self.getToken(BKOOLParser.INTEGER_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INTEGER_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.expr5(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def CONCATENATION(self):
            return self.getToken(BKOOLParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 248
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 249
                    self.expr6() 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr6)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(BKOOLParser.NOT)
                self.state = 256
                self.expr6()
                pass
            elif token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 261
                self.expr7()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.expr8()
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


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr8)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.expr9(0)
                self.state = 266
                self.match(BKOOLParser.LSB)
                self.state = 267
                self.expr()
                self.state = 268
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.expr9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(BKOOLParser.ID)
            self.state = 275
            self.match(BKOOLParser.DOT)
            self.state = 276
            self.match(BKOOLParser.ID)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 277
                self.match(BKOOLParser.LB)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 278
                    self.exprlist()


                self.state = 281
                self.match(BKOOLParser.RB)


            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
                    self.match(BKOOLParser.DOT)
                    self.state = 286
                    self.match(BKOOLParser.ID)
                    self.state = 292
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        self.state = 287
                        self.match(BKOOLParser.LB)
                        self.state = 289
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 288
                            self.exprlist()


                        self.state = 291
                        self.match(BKOOLParser.RB)

             
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKOOLParser.NEW)
            self.state = 300
            self.match(BKOOLParser.ID)
            self.state = 301
            self.match(BKOOLParser.LB)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 302
                self.exprlist()


            self.state = 305
            self.match(BKOOLParser.RB)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 306
                self.expr10()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr11)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(BKOOLParser.LB)
                self.state = 310
                self.expr()
                self.state = 311
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.match(BKOOLParser.NIL)
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


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exprlist)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.expr()
                self.state = 320
                self.match(BKOOLParser.COMMA)
                self.state = 321
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.expr()
                self.state = 324
                self.match(BKOOLParser.COMMA)
                pass


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

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def assignment_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_declContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.block_stmt()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.assignment_decl()
                pass
            elif token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.if_stmt()
                pass
            elif token in [BKOOLParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.for_stmt()
                pass
            elif token in [BKOOLParser.BREAK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 332
                self.break_stmt()
                pass
            elif token in [BKOOLParser.CONTINUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 333
                self.continue_stmt()
                pass
            elif token in [BKOOLParser.RETURN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 334
                self.return_stmt()
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


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def mem_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Mem_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BKOOLParser.LP)
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 338
                self.mem_stmt()


            self.state = 341
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def FINAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.FINAL)
            else:
                return self.getToken(BKOOLParser.FINAL, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mem_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem_stmt" ):
                return visitor.visitMem_stmt(self)
            else:
                return visitor.visitChildren(self)




    def mem_stmt(self):

        localctx = BKOOLParser.Mem_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_mem_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 344
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BKOOLParser.FINAL:
                        self.state = 343
                        self.match(BKOOLParser.FINAL)


                    self.state = 346
                    self.var_decl() 
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 352
                self.stmt()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_decl" ):
                return visitor.visitAssignment_decl(self)
            else:
                return visitor.visitChildren(self)




    def assignment_decl(self):

        localctx = BKOOLParser.Assignment_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignment_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 358
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 359
                self.expr8()
                pass


            self.state = 362
            self.match(BKOOLParser.ASSIGN)
            self.state = 363
            self.expr()
            self.state = 364
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(BKOOLParser.IF)
            self.state = 367
            self.expr()
            self.state = 368
            self.match(BKOOLParser.THEN)
            self.state = 369
            self.stmt()
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 370
                self.match(BKOOLParser.ELSE)
                self.state = 371
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(BKOOLParser.FOR)
            self.state = 375
            self.match(BKOOLParser.ID)
            self.state = 376
            self.match(BKOOLParser.ASSIGN)
            self.state = 377
            self.expr()
            self.state = 378
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 379
            self.expr()
            self.state = 380
            self.match(BKOOLParser.DO)
            self.state = 381
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(BKOOLParser.BREAK)
            self.state = 384
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(BKOOLParser.CONTINUE)
            self.state = 387
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(BKOOLParser.RETURN)
            self.state = 390
            self.expr()
            self.state = 391
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = BKOOLParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 393
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 394
                self.expr()
                pass


            self.state = 397
            self.match(BKOOLParser.DOT)
            self.state = 398
            self.match(BKOOLParser.ID)
            self.state = 399
            self.match(BKOOLParser.LB)
            self.state = 400
            self.exprlist()
            self.state = 401
            self.match(BKOOLParser.RB)
            self.state = 402
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKOOLParser.BOOL_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(BKOOLParser.STR_LIT, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_literal)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(BKOOLParser.BOOL_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.match(BKOOLParser.STR_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 408
                self.arr_lit()
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


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def arr_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_declContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = BKOOLParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(BKOOLParser.LP)
            self.state = 412
            self.arr_decl()
            self.state = 413
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_val(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_valContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def arr_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_decl" ):
                return visitor.visitArr_decl(self)
            else:
                return visitor.visitChildren(self)




    def arr_decl(self):

        localctx = BKOOLParser.Arr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arr_decl)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.arr_val()
                self.state = 416
                self.match(BKOOLParser.COMMA)
                self.state = 417
                self.arr_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.arr_val()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKOOLParser.BOOL_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(BKOOLParser.STR_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_val" ):
                return visitor.visitArr_val(self)
            else:
                return visitor.visitChildren(self)




    def arr_val(self):

        localctx = BKOOLParser.Arr_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arr_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STR_LIT))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expr2_sempred
        self._predicates[20] = self.expr3_sempred
        self._predicates[21] = self.expr4_sempred
        self._predicates[22] = self.expr5_sempred
        self._predicates[26] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




