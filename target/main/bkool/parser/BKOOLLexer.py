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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01b2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\7\2\u0088\n\2\f\2\16\2\u008b\13\2\3\2\5\2\u008e\n\2")
        buf.write("\3\2\3\2\5\2\u0092\n\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009a")
        buf.write("\n\3\f\3\16\3\u009d\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\6\67\u0167\n\67\r\67\16\67")
        buf.write("\u0168\38\68\u016c\n8\r8\168\u016d\38\38\38\68\u0173\n")
        buf.write("8\r8\168\u0174\38\38\38\68\u017a\n8\r8\168\u017b\38\3")
        buf.write("8\38\58\u0181\n8\39\39\3:\3:\3;\3;\3<\3<\7<\u018b\n<\f")
        buf.write("<\16<\u018e\13<\3=\3=\3=\5=\u0193\n=\3=\6=\u0196\n=\r")
        buf.write("=\16=\u0197\3>\3>\5>\u019c\n>\3>\3>\3>\7>\u01a1\n>\f>")
        buf.write("\16>\u01a4\13>\3?\6?\u01a7\n?\r?\16?\u01a8\3?\3?\3@\3")
        buf.write("@\3A\3A\3B\3B\3\u009b\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q\2s\2u\2w\2y\2{:};\177<\u0081=\u0083")
        buf.write(">\3\2\7\4\2\f\f\17\17\4\2C\\c|\3\2\62;\4\2GGgg\5\2\13")
        buf.write("\f\17\17\"\"\2\u01bf\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u0095")
        buf.write("\3\2\2\2\7\u00a3\3\2\2\2\t\u00ab\3\2\2\2\13\u00b1\3\2")
        buf.write("\2\2\r\u00b7\3\2\2\2\17\u00c0\3\2\2\2\21\u00c3\3\2\2\2")
        buf.write("\23\u00c8\3\2\2\2\25\u00d0\3\2\2\2\27\u00d6\3\2\2\2\31")
        buf.write("\u00d9\3\2\2\2\33\u00dd\3\2\2\2\35\u00e1\3\2\2\2\37\u00e8")
        buf.write("\3\2\2\2!\u00ed\3\2\2\2#\u00f1\3\2\2\2%\u00f8\3\2\2\2")
        buf.write("\'\u00fd\3\2\2\2)\u0103\3\2\2\2+\u0108\3\2\2\2-\u010c")
        buf.write("\3\2\2\2/\u0111\3\2\2\2\61\u0117\3\2\2\2\63\u011e\3\2")
        buf.write("\2\2\65\u0121\3\2\2\2\67\u0128\3\2\2\29\u012a\3\2\2\2")
        buf.write(";\u012c\3\2\2\2=\u012e\3\2\2\2?\u0130\3\2\2\2A\u0132\3")
        buf.write("\2\2\2C\u0134\3\2\2\2E\u0137\3\2\2\2G\u013a\3\2\2\2I\u013c")
        buf.write("\3\2\2\2K\u013e\3\2\2\2M\u0141\3\2\2\2O\u0144\3\2\2\2")
        buf.write("Q\u0147\3\2\2\2S\u014a\3\2\2\2U\u014c\3\2\2\2W\u014e\3")
        buf.write("\2\2\2Y\u0151\3\2\2\2[\u0153\3\2\2\2]\u0155\3\2\2\2_\u0157")
        buf.write("\3\2\2\2a\u0159\3\2\2\2c\u015b\3\2\2\2e\u015d\3\2\2\2")
        buf.write("g\u015f\3\2\2\2i\u0161\3\2\2\2k\u0163\3\2\2\2m\u0166\3")
        buf.write("\2\2\2o\u0180\3\2\2\2q\u0182\3\2\2\2s\u0184\3\2\2\2u\u0186")
        buf.write("\3\2\2\2w\u0188\3\2\2\2y\u018f\3\2\2\2{\u019b\3\2\2\2")
        buf.write("}\u01a6\3\2\2\2\177\u01ac\3\2\2\2\u0081\u01ae\3\2\2\2")
        buf.write("\u0083\u01b0\3\2\2\2\u0085\u0089\7%\2\2\u0086\u0088\n")
        buf.write("\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0091\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008c\u008e\7\17\2\2\u008d\u008c\3\2\2")
        buf.write("\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0092")
        buf.write("\7\f\2\2\u0090\u0092\7\2\2\3\u0091\u008d\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\b\2\2\2")
        buf.write("\u0094\4\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097\7,\2")
        buf.write("\2\u0097\u009b\3\2\2\2\u0098\u009a\13\2\2\2\u0099\u0098")
        buf.write("\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u009c\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009e\u009f\7,\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1\3")
        buf.write("\2\2\2\u00a1\u00a2\b\3\2\2\u00a2\6\3\2\2\2\u00a3\u00a4")
        buf.write("\7d\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7n\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\b\3\2\2\2\u00ab\u00ac\7d\2\2\u00ac\u00ad")
        buf.write("\7t\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7m\2\2\u00b0\n\3\2\2\2\u00b1\u00b2\7e\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7u\2\2\u00b6\f\3\2\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7w\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\16\3\2\2\2\u00c0\u00c1\7f\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\20\3\2\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5")
        buf.write("\7n\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7g\2\2\u00c7\22")
        buf.write("\3\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7z\2\2\u00ca\u00cb")
        buf.write("\7v\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7f\2\2\u00ce\u00cf\7u\2\2\u00cf\24\3\2\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7v\2\2\u00d5\26\3\2\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7h\2\2\u00d8\30\3\2\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc\32")
        buf.write("\3\2\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7y\2\2\u00e0\34\3\2\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7i\2\2\u00e7\36\3\2\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7j\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec \3\2\2\2\u00ed\u00ee\7h\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7t\2\2\u00f0\"\3\2\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7w\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7p\2\2\u00f7$\3")
        buf.write("\2\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7g\2\2\u00fc&\3\2\2\2\u00fd\u00fe")
        buf.write("\7h\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7n\2\2\u0100\u0101")
        buf.write("\7u\2\2\u0101\u0102\7g\2\2\u0102(\3\2\2\2\u0103\u0104")
        buf.write("\7x\2\2\u0104\u0105\7q\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write("\7f\2\2\u0107*\3\2\2\2\u0108\u0109\7p\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7n\2\2\u010b,\3\2\2\2\u010c\u010d")
        buf.write("\7v\2\2\u010d\u010e\7j\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7u\2\2\u0110.\3\2\2\2\u0111\u0112\7h\2\2\u0112\u0113")
        buf.write("\7k\2\2\u0113\u0114\7p\2\2\u0114\u0115\7c\2\2\u0115\u0116")
        buf.write("\7n\2\2\u0116\60\3\2\2\2\u0117\u0118\7u\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\u011a\7c\2\2\u011a\u011b\7v\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7e\2\2\u011d\62\3\2\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7q\2\2\u0120\64\3\2\2\2\u0121\u0122")
        buf.write("\7f\2\2\u0122\u0123\7q\2\2\u0123\u0124\7y\2\2\u0124\u0125")
        buf.write("\7p\2\2\u0125\u0126\7v\2\2\u0126\u0127\7q\2\2\u0127\66")
        buf.write("\3\2\2\2\u0128\u0129\7-\2\2\u01298\3\2\2\2\u012a\u012b")
        buf.write("\7/\2\2\u012b:\3\2\2\2\u012c\u012d\7,\2\2\u012d<\3\2\2")
        buf.write("\2\u012e\u012f\7\61\2\2\u012f>\3\2\2\2\u0130\u0131\7^")
        buf.write("\2\2\u0131@\3\2\2\2\u0132\u0133\7\'\2\2\u0133B\3\2\2\2")
        buf.write("\u0134\u0135\7#\2\2\u0135\u0136\7?\2\2\u0136D\3\2\2\2")
        buf.write("\u0137\u0138\7?\2\2\u0138\u0139\7?\2\2\u0139F\3\2\2\2")
        buf.write("\u013a\u013b\7>\2\2\u013bH\3\2\2\2\u013c\u013d\7@\2\2")
        buf.write("\u013dJ\3\2\2\2\u013e\u013f\7>\2\2\u013f\u0140\7?\2\2")
        buf.write("\u0140L\3\2\2\2\u0141\u0142\7@\2\2\u0142\u0143\7?\2\2")
        buf.write("\u0143N\3\2\2\2\u0144\u0145\7~\2\2\u0145\u0146\7~\2\2")
        buf.write("\u0146P\3\2\2\2\u0147\u0148\7(\2\2\u0148\u0149\7(\2\2")
        buf.write("\u0149R\3\2\2\2\u014a\u014b\7#\2\2\u014bT\3\2\2\2\u014c")
        buf.write("\u014d\7`\2\2\u014dV\3\2\2\2\u014e\u014f\7<\2\2\u014f")
        buf.write("\u0150\7?\2\2\u0150X\3\2\2\2\u0151\u0152\7]\2\2\u0152")
        buf.write("Z\3\2\2\2\u0153\u0154\7_\2\2\u0154\\\3\2\2\2\u0155\u0156")
        buf.write("\7}\2\2\u0156^\3\2\2\2\u0157\u0158\7\177\2\2\u0158`\3")
        buf.write("\2\2\2\u0159\u015a\7*\2\2\u015ab\3\2\2\2\u015b\u015c\7")
        buf.write("+\2\2\u015cd\3\2\2\2\u015d\u015e\7=\2\2\u015ef\3\2\2\2")
        buf.write("\u015f\u0160\7<\2\2\u0160h\3\2\2\2\u0161\u0162\7\60\2")
        buf.write("\2\u0162j\3\2\2\2\u0163\u0164\7.\2\2\u0164l\3\2\2\2\u0165")
        buf.write("\u0167\5u;\2\u0166\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169n\3\2\2\2\u016a")
        buf.write("\u016c\5u;\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0170\5w<\2\u0170\u0181\3\2\2\2\u0171\u0173\5u")
        buf.write(";\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0177\5y=\2\u0177\u0181\3\2\2\2\u0178\u017a\5u;\2\u0179")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\5")
        buf.write("w<\2\u017e\u017f\5y=\2\u017f\u0181\3\2\2\2\u0180\u016b")
        buf.write("\3\2\2\2\u0180\u0172\3\2\2\2\u0180\u0179\3\2\2\2\u0181")
        buf.write("p\3\2\2\2\u0182\u0183\7a\2\2\u0183r\3\2\2\2\u0184\u0185")
        buf.write("\t\3\2\2\u0185t\3\2\2\2\u0186\u0187\t\4\2\2\u0187v\3\2")
        buf.write("\2\2\u0188\u018c\5i\65\2\u0189\u018b\5u;\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018dx\3\2\2\2\u018e\u018c\3\2\2\2\u018f")
        buf.write("\u0192\t\5\2\2\u0190\u0193\5\67\34\2\u0191\u0193\59\35")
        buf.write("\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0196\5u;\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198z\3\2\2\2\u0199\u019c\5q9\2\u019a")
        buf.write("\u019c\5s:\2\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("\u01a2\3\2\2\2\u019d\u01a1\5q9\2\u019e\u01a1\5s:\2\u019f")
        buf.write("\u01a1\5u;\2\u01a0\u019d\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3|\3\2\2\2\u01a4\u01a2\3\2\2")
        buf.write("\2\u01a5\u01a7\t\6\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ab\b?\2\2\u01ab~\3\2\2\2\u01ac")
        buf.write("\u01ad\13\2\2\2\u01ad\u0080\3\2\2\2\u01ae\u01af\13\2\2")
        buf.write("\2\u01af\u0082\3\2\2\2\u01b0\u01b1\13\2\2\2\u01b1\u0084")
        buf.write("\3\2\2\2\23\2\u0089\u008d\u0091\u009b\u0168\u016d\u0174")
        buf.write("\u017b\u0180\u018c\u0192\u0197\u019b\u01a0\u01a2\u01a8")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_CMT = 1
    BLOCK_CMT = 2
    BOOLEAN = 3
    BREAK = 4
    CLASS = 5
    CONTINUE = 6
    DO = 7
    ELSE = 8
    EXTENDS = 9
    FLOAT = 10
    IF = 11
    INT = 12
    NEW = 13
    STRING = 14
    THEN = 15
    FOR = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    VOID = 20
    NIL = 21
    THIS = 22
    FINAL = 23
    STATIC = 24
    TO = 25
    DOWNTO = 26
    ADDOP = 27
    SUBOP = 28
    MULOP = 29
    FLOAT_DIV = 30
    INTEGER_DIV = 31
    MOD = 32
    NOT_EQUAL = 33
    EQUAL = 34
    LESS = 35
    GREATER = 36
    LESS_OR_EQUAL = 37
    GREATER_OR_EQUAL = 38
    OR = 39
    AND = 40
    NOT = 41
    CONCATENATION = 42
    ASSIGN = 43
    LSB = 44
    RSB = 45
    LP = 46
    RP = 47
    LB = 48
    RB = 49
    SEMI_COLONE = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    ID = 56
    WS = 57
    ERROR_CHAR = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
            "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "LINE_CMT", "BLOCK_CMT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
            "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
            "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
            "FINAL", "STATIC", "TO", "DOWNTO", "ADDOP", "SUBOP", "MULOP", 
            "FLOAT_DIV", "INTEGER_DIV", "MOD", "NOT_EQUAL", "EQUAL", "LESS", 
            "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", "OR", "AND", 
            "NOT", "CONCATENATION", "ASSIGN", "LSB", "RSB", "LP", "RP", 
            "LB", "RB", "SEMI_COLONE", "COLON", "DOT", "COMMA", "INT_LIT", 
            "FLOAT_LIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LINE_CMT", "BLOCK_CMT", "BOOLEAN", "BREAK", "CLASS", 
                  "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", 
                  "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                  "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                  "ADDOP", "SUBOP", "MULOP", "FLOAT_DIV", "INTEGER_DIV", 
                  "MOD", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                  "GREATER_OR_EQUAL", "OR", "AND", "NOT", "CONCATENATION", 
                  "ASSIGN", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI_COLONE", 
                  "COLON", "DOT", "COMMA", "INT_LIT", "FLOAT_LIT", "UNDERSCORE", 
                  "LETTER", "DIGIT", "DECIMAL", "EXPONENT", "ID", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


