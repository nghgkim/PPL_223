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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3a\n\3\3\3\3\3\7\3e\n\3\f\3\16\3h\13")
        buf.write("\3\3\3\3\3\3\4\3\4\5\4n\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5v\n\5\3\5\3\5\3\6\3\6\5\6|\n\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\5\n\u008b\n\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u0092\n\n\5\n\u0094\n\n\3\13\5\13\u0097")
        buf.write("\n\13\3\13\3\13\5\13\u009b\n\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a7\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00ae\n\f\3\r\3\r\3\16\3\16\3\16\5\16\u00b5")
        buf.write("\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u00c7\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\5\24\u00ce\n\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\7\25\u00d6\n\25\f\25\16\25\u00d9\13\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u00e1\n\26\f\26\16\26\u00e4")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00ec\n\27\f")
        buf.write("\27\16\27\u00ef\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7")
        buf.write("\30\u00f7\n\30\f\30\16\30\u00fa\13\30\3\31\3\31\3\31\5")
        buf.write("\31\u00ff\n\31\3\32\3\32\3\32\5\32\u0104\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u010c\n\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u0114\n\34\3\34\5\34\u0117\n\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u011e\n\34\3\34\5\34\u0121\n")
        buf.write("\34\7\34\u0123\n\34\f\34\16\34\u0126\13\34\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u012c\n\35\3\35\3\35\5\35\u0130\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u013a\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0143\n\37\3 \3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u014c\n \3!\3!\5!\u0150\n!\3!\3!\3")
        buf.write("\"\5\"\u0155\n\"\3\"\7\"\u0158\n\"\f\"\16\"\u015b\13\"")
        buf.write("\3\"\7\"\u015e\n\"\f\"\16\"\u0161\13\"\3#\3#\5#\u0165")
        buf.write("\n#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\5$\u0171\n$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write(")\3)\5)\u0188\n)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\5")
        buf.write("*\u0196\n*\3+\3+\3+\3+\3,\3,\3,\3,\3,\5,\u01a1\n,\3-\3")
        buf.write("-\3-\2\7(*,.\66.\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\n\6\2\5\5\f\f")
        buf.write("\16\16\20\20\3\2%(\3\2#$\3\2)*\3\2\35\36\3\2\37\"\3\2")
        buf.write("\33\34\3\28;\2\u01b0\2Z\3\2\2\2\4\\\3\2\2\2\6m\3\2\2\2")
        buf.write("\bu\3\2\2\2\n{\3\2\2\2\f\177\3\2\2\2\16\u0082\3\2\2\2")
        buf.write("\20\u0085\3\2\2\2\22\u0093\3\2\2\2\24\u00a6\3\2\2\2\26")
        buf.write("\u00ad\3\2\2\2\30\u00af\3\2\2\2\32\u00b4\3\2\2\2\34\u00b6")
        buf.write("\3\2\2\2\36\u00b8\3\2\2\2 \u00ba\3\2\2\2\"\u00bf\3\2\2")
        buf.write("\2$\u00c6\3\2\2\2&\u00cd\3\2\2\2(\u00cf\3\2\2\2*\u00da")
        buf.write("\3\2\2\2,\u00e5\3\2\2\2.\u00f0\3\2\2\2\60\u00fe\3\2\2")
        buf.write("\2\62\u0103\3\2\2\2\64\u010b\3\2\2\2\66\u010d\3\2\2\2")
        buf.write("8\u0127\3\2\2\2:\u0139\3\2\2\2<\u0142\3\2\2\2>\u014b\3")
        buf.write("\2\2\2@\u014d\3\2\2\2B\u0159\3\2\2\2D\u0164\3\2\2\2F\u016a")
        buf.write("\3\2\2\2H\u0172\3\2\2\2J\u017b\3\2\2\2L\u017e\3\2\2\2")
        buf.write("N\u0181\3\2\2\2P\u0187\3\2\2\2R\u0195\3\2\2\2T\u0197\3")
        buf.write("\2\2\2V\u01a0\3\2\2\2X\u01a2\3\2\2\2Z[\3\2\2\2[\3\3\2")
        buf.write("\2\2\\]\7\7\2\2]`\7<\2\2^_\7\13\2\2_a\7<\2\2`^\3\2\2\2")
        buf.write("`a\3\2\2\2ab\3\2\2\2bf\7\60\2\2ce\5\6\4\2dc\3\2\2\2eh")
        buf.write("\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7\61")
        buf.write("\2\2j\5\3\2\2\2kn\5\b\5\2ln\5\24\13\2mk\3\2\2\2ml\3\2")
        buf.write("\2\2n\7\3\2\2\2ov\7\32\2\2pv\7\31\2\2qr\7\32\2\2rv\7\31")
        buf.write("\2\2st\7\31\2\2tv\7\32\2\2uo\3\2\2\2up\3\2\2\2uq\3\2\2")
        buf.write("\2us\3\2\2\2uv\3\2\2\2vw\3\2\2\2wx\5\n\6\2x\t\3\2\2\2")
        buf.write("y|\5\f\7\2z|\5\16\b\2{y\3\2\2\2{z\3\2\2\2|}\3\2\2\2}~")
        buf.write("\7\64\2\2~\13\3\2\2\2\177\u0080\5\32\16\2\u0080\u0081")
        buf.write("\5\20\t\2\u0081\r\3\2\2\2\u0082\u0083\5\32\16\2\u0083")
        buf.write("\u0084\5\20\t\2\u0084\17\3\2\2\2\u0085\u0086\5\22\n\2")
        buf.write("\u0086\21\3\2\2\2\u0087\u008a\7<\2\2\u0088\u0089\7$\2")
        buf.write("\2\u0089\u008b\5$\23\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\7\67\2\2\u008d")
        buf.write("\u0094\5\22\n\2\u008e\u0091\7<\2\2\u008f\u0090\7$\2\2")
        buf.write("\u0090\u0092\5$\23\2\u0091\u008f\3\2\2\2\u0091\u0092\3")
        buf.write("\2\2\2\u0092\u0094\3\2\2\2\u0093\u0087\3\2\2\2\u0093\u008e")
        buf.write("\3\2\2\2\u0094\23\3\2\2\2\u0095\u0097\7\32\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u009a\3\2\2\2\u0098")
        buf.write("\u009b\5\32\16\2\u0099\u009b\5\36\20\2\u009a\u0098\3\2")
        buf.write("\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d")
        buf.write("\7<\2\2\u009d\u009e\7\62\2\2\u009e\u009f\5\26\f\2\u009f")
        buf.write("\u00a0\7\63\2\2\u00a0\u00a1\5@!\2\u00a1\u00a7\3\2\2\2")
        buf.write("\u00a2\u00a3\7<\2\2\u00a3\u00a4\5\26\f\2\u00a4\u00a5\5")
        buf.write("@!\2\u00a5\u00a7\3\2\2\2\u00a6\u0096\3\2\2\2\u00a6\u00a2")
        buf.write("\3\2\2\2\u00a7\25\3\2\2\2\u00a8\u00a9\5\30\r\2\u00a9\u00aa")
        buf.write("\7\64\2\2\u00aa\u00ab\5\26\f\2\u00ab\u00ae\3\2\2\2\u00ac")
        buf.write("\u00ae\3\2\2\2\u00ad\u00a8\3\2\2\2\u00ad\u00ac\3\2\2\2")
        buf.write("\u00ae\27\3\2\2\2\u00af\u00b0\5\22\n\2\u00b0\31\3\2\2")
        buf.write("\2\u00b1\u00b5\5\34\17\2\u00b2\u00b5\5 \21\2\u00b3\u00b5")
        buf.write("\5\"\22\2\u00b4\u00b1\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\33\3\2\2\2\u00b6\u00b7\t\2\2\2\u00b7")
        buf.write("\35\3\2\2\2\u00b8\u00b9\7\26\2\2\u00b9\37\3\2\2\2\u00ba")
        buf.write("\u00bb\5\34\17\2\u00bb\u00bc\7.\2\2\u00bc\u00bd\78\2\2")
        buf.write("\u00bd\u00be\7/\2\2\u00be!\3\2\2\2\u00bf\u00c0\7<\2\2")
        buf.write("\u00c0#\3\2\2\2\u00c1\u00c2\5&\24\2\u00c2\u00c3\t\3\2")
        buf.write("\2\u00c3\u00c4\5&\24\2\u00c4\u00c7\3\2\2\2\u00c5\u00c7")
        buf.write("\5&\24\2\u00c6\u00c1\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7")
        buf.write("%\3\2\2\2\u00c8\u00c9\5(\25\2\u00c9\u00ca\t\4\2\2\u00ca")
        buf.write("\u00cb\5(\25\2\u00cb\u00ce\3\2\2\2\u00cc\u00ce\5(\25\2")
        buf.write("\u00cd\u00c8\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\'\3\2\2")
        buf.write("\2\u00cf\u00d0\b\25\1\2\u00d0\u00d1\5*\26\2\u00d1\u00d7")
        buf.write("\3\2\2\2\u00d2\u00d3\f\4\2\2\u00d3\u00d4\t\5\2\2\u00d4")
        buf.write("\u00d6\5*\26\2\u00d5\u00d2\3\2\2\2\u00d6\u00d9\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8)\3\2\2")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00da\u00db\b\26\1\2\u00db\u00dc")
        buf.write("\5,\27\2\u00dc\u00e2\3\2\2\2\u00dd\u00de\f\4\2\2\u00de")
        buf.write("\u00df\t\6\2\2\u00df\u00e1\5,\27\2\u00e0\u00dd\3\2\2\2")
        buf.write("\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3+\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6")
        buf.write("\b\27\1\2\u00e6\u00e7\5.\30\2\u00e7\u00ed\3\2\2\2\u00e8")
        buf.write("\u00e9\f\4\2\2\u00e9\u00ea\t\7\2\2\u00ea\u00ec\5.\30\2")
        buf.write("\u00eb\u00e8\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3")
        buf.write("\2\2\2\u00ed\u00ee\3\2\2\2\u00ee-\3\2\2\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00f0\u00f1\b\30\1\2\u00f1\u00f2\5\60\31\2\u00f2")
        buf.write("\u00f8\3\2\2\2\u00f3\u00f4\f\4\2\2\u00f4\u00f5\7,\2\2")
        buf.write("\u00f5\u00f7\5\60\31\2\u00f6\u00f3\3\2\2\2\u00f7\u00fa")
        buf.write("\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("/\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\7+\2\2\u00fc")
        buf.write("\u00ff\5\60\31\2\u00fd\u00ff\5\62\32\2\u00fe\u00fb\3\2")
        buf.write("\2\2\u00fe\u00fd\3\2\2\2\u00ff\61\3\2\2\2\u0100\u0101")
        buf.write("\t\6\2\2\u0101\u0104\5\62\32\2\u0102\u0104\5\64\33\2\u0103")
        buf.write("\u0100\3\2\2\2\u0103\u0102\3\2\2\2\u0104\63\3\2\2\2\u0105")
        buf.write("\u0106\5\66\34\2\u0106\u0107\7.\2\2\u0107\u0108\5$\23")
        buf.write("\2\u0108\u0109\7/\2\2\u0109\u010c\3\2\2\2\u010a\u010c")
        buf.write("\5\66\34\2\u010b\u0105\3\2\2\2\u010b\u010a\3\2\2\2\u010c")
        buf.write("\65\3\2\2\2\u010d\u010e\b\34\1\2\u010e\u010f\7<\2\2\u010f")
        buf.write("\u0110\7\66\2\2\u0110\u0116\7<\2\2\u0111\u0113\7\62\2")
        buf.write("\2\u0112\u0114\5<\37\2\u0113\u0112\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\7\63\2\2\u0116")
        buf.write("\u0111\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0124\3\2\2\2")
        buf.write("\u0118\u0119\f\4\2\2\u0119\u011a\7\66\2\2\u011a\u0120")
        buf.write("\7<\2\2\u011b\u011d\7\62\2\2\u011c\u011e\5<\37\2\u011d")
        buf.write("\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f\u0121\7\63\2\2\u0120\u011b\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0118\3\2\2\2\u0123")
        buf.write("\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\67\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u0128\7\17")
        buf.write("\2\2\u0128\u0129\7<\2\2\u0129\u012b\7\62\2\2\u012a\u012c")
        buf.write("\5<\37\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012f\7\63\2\2\u012e\u0130\58\35")
        buf.write("\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u01309\3\2")
        buf.write("\2\2\u0131\u0132\7\62\2\2\u0132\u0133\5$\23\2\u0133\u0134")
        buf.write("\7\63\2\2\u0134\u013a\3\2\2\2\u0135\u013a\7<\2\2\u0136")
        buf.write("\u013a\5R*\2\u0137\u013a\7\30\2\2\u0138\u013a\7\27\2\2")
        buf.write("\u0139\u0131\3\2\2\2\u0139\u0135\3\2\2\2\u0139\u0136\3")
        buf.write("\2\2\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013a;")
        buf.write("\3\2\2\2\u013b\u013c\5$\23\2\u013c\u013d\7\67\2\2\u013d")
        buf.write("\u013e\5<\37\2\u013e\u0143\3\2\2\2\u013f\u0140\5$\23\2")
        buf.write("\u0140\u0141\7\67\2\2\u0141\u0143\3\2\2\2\u0142\u013b")
        buf.write("\3\2\2\2\u0142\u013f\3\2\2\2\u0143=\3\2\2\2\u0144\u014c")
        buf.write("\5@!\2\u0145\u014c\5D#\2\u0146\u014c\5F$\2\u0147\u014c")
        buf.write("\5H%\2\u0148\u014c\5J&\2\u0149\u014c\5L\'\2\u014a\u014c")
        buf.write("\5N(\2\u014b\u0144\3\2\2\2\u014b\u0145\3\2\2\2\u014b\u0146")
        buf.write("\3\2\2\2\u014b\u0147\3\2\2\2\u014b\u0148\3\2\2\2\u014b")
        buf.write("\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c?\3\2\2\2\u014d")
        buf.write("\u014f\7\60\2\2\u014e\u0150\5B\"\2\u014f\u014e\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\7")
        buf.write("\61\2\2\u0152A\3\2\2\2\u0153\u0155\7\31\2\2\u0154\u0153")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0158\5\n\6\2\u0157\u0154\3\2\2\2\u0158\u015b\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015f\3")
        buf.write("\2\2\2\u015b\u0159\3\2\2\2\u015c\u015e\5> \2\u015d\u015c")
        buf.write("\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160C\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write("\u0165\7<\2\2\u0163\u0165\5\64\33\2\u0164\u0162\3\2\2")
        buf.write("\2\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167")
        buf.write("\7-\2\2\u0167\u0168\5$\23\2\u0168\u0169\7\64\2\2\u0169")
        buf.write("E\3\2\2\2\u016a\u016b\7\r\2\2\u016b\u016c\5$\23\2\u016c")
        buf.write("\u016d\7\21\2\2\u016d\u0170\5> \2\u016e\u016f\7\n\2\2")
        buf.write("\u016f\u0171\5> \2\u0170\u016e\3\2\2\2\u0170\u0171\3\2")
        buf.write("\2\2\u0171G\3\2\2\2\u0172\u0173\7\22\2\2\u0173\u0174\7")
        buf.write("<\2\2\u0174\u0175\7-\2\2\u0175\u0176\5$\23\2\u0176\u0177")
        buf.write("\t\b\2\2\u0177\u0178\5$\23\2\u0178\u0179\7\t\2\2\u0179")
        buf.write("\u017a\5> \2\u017aI\3\2\2\2\u017b\u017c\7\6\2\2\u017c")
        buf.write("\u017d\7\64\2\2\u017dK\3\2\2\2\u017e\u017f\7\b\2\2\u017f")
        buf.write("\u0180\7\64\2\2\u0180M\3\2\2\2\u0181\u0182\7\23\2\2\u0182")
        buf.write("\u0183\5$\23\2\u0183\u0184\7\64\2\2\u0184O\3\2\2\2\u0185")
        buf.write("\u0188\7<\2\2\u0186\u0188\5$\23\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7")
        buf.write("\66\2\2\u018a\u018b\7<\2\2\u018b\u018c\7\62\2\2\u018c")
        buf.write("\u018d\5<\37\2\u018d\u018e\7\63\2\2\u018e\u018f\7\64\2")
        buf.write("\2\u018fQ\3\2\2\2\u0190\u0196\78\2\2\u0191\u0196\79\2")
        buf.write("\2\u0192\u0196\7:\2\2\u0193\u0196\7;\2\2\u0194\u0196\5")
        buf.write("T+\2\u0195\u0190\3\2\2\2\u0195\u0191\3\2\2\2\u0195\u0192")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("S\3\2\2\2\u0197\u0198\7\60\2\2\u0198\u0199\5V,\2\u0199")
        buf.write("\u019a\7\61\2\2\u019aU\3\2\2\2\u019b\u019c\5X-\2\u019c")
        buf.write("\u019d\7\67\2\2\u019d\u019e\5V,\2\u019e\u01a1\3\2\2\2")
        buf.write("\u019f\u01a1\5X-\2\u01a0\u019b\3\2\2\2\u01a0\u019f\3\2")
        buf.write("\2\2\u01a1W\3\2\2\2\u01a2\u01a3\t\t\2\2\u01a3Y\3\2\2\2")
        buf.write("+`fmu{\u008a\u0091\u0093\u0096\u009a\u00a6\u00ad\u00b4")
        buf.write("\u00c6\u00cd\u00d7\u00e2\u00ed\u00f8\u00fe\u0103\u010b")
        buf.write("\u0113\u0116\u011d\u0120\u0124\u012b\u012f\u0139\u0142")
        buf.write("\u014b\u014f\u0154\u0159\u015f\u0164\u0170\u0187\u0195")
        buf.write("\u01a0")
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




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BKOOLParser.CLASS)
            self.state = 91
            self.match(BKOOLParser.ID)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 92
                self.match(BKOOLParser.EXTENDS)
                self.state = 93
                self.match(BKOOLParser.ID)


            self.state = 96
            self.match(BKOOLParser.LP)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 97
                self.member()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
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




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
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




    def attribute_decl(self):

        localctx = BKOOLParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 109
                self.match(BKOOLParser.STATIC)

            elif la_ == 2:
                self.state = 110
                self.match(BKOOLParser.FINAL)

            elif la_ == 3:
                self.state = 111
                self.match(BKOOLParser.STATIC)
                self.state = 112
                self.match(BKOOLParser.FINAL)

            elif la_ == 4:
                self.state = 113
                self.match(BKOOLParser.FINAL)
                self.state = 114
                self.match(BKOOLParser.STATIC)


            self.state = 117
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




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 119
                self.immutable_attribute()
                pass

            elif la_ == 2:
                self.state = 120
                self.mutable_attribute()
                pass


            self.state = 123
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




    def immutable_attribute(self):

        localctx = BKOOLParser.Immutable_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immutable_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.data_type()
            self.state = 126
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




    def mutable_attribute(self):

        localctx = BKOOLParser.Mutable_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mutable_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.data_type()
            self.state = 129
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




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(BKOOLParser.ID)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 134
                    self.match(BKOOLParser.EQUAL)
                    self.state = 135
                    self.expr()


                self.state = 138
                self.match(BKOOLParser.COMMA)
                self.state = 139
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(BKOOLParser.ID)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 141
                    self.match(BKOOLParser.EQUAL)
                    self.state = 142
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




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 147
                    self.match(BKOOLParser.STATIC)


                self.state = 152
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                    self.state = 150
                    self.data_type()
                    pass
                elif token in [BKOOLParser.VOID]:
                    self.state = 151
                    self.void_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 154
                self.match(BKOOLParser.ID)
                self.state = 155
                self.match(BKOOLParser.LB)
                self.state = 156
                self.paralist()
                self.state = 157
                self.match(BKOOLParser.RB)
                self.state = 158
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(BKOOLParser.ID)
                self.state = 161
                self.paralist()
                self.state = 162
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




    def paralist(self):

        localctx = BKOOLParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paralist)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.para_decl()
                self.state = 167
                self.match(BKOOLParser.SEMI)
                self.state = 168
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




    def para_decl(self):

        localctx = BKOOLParser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_para_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
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




    def data_type(self):

        localctx = BKOOLParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_data_type)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.not_void_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.arr_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
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




    def not_void_type(self):

        localctx = BKOOLParser.Not_void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_not_void_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
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




    def void_type(self):

        localctx = BKOOLParser.Void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
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




    def arr_type(self):

        localctx = BKOOLParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.not_void_type()
            self.state = 185
            self.match(BKOOLParser.LSB)
            self.state = 186
            self.match(BKOOLParser.INT_LIT)
            self.state = 187
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




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.expr1()
                self.state = 192
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.expr2(0)
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
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
            self.state = 206
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 210
                    self.expr3(0) 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 217
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 219
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 220
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 221
                    self.expr4(0) 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 228
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INTEGER_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 232
                    self.expr5(0) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 241
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 242
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 243
                    self.expr6() 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr6)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(BKOOLParser.NOT)
                self.state = 250
                self.expr6()
                pass
            elif token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
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




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.expr7()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
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




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr8)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.expr9(0)
                self.state = 260
                self.match(BKOOLParser.LSB)
                self.state = 261
                self.expr()
                self.state = 262
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
            self.state = 268
            self.match(BKOOLParser.ID)
            self.state = 269
            self.match(BKOOLParser.DOT)
            self.state = 270
            self.match(BKOOLParser.ID)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 271
                self.match(BKOOLParser.LB)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 272
                    self.exprlist()


                self.state = 275
                self.match(BKOOLParser.RB)


            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    self.match(BKOOLParser.DOT)
                    self.state = 280
                    self.match(BKOOLParser.ID)
                    self.state = 286
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        self.state = 281
                        self.match(BKOOLParser.LB)
                        self.state = 283
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 282
                            self.exprlist()


                        self.state = 285
                        self.match(BKOOLParser.RB)

             
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(BKOOLParser.NEW)
            self.state = 294
            self.match(BKOOLParser.ID)
            self.state = 295
            self.match(BKOOLParser.LB)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 296
                self.exprlist()


            self.state = 299
            self.match(BKOOLParser.RB)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 300
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




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr11)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(BKOOLParser.LB)
                self.state = 304
                self.expr()
                self.state = 305
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 310
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




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exprlist)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.expr()
                self.state = 314
                self.match(BKOOLParser.COMMA)
                self.state = 315
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.expr()
                self.state = 318
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




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.block_stmt()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.assignment_decl()
                pass
            elif token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.if_stmt()
                pass
            elif token in [BKOOLParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.for_stmt()
                pass
            elif token in [BKOOLParser.BREAK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 326
                self.break_stmt()
                pass
            elif token in [BKOOLParser.CONTINUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 327
                self.continue_stmt()
                pass
            elif token in [BKOOLParser.RETURN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 328
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




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(BKOOLParser.LP)
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 332
                self.mem_stmt()


            self.state = 335
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




    def mem_stmt(self):

        localctx = BKOOLParser.Mem_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_mem_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 338
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BKOOLParser.FINAL:
                        self.state = 337
                        self.match(BKOOLParser.FINAL)


                    self.state = 340
                    self.var_decl() 
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 346
                self.stmt()
                self.state = 351
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




    def assignment_decl(self):

        localctx = BKOOLParser.Assignment_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignment_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 352
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 353
                self.expr8()
                pass


            self.state = 356
            self.match(BKOOLParser.ASSIGN)
            self.state = 357
            self.expr()
            self.state = 358
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




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(BKOOLParser.IF)
            self.state = 361
            self.expr()
            self.state = 362
            self.match(BKOOLParser.THEN)
            self.state = 363
            self.stmt()
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 364
                self.match(BKOOLParser.ELSE)
                self.state = 365
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




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(BKOOLParser.FOR)
            self.state = 369
            self.match(BKOOLParser.ID)
            self.state = 370
            self.match(BKOOLParser.ASSIGN)
            self.state = 371
            self.expr()
            self.state = 372
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 373
            self.expr()
            self.state = 374
            self.match(BKOOLParser.DO)
            self.state = 375
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




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(BKOOLParser.BREAK)
            self.state = 378
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




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(BKOOLParser.CONTINUE)
            self.state = 381
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




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(BKOOLParser.RETURN)
            self.state = 384
            self.expr()
            self.state = 385
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




    def method_invocation_stmt(self):

        localctx = BKOOLParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 387
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 388
                self.expr()
                pass


            self.state = 391
            self.match(BKOOLParser.DOT)
            self.state = 392
            self.match(BKOOLParser.ID)
            self.state = 393
            self.match(BKOOLParser.LB)
            self.state = 394
            self.exprlist()
            self.state = 395
            self.match(BKOOLParser.RB)
            self.state = 396
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




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_literal)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.match(BKOOLParser.BOOL_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 400
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 401
                self.match(BKOOLParser.STR_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 402
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




    def arr_lit(self):

        localctx = BKOOLParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(BKOOLParser.LP)
            self.state = 406
            self.arr_decl()
            self.state = 407
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




    def arr_decl(self):

        localctx = BKOOLParser.Arr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arr_decl)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.arr_val()
                self.state = 410
                self.match(BKOOLParser.COMMA)
                self.state = 411
                self.arr_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
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




    def arr_val(self):

        localctx = BKOOLParser.Arr_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arr_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
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
         




