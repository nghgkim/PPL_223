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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01b7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\6\2")
        buf.write("\\\n\2\r\2\16\2]\3\2\3\2\3\3\3\3\3\3\3\3\5\3f\n\3\3\3")
        buf.write("\3\3\7\3j\n\3\f\3\16\3m\13\3\3\3\3\3\3\4\3\4\5\4s\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5{\n\5\3\5\3\5\3\6\3\6\5\6")
        buf.write("\u0081\n\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\5\t\u008e\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0098")
        buf.write("\n\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a0\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00a7\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u00ae")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00b6\n\f\f\f\16\f\u00b9")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c1\n\r\f\r\16\r\u00c4")
        buf.write("\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00cc\n\16\f")
        buf.write("\16\16\16\u00cf\13\16\3\17\3\17\3\17\3\17\3\17\3\17\7")
        buf.write("\17\u00d7\n\17\f\17\16\17\u00da\13\17\3\20\3\20\3\20\5")
        buf.write("\20\u00df\n\20\3\21\3\21\3\21\5\21\u00e4\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00ec\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\5\23\u00f4\n\23\3\23\5\23\u00f7\n\23\3\23")
        buf.write("\5\23\u00fa\n\23\3\23\3\23\3\23\3\23\3\23\5\23\u0101\n")
        buf.write("\23\3\23\5\23\u0104\n\23\7\23\u0106\n\23\f\23\16\23\u0109")
        buf.write("\13\23\3\24\3\24\3\24\3\24\5\24\u010f\n\24\3\24\3\24\5")
        buf.write("\24\u0113\n\24\3\24\5\24\u0116\n\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0120\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u0129\n\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0133\n\27\3\30\3\30\5\30\u0137")
        buf.write("\n\30\3\30\3\30\3\31\5\31\u013c\n\31\3\31\7\31\u013f\n")
        buf.write("\31\f\31\16\31\u0142\13\31\3\31\6\31\u0145\n\31\r\31\16")
        buf.write("\31\u0146\3\32\3\32\5\32\u014b\n\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0157\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \5 \u016e\n ")
        buf.write("\3 \3 \3 \3 \5 \u0174\n \3 \3 \3!\3!\3!\3\"\3\"\3\"\5")
        buf.write("\"\u017e\n\"\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u018c")
        buf.write("\n%\3&\3&\3\'\3\'\3(\3(\3(\3(\3(\5(\u0197\n(\3)\3)\3*")
        buf.write("\3*\3*\5*\u019e\n*\3*\3*\3*\3*\3*\5*\u01a5\n*\5*\u01a7")
        buf.write("\n*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\5-\u01b5\n-\3")
        buf.write("-\2\7\26\30\32\34$.\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\t\3\2#&\3")
        buf.write("\2!\"\3\2\'(\3\2\33\34\3\2\35 \3\2\31\32\6\2\5\5\f\f\16")
        buf.write("\16\20\20\2\u01c8\2[\3\2\2\2\4a\3\2\2\2\6r\3\2\2\2\bz")
        buf.write("\3\2\2\2\n\u0080\3\2\2\2\f\u0084\3\2\2\2\16\u0087\3\2")
        buf.write("\2\2\20\u009f\3\2\2\2\22\u00a6\3\2\2\2\24\u00ad\3\2\2")
        buf.write("\2\26\u00af\3\2\2\2\30\u00ba\3\2\2\2\32\u00c5\3\2\2\2")
        buf.write("\34\u00d0\3\2\2\2\36\u00de\3\2\2\2 \u00e3\3\2\2\2\"\u00eb")
        buf.write("\3\2\2\2$\u00f9\3\2\2\2&\u0115\3\2\2\2(\u011f\3\2\2\2")
        buf.write("*\u0128\3\2\2\2,\u0132\3\2\2\2.\u0134\3\2\2\2\60\u0140")
        buf.write("\3\2\2\2\62\u014a\3\2\2\2\64\u0150\3\2\2\2\66\u0158\3")
        buf.write("\2\2\28\u0161\3\2\2\2:\u0164\3\2\2\2<\u0167\3\2\2\2>\u016d")
        buf.write("\3\2\2\2@\u0177\3\2\2\2B\u017d\3\2\2\2D\u017f\3\2\2\2")
        buf.write("F\u0181\3\2\2\2H\u018b\3\2\2\2J\u018d\3\2\2\2L\u018f\3")
        buf.write("\2\2\2N\u0196\3\2\2\2P\u0198\3\2\2\2R\u01a6\3\2\2\2T\u01a8")
        buf.write("\3\2\2\2V\u01ac\3\2\2\2X\u01b4\3\2\2\2Z\\\5\4\3\2[Z\3")
        buf.write("\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\7\2")
        buf.write("\2\3`\3\3\2\2\2ab\7\7\2\2be\7<\2\2cd\7\13\2\2df\7<\2\2")
        buf.write("ec\3\2\2\2ef\3\2\2\2fg\3\2\2\2gk\7\60\2\2hj\5\6\4\2ih")
        buf.write("\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2")
        buf.write("\2\2no\7\61\2\2o\5\3\2\2\2ps\5\b\5\2qs\5\20\t\2rp\3\2")
        buf.write("\2\2rq\3\2\2\2s\7\3\2\2\2t{\7\30\2\2u{\7\27\2\2vw\7\27")
        buf.write("\2\2w{\7\30\2\2xy\7\30\2\2y{\7\27\2\2zt\3\2\2\2zu\3\2")
        buf.write("\2\2zv\3\2\2\2zx\3\2\2\2z{\3\2\2\2{|\3\2\2\2|}\5\n\6\2")
        buf.write("}\t\3\2\2\2~\u0081\5\f\7\2\177\u0081\5\16\b\2\u0080~\3")
        buf.write("\2\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083")
        buf.write("\7\64\2\2\u0083\13\3\2\2\2\u0084\u0085\5B\"\2\u0085\u0086")
        buf.write("\5L\'\2\u0086\r\3\2\2\2\u0087\u0088\5B\"\2\u0088\u0089")
        buf.write("\5L\'\2\u0089\17\3\2\2\2\u008a\u008d\7\30\2\2\u008b\u008e")
        buf.write("\5B\"\2\u008c\u008e\7\24\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\7<\2\2")
        buf.write("\u0090\u0091\7\62\2\2\u0091\u0092\5N(\2\u0092\u0093\7")
        buf.write("\63\2\2\u0093\u0094\5.\30\2\u0094\u00a0\3\2\2\2\u0095")
        buf.write("\u0098\5B\"\2\u0096\u0098\7\24\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3")
        buf.write("\2\2\2\u0099\u009a\7<\2\2\u009a\u009b\7\62\2\2\u009b\u009c")
        buf.write("\5N(\2\u009c\u009d\7\63\2\2\u009d\u009e\5.\30\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u008a\3\2\2\2\u009f\u0097\3\2\2\2")
        buf.write("\u00a0\21\3\2\2\2\u00a1\u00a2\5\24\13\2\u00a2\u00a3\t")
        buf.write("\2\2\2\u00a3\u00a4\5\24\13\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a7\5\24\13\2\u00a6\u00a1\3\2\2\2\u00a6\u00a5\3\2\2")
        buf.write("\2\u00a7\23\3\2\2\2\u00a8\u00a9\5\26\f\2\u00a9\u00aa\t")
        buf.write("\3\2\2\u00aa\u00ab\5\26\f\2\u00ab\u00ae\3\2\2\2\u00ac")
        buf.write("\u00ae\5\26\f\2\u00ad\u00a8\3\2\2\2\u00ad\u00ac\3\2\2")
        buf.write("\2\u00ae\25\3\2\2\2\u00af\u00b0\b\f\1\2\u00b0\u00b1\5")
        buf.write("\30\r\2\u00b1\u00b7\3\2\2\2\u00b2\u00b3\f\4\2\2\u00b3")
        buf.write("\u00b4\t\4\2\2\u00b4\u00b6\5\30\r\2\u00b5\u00b2\3\2\2")
        buf.write("\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\27\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb")
        buf.write("\b\r\1\2\u00bb\u00bc\5\32\16\2\u00bc\u00c2\3\2\2\2\u00bd")
        buf.write("\u00be\f\4\2\2\u00be\u00bf\t\5\2\2\u00bf\u00c1\5\32\16")
        buf.write("\2\u00c0\u00bd\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\31\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c5\u00c6\b\16\1\2\u00c6\u00c7\5\34\17\2\u00c7")
        buf.write("\u00cd\3\2\2\2\u00c8\u00c9\f\4\2\2\u00c9\u00ca\t\6\2\2")
        buf.write("\u00ca\u00cc\5\34\17\2\u00cb\u00c8\3\2\2\2\u00cc\u00cf")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\33\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\b\17\1\2\u00d1")
        buf.write("\u00d2\5\36\20\2\u00d2\u00d8\3\2\2\2\u00d3\u00d4\f\4\2")
        buf.write("\2\u00d4\u00d5\7*\2\2\u00d5\u00d7\5\36\20\2\u00d6\u00d3")
        buf.write("\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\35\3\2\2\2\u00da\u00d8\3\2\2\2\u00db")
        buf.write("\u00dc\7)\2\2\u00dc\u00df\5\36\20\2\u00dd\u00df\5 \21")
        buf.write("\2\u00de\u00db\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\37\3")
        buf.write("\2\2\2\u00e0\u00e1\t\5\2\2\u00e1\u00e4\5 \21\2\u00e2\u00e4")
        buf.write("\5\"\22\2\u00e3\u00e0\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write("!\3\2\2\2\u00e5\u00e6\5$\23\2\u00e6\u00e7\7.\2\2\u00e7")
        buf.write("\u00e8\5\22\n\2\u00e8\u00e9\7/\2\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00ec\5$\23\2\u00eb\u00e5\3\2\2\2\u00eb\u00ea\3")
        buf.write("\2\2\2\u00ec#\3\2\2\2\u00ed\u00ee\b\23\1\2\u00ee\u00ef")
        buf.write("\7<\2\2\u00ef\u00f0\7\66\2\2\u00f0\u00f6\7<\2\2\u00f1")
        buf.write("\u00f3\7\62\2\2\u00f2\u00f4\5*\26\2\u00f3\u00f2\3\2\2")
        buf.write("\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7")
        buf.write("\7\63\2\2\u00f6\u00f1\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00fa\5&\24\2\u00f9\u00ed\3\2\2\2")
        buf.write("\u00f9\u00f8\3\2\2\2\u00fa\u0107\3\2\2\2\u00fb\u00fc\f")
        buf.write("\5\2\2\u00fc\u00fd\7\66\2\2\u00fd\u0103\7<\2\2\u00fe\u0100")
        buf.write("\7\62\2\2\u00ff\u0101\5*\26\2\u0100\u00ff\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0104\7\63\2")
        buf.write("\2\u0103\u00fe\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106")
        buf.write("\3\2\2\2\u0105\u00fb\3\2\2\2\u0106\u0109\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108%\3\2\2\2\u0109")
        buf.write("\u0107\3\2\2\2\u010a\u010b\7\17\2\2\u010b\u010c\7<\2\2")
        buf.write("\u010c\u010e\7\62\2\2\u010d\u010f\5*\26\2\u010e\u010d")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0112\7\63\2\2\u0111\u0113\5&\24\2\u0112\u0111\3\2\2")
        buf.write("\2\u0112\u0113\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0116")
        buf.write("\5(\25\2\u0115\u010a\3\2\2\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\'\3\2\2\2\u0117\u0118\7\62\2\2\u0118\u0119\5\22\n\2\u0119")
        buf.write("\u011a\7\63\2\2\u011a\u0120\3\2\2\2\u011b\u0120\7<\2\2")
        buf.write("\u011c\u0120\5H%\2\u011d\u0120\7\26\2\2\u011e\u0120\7")
        buf.write("\25\2\2\u011f\u0117\3\2\2\2\u011f\u011b\3\2\2\2\u011f")
        buf.write("\u011c\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2")
        buf.write("\u0120)\3\2\2\2\u0121\u0122\5\22\n\2\u0122\u0123\7\67")
        buf.write("\2\2\u0123\u0124\5*\26\2\u0124\u0129\3\2\2\2\u0125\u0126")
        buf.write("\5\22\n\2\u0126\u0127\7\67\2\2\u0127\u0129\3\2\2\2\u0128")
        buf.write("\u0121\3\2\2\2\u0128\u0125\3\2\2\2\u0129+\3\2\2\2\u012a")
        buf.write("\u0133\5\62\32\2\u012b\u0133\5\64\33\2\u012c\u0133\5\66")
        buf.write("\34\2\u012d\u0133\58\35\2\u012e\u0133\5:\36\2\u012f\u0133")
        buf.write("\5<\37\2\u0130\u0133\5@!\2\u0131\u0133\5.\30\2\u0132\u012a")
        buf.write("\3\2\2\2\u0132\u012b\3\2\2\2\u0132\u012c\3\2\2\2\u0132")
        buf.write("\u012d\3\2\2\2\u0132\u012e\3\2\2\2\u0132\u012f\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133-\3\2\2")
        buf.write("\2\u0134\u0136\7\60\2\2\u0135\u0137\5\60\31\2\u0136\u0135")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0139\7\61\2\2\u0139/\3\2\2\2\u013a\u013c\7\27\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013f\5\n\6\2\u013e\u013b\3\2\2\2\u013f\u0142\3")
        buf.write("\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0144")
        buf.write("\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0145\5,\27\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147\61\3\2\2\2\u0148\u014b\7<\2")
        buf.write("\2\u0149\u014b\5\"\22\2\u014a\u0148\3\2\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\7,\2\2\u014d")
        buf.write("\u014e\5\22\n\2\u014e\u014f\7\64\2\2\u014f\63\3\2\2\2")
        buf.write("\u0150\u0151\7\r\2\2\u0151\u0152\5\22\n\2\u0152\u0153")
        buf.write("\7\21\2\2\u0153\u0156\5,\27\2\u0154\u0155\7\n\2\2\u0155")
        buf.write("\u0157\5,\27\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\65\3\2\2\2\u0158\u0159\7\22\2\2\u0159\u015a\7<")
        buf.write("\2\2\u015a\u015b\7,\2\2\u015b\u015c\5\22\n\2\u015c\u015d")
        buf.write("\t\7\2\2\u015d\u015e\5\22\n\2\u015e\u015f\7\t\2\2\u015f")
        buf.write("\u0160\5,\27\2\u0160\67\3\2\2\2\u0161\u0162\7\6\2\2\u0162")
        buf.write("\u0163\7\64\2\2\u01639\3\2\2\2\u0164\u0165\7\b\2\2\u0165")
        buf.write("\u0166\7\64\2\2\u0166;\3\2\2\2\u0167\u0168\7\23\2\2\u0168")
        buf.write("\u0169\5\22\n\2\u0169\u016a\7\64\2\2\u016a=\3\2\2\2\u016b")
        buf.write("\u016e\7<\2\2\u016c\u016e\5\22\n\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\7")
        buf.write("\66\2\2\u0170\u0171\7<\2\2\u0171\u0173\7\62\2\2\u0172")
        buf.write("\u0174\5*\26\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175\u0176\7\63\2\2\u0176?\3\2\2")
        buf.write("\2\u0177\u0178\5> \2\u0178\u0179\7\64\2\2\u0179A\3\2\2")
        buf.write("\2\u017a\u017e\5D#\2\u017b\u017e\5F$\2\u017c\u017e\5J")
        buf.write("&\2\u017d\u017a\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017eC\3\2\2\2\u017f\u0180\t\b\2\2\u0180E\3\2")
        buf.write("\2\2\u0181\u0182\5D#\2\u0182\u0183\7.\2\2\u0183\u0184")
        buf.write("\7;\2\2\u0184\u0185\7/\2\2\u0185G\3\2\2\2\u0186\u018c")
        buf.write("\5T+\2\u0187\u018c\7;\2\2\u0188\u018c\7:\2\2\u0189\u018c")
        buf.write("\78\2\2\u018a\u018c\79\2\2\u018b\u0186\3\2\2\2\u018b\u0187")
        buf.write("\3\2\2\2\u018b\u0188\3\2\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018cI\3\2\2\2\u018d\u018e\7<\2\2\u018e")
        buf.write("K\3\2\2\2\u018f\u0190\5R*\2\u0190M\3\2\2\2\u0191\u0192")
        buf.write("\5P)\2\u0192\u0193\7\64\2\2\u0193\u0194\5N(\2\u0194\u0197")
        buf.write("\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0191\3\2\2\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197O\3\2\2\2\u0198\u0199\5R*\2\u0199")
        buf.write("Q\3\2\2\2\u019a\u019d\7<\2\2\u019b\u019c\7\"\2\2\u019c")
        buf.write("\u019e\5\22\n\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2")
        buf.write("\2\u019e\u019f\3\2\2\2\u019f\u01a0\7\67\2\2\u01a0\u01a7")
        buf.write("\5R*\2\u01a1\u01a4\7<\2\2\u01a2\u01a3\7\"\2\2\u01a3\u01a5")
        buf.write("\5\22\n\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a7\3\2\2\2\u01a6\u019a\3\2\2\2\u01a6\u01a1\3\2\2\2")
        buf.write("\u01a7S\3\2\2\2\u01a8\u01a9\7\60\2\2\u01a9\u01aa\5V,\2")
        buf.write("\u01aa\u01ab\7\61\2\2\u01abU\3\2\2\2\u01ac\u01ad\5\22")
        buf.write("\n\2\u01ad\u01ae\5X-\2\u01aeW\3\2\2\2\u01af\u01b0\7\67")
        buf.write("\2\2\u01b0\u01b1\5\22\n\2\u01b1\u01b2\5X-\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01af\3\2\2\2\u01b4")
        buf.write("\u01b3\3\2\2\2\u01b5Y\3\2\2\2/]ekrz\u0080\u008d\u0097")
        buf.write("\u009f\u00a6\u00ad\u00b7\u00c2\u00cd\u00d8\u00de\u00e3")
        buf.write("\u00eb\u00f3\u00f6\u00f9\u0100\u0103\u0107\u010e\u0112")
        buf.write("\u0115\u011f\u0128\u0132\u0136\u013b\u0140\u0146\u014a")
        buf.write("\u0156\u016d\u0173\u017d\u018b\u0196\u019d\u01a4\u01a6")
        buf.write("\u01b4")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'boolean'", 
                     "'break'", "'class'", "'continue'", "'do'", "'else'", 
                     "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
                     "'then'", "'for'", "'return'", "'void'", "'nil'", "'this'", 
                     "'final'", "'static'", "'to'", "'downto'", "'+'", "'-'", 
                     "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
                     "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", 
                     "<INVALID>", "':='", "'='", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMAT", "BLOCK_COMMAT", "BOOLEAN", 
                      "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
                      "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", 
                      "RETURN", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                      "TO", "DOWNTO", "ADD", "SUB", "MUL", "DIV", "INT_DIV", 
                      "MOD", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", 
                      "OR", "AND", "NOT", "CONCATENATION", "NEW_OP", "ASSINGMENT", 
                      "ASSIGN", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", 
                      "CL", "DOT", "COMMA", "BOOLLIT", "STRINGLIT", "FLOATLIT", 
                      "INTLIT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "WS", "NEWLINE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declare = 1
    RULE_members = 2
    RULE_attribute_declare = 3
    RULE_var_decl = 4
    RULE_immutable_attribute = 5
    RULE_mutable_attribute = 6
    RULE_method_declare = 7
    RULE_expr = 8
    RULE_expr1 = 9
    RULE_expr2 = 10
    RULE_expr3 = 11
    RULE_expr4 = 12
    RULE_expr5 = 13
    RULE_expr6 = 14
    RULE_expr7 = 15
    RULE_expr8 = 16
    RULE_expr9 = 17
    RULE_expr10 = 18
    RULE_expr11 = 19
    RULE_exprlist = 20
    RULE_statement = 21
    RULE_block_statement = 22
    RULE_member_block = 23
    RULE_assignment_statement = 24
    RULE_if_statement = 25
    RULE_for_statement = 26
    RULE_break_statement = 27
    RULE_continue_statement = 28
    RULE_return_statement = 29
    RULE_member_access = 30
    RULE_method_invocation_statement = 31
    RULE_data_type = 32
    RULE_type_not_void = 33
    RULE_array_type = 34
    RULE_literal = 35
    RULE_class_type = 36
    RULE_attribute = 37
    RULE_paralist = 38
    RULE_para_decl = 39
    RULE_idlist = 40
    RULE_array_lit = 41
    RULE_array_declare = 42
    RULE_array_list = 43

    ruleNames =  [ "program", "class_declare", "members", "attribute_declare", 
                   "var_decl", "immutable_attribute", "mutable_attribute", 
                   "method_declare", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "expr11", "exprlist", "statement", "block_statement", 
                   "member_block", "assignment_statement", "if_statement", 
                   "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "member_access", "method_invocation_statement", 
                   "data_type", "type_not_void", "array_type", "literal", 
                   "class_type", "attribute", "paralist", "para_decl", "idlist", 
                   "array_lit", "array_declare", "array_list" ]

    EOF = Token.EOF
    LINE_COMMAT=1
    BLOCK_COMMAT=2
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
    VOID=18
    NIL=19
    THIS=20
    FINAL=21
    STATIC=22
    TO=23
    DOWNTO=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    INT_DIV=29
    MOD=30
    NOT_EQUAL=31
    EQUAL=32
    LT=33
    GT=34
    LE=35
    GE=36
    OR=37
    AND=38
    NOT=39
    CONCATENATION=40
    NEW_OP=41
    ASSINGMENT=42
    ASSIGN=43
    LSB=44
    RSB=45
    LP=46
    RP=47
    LB=48
    RB=49
    SEMI=50
    CL=51
    DOT=52
    COMMA=53
    BOOLLIT=54
    STRINGLIT=55
    FLOATLIT=56
    INTLIT=57
    ID=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    WS=61
    NEWLINE=62
    ERROR_CHAR=63

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

        def class_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declareContext,i)


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
            self.state = 89 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self.class_declare()
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 93
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
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

        def members(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MembersContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MembersContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = BKOOLParser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(BKOOLParser.CLASS)
            self.state = 96
            self.match(BKOOLParser.ID)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 97
                self.match(BKOOLParser.EXTENDS)
                self.state = 98
                self.match(BKOOLParser.ID)


            self.state = 101
            self.match(BKOOLParser.LP)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 102
                self.members()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = BKOOLParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_members)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 110
                self.attribute_declare()
                pass

            elif la_ == 2:
                self.state = 111
                self.method_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):
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
            return BKOOLParser.RULE_attribute_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declare" ):
                return visitor.visitAttribute_declare(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declare(self):

        localctx = BKOOLParser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 114
                self.match(BKOOLParser.STATIC)

            elif la_ == 2:
                self.state = 115
                self.match(BKOOLParser.FINAL)

            elif la_ == 3:
                self.state = 116
                self.match(BKOOLParser.FINAL)
                self.state = 117
                self.match(BKOOLParser.STATIC)

            elif la_ == 4:
                self.state = 118
                self.match(BKOOLParser.STATIC)
                self.state = 119
                self.match(BKOOLParser.FINAL)


            self.state = 122
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 124
                self.immutable_attribute()
                pass

            elif la_ == 2:
                self.state = 125
                self.mutable_attribute()
                pass


            self.state = 128
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
            self.state = 130
            self.data_type()
            self.state = 131
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
            self.state = 133
            self.data_type()
            self.state = 134
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
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

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = BKOOLParser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_declare)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(BKOOLParser.STATIC)
                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                    self.state = 137
                    self.data_type()
                    pass
                elif token in [BKOOLParser.VOID]:
                    self.state = 138
                    self.match(BKOOLParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 141
                self.match(BKOOLParser.ID)
                self.state = 142
                self.match(BKOOLParser.LB)
                self.state = 143
                self.paralist()
                self.state = 144
                self.match(BKOOLParser.RB)
                self.state = 145
                self.block_statement()
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 147
                    self.data_type()

                elif la_ == 2:
                    self.state = 148
                    self.match(BKOOLParser.VOID)


                self.state = 151
                self.match(BKOOLParser.ID)
                self.state = 152
                self.match(BKOOLParser.LB)
                self.state = 153
                self.paralist()
                self.state = 154
                self.match(BKOOLParser.RB)
                self.state = 155
                self.block_statement()
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


        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LE(self):
            return self.getToken(BKOOLParser.LE, 0)

        def GE(self):
            return self.getToken(BKOOLParser.GE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.expr1()
                self.state = 160
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LE) | (1 << BKOOLParser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
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
        self.enterRule(localctx, 18, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.expr2(0)
                self.state = 167
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 176
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 177
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 178
                    self.expr3(0) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 187
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 188
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 189
                    self.expr4(0) 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 198
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 199
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 200
                    self.expr5(0) 
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 209
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 210
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 211
                    self.expr6() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_expr6)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(BKOOLParser.NOT)
                self.state = 218
                self.expr6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

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
        self.enterRule(localctx, 30, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.expr7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
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
        self.enterRule(localctx, 32, self.RULE_expr8)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.expr9(0)
                self.state = 228
                self.match(BKOOLParser.LSB)
                self.state = 229
                self.expr()
                self.state = 230
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
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


        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 236
                self.match(BKOOLParser.ID)
                self.state = 237
                self.match(BKOOLParser.DOT)
                self.state = 238
                self.match(BKOOLParser.ID)
                self.state = 244
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 239
                    self.match(BKOOLParser.LB)
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                        self.state = 240
                        self.exprlist()


                    self.state = 243
                    self.match(BKOOLParser.RB)


                pass

            elif la_ == 2:
                self.state = 246
                self.expr10()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 249
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 250
                    self.match(BKOOLParser.DOT)
                    self.state = 251
                    self.match(BKOOLParser.ID)
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 252
                        self.match(BKOOLParser.LB)
                        self.state = 254
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 253
                            self.exprlist()


                        self.state = 256
                        self.match(BKOOLParser.RB)

             
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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


        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(BKOOLParser.NEW)
                self.state = 265
                self.match(BKOOLParser.ID)
                self.state = 266
                self.match(BKOOLParser.LB)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 267
                    self.exprlist()


                self.state = 270
                self.match(BKOOLParser.RB)
                self.state = 272
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 271
                    self.expr10()


                pass
            elif token in [BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.expr11()
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
        self.enterRule(localctx, 38, self.RULE_expr11)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(BKOOLParser.LB)
                self.state = 278
                self.expr()
                self.state = 279
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
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
        self.enterRule(localctx, 40, self.RULE_exprlist)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(BKOOLParser.COMMA)
                self.state = 289
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr()
                self.state = 292
                self.match(BKOOLParser.COMMA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKOOLParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKOOLParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Return_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invocation_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.break_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 300
                self.continue_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 301
                self.return_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 302
                self.method_invocation_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 303
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def member_block(self):
            return self.getTypedRuleContext(BKOOLParser.Member_blockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = BKOOLParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(BKOOLParser.LP)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 307
                self.member_block()


            self.state = 310
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def FINAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.FINAL)
            else:
                return self.getToken(BKOOLParser.FINAL, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_member_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_block" ):
                return visitor.visitMember_block(self)
            else:
                return visitor.visitChildren(self)




    def member_block(self):

        localctx = BKOOLParser.Member_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_member_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BKOOLParser.FINAL:
                        self.state = 312
                        self.match(BKOOLParser.FINAL)


                    self.state = 315
                    self.var_decl() 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 322 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 321
                self.statement()
                self.state = 324 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSINGMENT(self):
            return self.getToken(BKOOLParser.ASSINGMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = BKOOLParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 326
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 327
                self.expr8()
                pass


            self.state = 330
            self.match(BKOOLParser.ASSINGMENT)
            self.state = 331
            self.expr()
            self.state = 332
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKOOLParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(BKOOLParser.IF)
            self.state = 335
            self.expr()
            self.state = 336
            self.match(BKOOLParser.THEN)
            self.state = 337
            self.statement()
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 338
                self.match(BKOOLParser.ELSE)
                self.state = 339
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSINGMENT(self):
            return self.getToken(BKOOLParser.ASSINGMENT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKOOLParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKOOLParser.FOR)
            self.state = 343
            self.match(BKOOLParser.ID)
            self.state = 344
            self.match(BKOOLParser.ASSINGMENT)
            self.state = 345
            self.expr()
            self.state = 346
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 347
            self.expr()
            self.state = 348
            self.match(BKOOLParser.DO)
            self.state = 349
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKOOLParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(BKOOLParser.BREAK)
            self.state = 352
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKOOLParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(BKOOLParser.CONTINUE)
            self.state = 355
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
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
            return BKOOLParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKOOLParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(BKOOLParser.RETURN)
            self.state = 358
            self.expr()
            self.state = 359
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):
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

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)




    def member_access(self):

        localctx = BKOOLParser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_member_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 361
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 362
                self.expr()
                pass


            self.state = 365
            self.match(BKOOLParser.DOT)
            self.state = 366
            self.match(BKOOLParser.ID)
            self.state = 367
            self.match(BKOOLParser.LB)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 368
                self.exprlist()


            self.state = 371
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access(self):
            return self.getTypedRuleContext(BKOOLParser.Member_accessContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = BKOOLParser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.member_access()
            self.state = 374
            self.match(BKOOLParser.SEMI)
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

        def type_not_void(self):
            return self.getTypedRuleContext(BKOOLParser.Type_not_voidContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


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
        self.enterRule(localctx, 64, self.RULE_data_type)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.type_not_void()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_not_voidContext(ParserRuleContext):
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
            return BKOOLParser.RULE_type_not_void

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_not_void" ):
                return visitor.visitType_not_void(self)
            else:
                return visitor.visitChildren(self)




    def type_not_void(self):

        localctx = BKOOLParser.Type_not_voidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_type_not_void)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_not_void(self):
            return self.getTypedRuleContext(BKOOLParser.Type_not_voidContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.type_not_void()
            self.state = 384
            self.match(BKOOLParser.LSB)
            self.state = 385
            self.match(BKOOLParser.INTLIT)
            self.state = 386
            self.match(BKOOLParser.RSB)
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

        def array_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Array_litContext,0)


        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_literal)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.array_lit()
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 391
                self.match(BKOOLParser.BOOLLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 392
                self.match(BKOOLParser.STRINGLIT)
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
        self.enterRule(localctx, 72, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(BKOOLParser.ID)
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
        self.enterRule(localctx, 74, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.idlist()
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
        self.enterRule(localctx, 76, self.RULE_paralist)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.para_decl()
                self.state = 400
                self.match(BKOOLParser.SEMI)
                self.state = 401
                self.paralist()
                pass
            elif token in [BKOOLParser.RB]:
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
        self.enterRule(localctx, 78, self.RULE_para_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
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
        self.enterRule(localctx, 80, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(BKOOLParser.ID)
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 409
                    self.match(BKOOLParser.EQUAL)
                    self.state = 410
                    self.expr()


                self.state = 413
                self.match(BKOOLParser.COMMA)
                self.state = 414
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(BKOOLParser.ID)
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 416
                    self.match(BKOOLParser.EQUAL)
                    self.state = 417
                    self.expr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def array_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Array_declareContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(BKOOLParser.LP)
            self.state = 423
            self.array_declare()
            self.state = 424
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare" ):
                return visitor.visitArray_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_declare(self):

        localctx = BKOOLParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.expr()
            self.state = 427
            self.array_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKOOLParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_list)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(BKOOLParser.COMMA)
                self.state = 430
                self.expr()
                self.state = 431
                self.array_list()
                pass
            elif token in [BKOOLParser.RP]:
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr2_sempred
        self._predicates[11] = self.expr3_sempred
        self._predicates[12] = self.expr4_sempred
        self._predicates[13] = self.expr5_sempred
        self._predicates[17] = self.expr9_sempred
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
                return self.precpred(self._ctx, 3)
         




