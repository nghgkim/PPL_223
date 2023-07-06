# Generated from /Users/nguyenkim/Downloads/assignment1/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01cf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\7\2\u0090\n\2\f\2\16\2\u0093")
        buf.write("\13\2\3\2\5\2\u0096\n\2\3\2\3\2\5\2\u009a\n\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\7\3\u00a2\n\3\f\3\16\3\u00a5\13\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\6\67\u016f\n\67\r\67\16\67\u0170\38\38\58\u0175\n8\3")
        buf.write("9\69\u0178\n9\r9\169\u0179\39\39\39\69\u017f\n9\r9\16")
        buf.write("9\u0180\39\39\39\69\u0186\n9\r9\169\u0187\39\39\39\59")
        buf.write("\u018d\n9\3:\3:\7:\u0191\n:\f:\16:\u0194\13:\3:\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\7>\u01a1\n>\f>\16>\u01a4\13>")
        buf.write("\3?\3?\3?\5?\u01a9\n?\3?\6?\u01ac\n?\r?\16?\u01ad\3@\3")
        buf.write("@\5@\u01b2\n@\3A\3A\3A\3B\3B\5B\u01b9\nB\3B\3B\3B\7B\u01be")
        buf.write("\nB\fB\16B\u01c1\13B\3C\6C\u01c4\nC\rC\16C\u01c5\3C\3")
        buf.write("C\3D\3D\3E\3E\3F\3F\3\u00a3\2G\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2{\2}\2\177\2")
        buf.write("\u0081\2\u0083<\u0085=\u0087>\u0089?\u008b@\3\2\t\4\2")
        buf.write("\f\f\17\17\4\2C\\c|\3\2\62;\4\2GGgg\6\2\n\f\16\17$$^^")
        buf.write("\t\2$$^^ddhhppttvv\5\2\13\f\17\17\"\"\2\u01dd\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3")
        buf.write("\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2")
        buf.write("\5\u009d\3\2\2\2\7\u00ab\3\2\2\2\t\u00b3\3\2\2\2\13\u00b9")
        buf.write("\3\2\2\2\r\u00bf\3\2\2\2\17\u00c8\3\2\2\2\21\u00cb\3\2")
        buf.write("\2\2\23\u00d0\3\2\2\2\25\u00d8\3\2\2\2\27\u00de\3\2\2")
        buf.write("\2\31\u00e1\3\2\2\2\33\u00e5\3\2\2\2\35\u00e9\3\2\2\2")
        buf.write("\37\u00f0\3\2\2\2!\u00f5\3\2\2\2#\u00f9\3\2\2\2%\u0100")
        buf.write("\3\2\2\2\'\u0105\3\2\2\2)\u010b\3\2\2\2+\u0110\3\2\2\2")
        buf.write("-\u0114\3\2\2\2/\u0119\3\2\2\2\61\u011f\3\2\2\2\63\u0126")
        buf.write("\3\2\2\2\65\u0129\3\2\2\2\67\u0130\3\2\2\29\u0132\3\2")
        buf.write("\2\2;\u0134\3\2\2\2=\u0136\3\2\2\2?\u0138\3\2\2\2A\u013a")
        buf.write("\3\2\2\2C\u013c\3\2\2\2E\u013f\3\2\2\2G\u0142\3\2\2\2")
        buf.write("I\u0144\3\2\2\2K\u0146\3\2\2\2M\u0149\3\2\2\2O\u014c\3")
        buf.write("\2\2\2Q\u014f\3\2\2\2S\u0152\3\2\2\2U\u0154\3\2\2\2W\u0156")
        buf.write("\3\2\2\2Y\u0159\3\2\2\2[\u015b\3\2\2\2]\u015d\3\2\2\2")
        buf.write("_\u015f\3\2\2\2a\u0161\3\2\2\2c\u0163\3\2\2\2e\u0165\3")
        buf.write("\2\2\2g\u0167\3\2\2\2i\u0169\3\2\2\2k\u016b\3\2\2\2m\u016e")
        buf.write("\3\2\2\2o\u0174\3\2\2\2q\u018c\3\2\2\2s\u018e\3\2\2\2")
        buf.write("u\u0198\3\2\2\2w\u019a\3\2\2\2y\u019c\3\2\2\2{\u019e\3")
        buf.write("\2\2\2}\u01a5\3\2\2\2\177\u01b1\3\2\2\2\u0081\u01b3\3")
        buf.write("\2\2\2\u0083\u01b8\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u01c9")
        buf.write("\3\2\2\2\u0089\u01cb\3\2\2\2\u008b\u01cd\3\2\2\2\u008d")
        buf.write("\u0091\7%\2\2\u008e\u0090\n\2\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3")
        buf.write("\2\2\2\u0092\u0099\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0096")
        buf.write("\7\17\2\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u009a\7\f\2\2\u0098\u009a\7\2\2\3")
        buf.write("\u0099\u0095\3\2\2\2\u0099\u0098\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u009c\b\2\2\2\u009c\4\3\2\2\2\u009d\u009e")
        buf.write("\7\61\2\2\u009e\u009f\7,\2\2\u009f\u00a3\3\2\2\2\u00a0")
        buf.write("\u00a2\13\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2")
        buf.write("\2\u00a3\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7,\2\2\u00a7")
        buf.write("\u00a8\7\61\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\b\3\2")
        buf.write("\2\u00aa\6\3\2\2\2\u00ab\u00ac\7d\2\2\u00ac\u00ad\7q\2")
        buf.write("\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7n\2\2\u00af\u00b0\7")
        buf.write("g\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7p\2\2\u00b2\b\3")
        buf.write("\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7m\2\2\u00b8\n")
        buf.write("\3\2\2\2\u00b9\u00ba\7e\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be\7u\2\2\u00be\f")
        buf.write("\3\2\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7p\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7g\2\2\u00c7\16")
        buf.write("\3\2\2\2\u00c8\u00c9\7f\2\2\u00c9\u00ca\7q\2\2\u00ca\20")
        buf.write("\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce")
        buf.write("\7u\2\2\u00ce\u00cf\7g\2\2\u00cf\22\3\2\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7z\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7f\2\2\u00d6\u00d7")
        buf.write("\7u\2\2\u00d7\24\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\26\3\2\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7h\2\2\u00e0\30\3\2\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7v\2\2\u00e4\32\3\2\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7y\2\2\u00e8\34")
        buf.write("\3\2\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7i\2\2\u00ef\36\3\2\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2")
        buf.write("\7j\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7p\2\2\u00f4 \3")
        buf.write("\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\"\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\u00ff\7p\2\2\u00ff$\3\2\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7t\2\2\u0102\u0103\7w\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104&\3\2\2\2\u0105\u0106\7h\2\2\u0106\u0107")
        buf.write("\7c\2\2\u0107\u0108\7n\2\2\u0108\u0109\7u\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a(\3\2\2\2\u010b\u010c\7x\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010d\u010e\7k\2\2\u010e\u010f\7f\2\2\u010f*\3")
        buf.write("\2\2\2\u0110\u0111\7p\2\2\u0111\u0112\7k\2\2\u0112\u0113")
        buf.write("\7n\2\2\u0113,\3\2\2\2\u0114\u0115\7v\2\2\u0115\u0116")
        buf.write("\7j\2\2\u0116\u0117\7k\2\2\u0117\u0118\7u\2\2\u0118.\3")
        buf.write("\2\2\2\u0119\u011a\7h\2\2\u011a\u011b\7k\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e\60")
        buf.write("\3\2\2\2\u011f\u0120\7u\2\2\u0120\u0121\7v\2\2\u0121\u0122")
        buf.write("\7c\2\2\u0122\u0123\7v\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7e\2\2\u0125\62\3\2\2\2\u0126\u0127\7v\2\2\u0127\u0128")
        buf.write("\7q\2\2\u0128\64\3\2\2\2\u0129\u012a\7f\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7y\2\2\u012c\u012d\7p\2\2\u012d\u012e")
        buf.write("\7v\2\2\u012e\u012f\7q\2\2\u012f\66\3\2\2\2\u0130\u0131")
        buf.write("\7-\2\2\u01318\3\2\2\2\u0132\u0133\7/\2\2\u0133:\3\2\2")
        buf.write("\2\u0134\u0135\7,\2\2\u0135<\3\2\2\2\u0136\u0137\7\61")
        buf.write("\2\2\u0137>\3\2\2\2\u0138\u0139\7^\2\2\u0139@\3\2\2\2")
        buf.write("\u013a\u013b\7\'\2\2\u013bB\3\2\2\2\u013c\u013d\7#\2\2")
        buf.write("\u013d\u013e\7?\2\2\u013eD\3\2\2\2\u013f\u0140\7?\2\2")
        buf.write("\u0140\u0141\7?\2\2\u0141F\3\2\2\2\u0142\u0143\7>\2\2")
        buf.write("\u0143H\3\2\2\2\u0144\u0145\7@\2\2\u0145J\3\2\2\2\u0146")
        buf.write("\u0147\7>\2\2\u0147\u0148\7?\2\2\u0148L\3\2\2\2\u0149")
        buf.write("\u014a\7@\2\2\u014a\u014b\7?\2\2\u014bN\3\2\2\2\u014c")
        buf.write("\u014d\7~\2\2\u014d\u014e\7~\2\2\u014eP\3\2\2\2\u014f")
        buf.write("\u0150\7(\2\2\u0150\u0151\7(\2\2\u0151R\3\2\2\2\u0152")
        buf.write("\u0153\7#\2\2\u0153T\3\2\2\2\u0154\u0155\7`\2\2\u0155")
        buf.write("V\3\2\2\2\u0156\u0157\7<\2\2\u0157\u0158\7?\2\2\u0158")
        buf.write("X\3\2\2\2\u0159\u015a\7]\2\2\u015aZ\3\2\2\2\u015b\u015c")
        buf.write("\7_\2\2\u015c\\\3\2\2\2\u015d\u015e\7}\2\2\u015e^\3\2")
        buf.write("\2\2\u015f\u0160\7\177\2\2\u0160`\3\2\2\2\u0161\u0162")
        buf.write("\7*\2\2\u0162b\3\2\2\2\u0163\u0164\7+\2\2\u0164d\3\2\2")
        buf.write("\2\u0165\u0166\7=\2\2\u0166f\3\2\2\2\u0167\u0168\7<\2")
        buf.write("\2\u0168h\3\2\2\2\u0169\u016a\7\60\2\2\u016aj\3\2\2\2")
        buf.write("\u016b\u016c\7.\2\2\u016cl\3\2\2\2\u016d\u016f\5y=\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171n\3\2\2\2\u0172\u0175\5%\23")
        buf.write("\2\u0173\u0175\5\'\24\2\u0174\u0172\3\2\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175p\3\2\2\2\u0176\u0178\5y=\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\5{>\2\u017c")
        buf.write("\u018d\3\2\2\2\u017d\u017f\5y=\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0183\5}?\2\u0183\u018d\3\2")
        buf.write("\2\2\u0184\u0186\5y=\2\u0185\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\5{>\2\u018a\u018b\5}?\2\u018b")
        buf.write("\u018d\3\2\2\2\u018c\u0177\3\2\2\2\u018c\u017e\3\2\2\2")
        buf.write("\u018c\u0185\3\2\2\2\u018dr\3\2\2\2\u018e\u0192\7$\2\2")
        buf.write("\u018f\u0191\5\177@\2\u0190\u018f\3\2\2\2\u0191\u0194")
        buf.write("\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0195\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196\7$\2\2")
        buf.write("\u0196\u0197\b:\3\2\u0197t\3\2\2\2\u0198\u0199\7a\2\2")
        buf.write("\u0199v\3\2\2\2\u019a\u019b\t\3\2\2\u019bx\3\2\2\2\u019c")
        buf.write("\u019d\t\4\2\2\u019dz\3\2\2\2\u019e\u01a2\5i\65\2\u019f")
        buf.write("\u01a1\5y=\2\u01a0\u019f\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3|\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a5\u01a8\t\5\2\2\u01a6\u01a9\5\67\34")
        buf.write("\2\u01a7\u01a9\59\35\2\u01a8\u01a6\3\2\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01ac\5y=\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae~\3\2\2\2\u01af")
        buf.write("\u01b2\5\u0081A\2\u01b0\u01b2\n\6\2\2\u01b1\u01af\3\2")
        buf.write("\2\2\u01b1\u01b0\3\2\2\2\u01b2\u0080\3\2\2\2\u01b3\u01b4")
        buf.write("\7^\2\2\u01b4\u01b5\t\7\2\2\u01b5\u0082\3\2\2\2\u01b6")
        buf.write("\u01b9\5u;\2\u01b7\u01b9\5w<\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b9\u01bf\3\2\2\2\u01ba\u01be\5u;\2\u01bb")
        buf.write("\u01be\5w<\2\u01bc\u01be\5y=\2\u01bd\u01ba\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u0084\3")
        buf.write("\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c4\t\b\2\2\u01c3\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\bC\2\2")
        buf.write("\u01c8\u0086\3\2\2\2\u01c9\u01ca\13\2\2\2\u01ca\u0088")
        buf.write("\3\2\2\2\u01cb\u01cc\13\2\2\2\u01cc\u008a\3\2\2\2\u01cd")
        buf.write("\u01ce\13\2\2\2\u01ce\u008c\3\2\2\2\26\2\u0091\u0095\u0099")
        buf.write("\u00a3\u0170\u0174\u0179\u0180\u0187\u018c\u0192\u01a2")
        buf.write("\u01a8\u01ad\u01b1\u01b8\u01bd\u01bf\u01c5\4\b\2\2\3:")
        buf.write("\2")
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
    SEMI = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    INT_LIT = 54
    BOOL_LIT = 55
    FLOAT_LIT = 56
    STR_LIT = 57
    ID = 58
    WS = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

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
            "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", "INT_LIT", "BOOL_LIT", 
            "FLOAT_LIT", "STR_LIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LINE_CMT", "BLOCK_CMT", "BOOLEAN", "BREAK", "CLASS", 
                  "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", 
                  "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                  "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                  "ADDOP", "SUBOP", "MULOP", "FLOAT_DIV", "INTEGER_DIV", 
                  "MOD", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                  "GREATER_OR_EQUAL", "OR", "AND", "NOT", "CONCATENATION", 
                  "ASSIGN", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", 
                  "COLON", "DOT", "COMMA", "INT_LIT", "BOOL_LIT", "FLOAT_LIT", 
                  "STR_LIT", "UNDERSCORE", "LETTER", "DIGIT", "DECIMAL", 
                  "EXPONENT", "CHAR", "ESC_SEQ", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[56] = self.STR_LIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[:];

     


