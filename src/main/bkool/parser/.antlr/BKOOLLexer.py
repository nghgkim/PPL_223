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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01c9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\2\5\2\u0094\n\2\3\2\3\2\5\2\u0098\n\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3\u00a0\n\3\f\3\16\3\u00a3\13\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\6\67\u016d")
        buf.write("\n\67\r\67\16\67\u016e\38\68\u0172\n8\r8\168\u0173\38")
        buf.write("\38\38\68\u0179\n8\r8\168\u017a\38\38\38\68\u0180\n8\r")
        buf.write("8\168\u0181\38\38\38\58\u0187\n8\39\39\79\u018b\n9\f9")
        buf.write("\169\u018e\139\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\7=\u019b")
        buf.write("\n=\f=\16=\u019e\13=\3>\3>\3>\5>\u01a3\n>\3>\6>\u01a6")
        buf.write("\n>\r>\16>\u01a7\3?\3?\5?\u01ac\n?\3@\3@\3@\3A\3A\5A\u01b3")
        buf.write("\nA\3A\3A\3A\7A\u01b8\nA\fA\16A\u01bb\13A\3B\6B\u01be")
        buf.write("\nB\rB\16B\u01bf\3B\3B\3C\3C\3D\3D\3E\3E\3\u00a1\2F\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081;\u0083<\u0085=\u0087>\u0089?")
        buf.write("\3\2\t\4\2\f\f\17\17\4\2C\\c|\3\2\62;\4\2GGgg\6\2\n\f")
        buf.write("\16\17$$^^\t\2$$^^ddhhppttvv\5\2\13\f\17\17\"\"\2\u01d6")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u009b")
        buf.write("\3\2\2\2\7\u00a9\3\2\2\2\t\u00b1\3\2\2\2\13\u00b7\3\2")
        buf.write("\2\2\r\u00bd\3\2\2\2\17\u00c6\3\2\2\2\21\u00c9\3\2\2\2")
        buf.write("\23\u00ce\3\2\2\2\25\u00d6\3\2\2\2\27\u00dc\3\2\2\2\31")
        buf.write("\u00df\3\2\2\2\33\u00e3\3\2\2\2\35\u00e7\3\2\2\2\37\u00ee")
        buf.write("\3\2\2\2!\u00f3\3\2\2\2#\u00f7\3\2\2\2%\u00fe\3\2\2\2")
        buf.write("\'\u0103\3\2\2\2)\u0109\3\2\2\2+\u010e\3\2\2\2-\u0112")
        buf.write("\3\2\2\2/\u0117\3\2\2\2\61\u011d\3\2\2\2\63\u0124\3\2")
        buf.write("\2\2\65\u0127\3\2\2\2\67\u012e\3\2\2\29\u0130\3\2\2\2")
        buf.write(";\u0132\3\2\2\2=\u0134\3\2\2\2?\u0136\3\2\2\2A\u0138\3")
        buf.write("\2\2\2C\u013a\3\2\2\2E\u013d\3\2\2\2G\u0140\3\2\2\2I\u0142")
        buf.write("\3\2\2\2K\u0144\3\2\2\2M\u0147\3\2\2\2O\u014a\3\2\2\2")
        buf.write("Q\u014d\3\2\2\2S\u0150\3\2\2\2U\u0152\3\2\2\2W\u0154\3")
        buf.write("\2\2\2Y\u0157\3\2\2\2[\u0159\3\2\2\2]\u015b\3\2\2\2_\u015d")
        buf.write("\3\2\2\2a\u015f\3\2\2\2c\u0161\3\2\2\2e\u0163\3\2\2\2")
        buf.write("g\u0165\3\2\2\2i\u0167\3\2\2\2k\u0169\3\2\2\2m\u016c\3")
        buf.write("\2\2\2o\u0186\3\2\2\2q\u0188\3\2\2\2s\u0192\3\2\2\2u\u0194")
        buf.write("\3\2\2\2w\u0196\3\2\2\2y\u0198\3\2\2\2{\u019f\3\2\2\2")
        buf.write("}\u01ab\3\2\2\2\177\u01ad\3\2\2\2\u0081\u01b2\3\2\2\2")
        buf.write("\u0083\u01bd\3\2\2\2\u0085\u01c3\3\2\2\2\u0087\u01c5\3")
        buf.write("\2\2\2\u0089\u01c7\3\2\2\2\u008b\u008f\7%\2\2\u008c\u008e")
        buf.write("\n\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0097\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0092\u0094\7\17\2\2\u0093\u0092")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0098\7\f\2\2\u0096\u0098\7\2\2\3\u0097\u0093\3\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b")
        buf.write("\2\2\2\u009a\4\3\2\2\2\u009b\u009c\7\61\2\2\u009c\u009d")
        buf.write("\7,\2\2\u009d\u00a1\3\2\2\2\u009e\u00a0\13\2\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3")
        buf.write("\2\2\2\u00a4\u00a5\7,\2\2\u00a5\u00a6\7\61\2\2\u00a6\u00a7")
        buf.write("\3\2\2\2\u00a7\u00a8\b\3\2\2\u00a8\6\3\2\2\2\u00a9\u00aa")
        buf.write("\7d\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\b\3\2\2\2\u00b1\u00b2\7d\2\2\u00b2\u00b3")
        buf.write("\7t\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7m\2\2\u00b6\n\3\2\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9")
        buf.write("\7n\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc")
        buf.write("\7u\2\2\u00bc\f\3\2\2\2\u00bd\u00be\7e\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\16\3\2\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8")
        buf.write("\7q\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb")
        buf.write("\7n\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7g\2\2\u00cd\22")
        buf.write("\3\2\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7z\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4")
        buf.write("\7f\2\2\u00d4\u00d5\7u\2\2\u00d5\24\3\2\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7v\2\2\u00db\26\3\2\2\2\u00dc\u00dd")
        buf.write("\7k\2\2\u00dd\u00de\7h\2\2\u00de\30\3\2\2\2\u00df\u00e0")
        buf.write("\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2\32")
        buf.write("\3\2\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6")
        buf.write("\7y\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7i\2\2\u00ed\36\3\2\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef\u00f0\7j\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2 \3\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5")
        buf.write("\7q\2\2\u00f5\u00f6\7t\2\2\u00f6\"\3\2\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd\7p\2\2\u00fd$\3")
        buf.write("\2\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7g\2\2\u0102&\3\2\2\2\u0103\u0104")
        buf.write("\7h\2\2\u0104\u0105\7c\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7u\2\2\u0107\u0108\7g\2\2\u0108(\3\2\2\2\u0109\u010a")
        buf.write("\7x\2\2\u010a\u010b\7q\2\2\u010b\u010c\7k\2\2\u010c\u010d")
        buf.write("\7f\2\2\u010d*\3\2\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7n\2\2\u0111,\3\2\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\u0114\7j\2\2\u0114\u0115\7k\2\2\u0115\u0116")
        buf.write("\7u\2\2\u0116.\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119")
        buf.write("\7k\2\2\u0119\u011a\7p\2\2\u011a\u011b\7c\2\2\u011b\u011c")
        buf.write("\7n\2\2\u011c\60\3\2\2\2\u011d\u011e\7u\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7c\2\2\u0120\u0121\7v\2\2\u0121\u0122")
        buf.write("\7k\2\2\u0122\u0123\7e\2\2\u0123\62\3\2\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7q\2\2\u0126\64\3\2\2\2\u0127\u0128")
        buf.write("\7f\2\2\u0128\u0129\7q\2\2\u0129\u012a\7y\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7v\2\2\u012c\u012d\7q\2\2\u012d\66")
        buf.write("\3\2\2\2\u012e\u012f\7-\2\2\u012f8\3\2\2\2\u0130\u0131")
        buf.write("\7/\2\2\u0131:\3\2\2\2\u0132\u0133\7,\2\2\u0133<\3\2\2")
        buf.write("\2\u0134\u0135\7\61\2\2\u0135>\3\2\2\2\u0136\u0137\7^")
        buf.write("\2\2\u0137@\3\2\2\2\u0138\u0139\7\'\2\2\u0139B\3\2\2\2")
        buf.write("\u013a\u013b\7#\2\2\u013b\u013c\7?\2\2\u013cD\3\2\2\2")
        buf.write("\u013d\u013e\7?\2\2\u013e\u013f\7?\2\2\u013fF\3\2\2\2")
        buf.write("\u0140\u0141\7>\2\2\u0141H\3\2\2\2\u0142\u0143\7@\2\2")
        buf.write("\u0143J\3\2\2\2\u0144\u0145\7>\2\2\u0145\u0146\7?\2\2")
        buf.write("\u0146L\3\2\2\2\u0147\u0148\7@\2\2\u0148\u0149\7?\2\2")
        buf.write("\u0149N\3\2\2\2\u014a\u014b\7~\2\2\u014b\u014c\7~\2\2")
        buf.write("\u014cP\3\2\2\2\u014d\u014e\7(\2\2\u014e\u014f\7(\2\2")
        buf.write("\u014fR\3\2\2\2\u0150\u0151\7#\2\2\u0151T\3\2\2\2\u0152")
        buf.write("\u0153\7`\2\2\u0153V\3\2\2\2\u0154\u0155\7<\2\2\u0155")
        buf.write("\u0156\7?\2\2\u0156X\3\2\2\2\u0157\u0158\7]\2\2\u0158")
        buf.write("Z\3\2\2\2\u0159\u015a\7_\2\2\u015a\\\3\2\2\2\u015b\u015c")
        buf.write("\7}\2\2\u015c^\3\2\2\2\u015d\u015e\7\177\2\2\u015e`\3")
        buf.write("\2\2\2\u015f\u0160\7*\2\2\u0160b\3\2\2\2\u0161\u0162\7")
        buf.write("+\2\2\u0162d\3\2\2\2\u0163\u0164\7=\2\2\u0164f\3\2\2\2")
        buf.write("\u0165\u0166\7<\2\2\u0166h\3\2\2\2\u0167\u0168\7\60\2")
        buf.write("\2\u0168j\3\2\2\2\u0169\u016a\7.\2\2\u016al\3\2\2\2\u016b")
        buf.write("\u016d\5w<\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016fn\3\2\2\2\u0170")
        buf.write("\u0172\5w<\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0176\5y=\2\u0176\u0187\3\2\2\2\u0177\u0179\5w")
        buf.write("<\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017d\5{>\2\u017d\u0187\3\2\2\2\u017e\u0180\5w<\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\5")
        buf.write("y=\2\u0184\u0185\5{>\2\u0185\u0187\3\2\2\2\u0186\u0171")
        buf.write("\3\2\2\2\u0186\u0178\3\2\2\2\u0186\u017f\3\2\2\2\u0187")
        buf.write("p\3\2\2\2\u0188\u018c\7$\2\2\u0189\u018b\5}?\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018f\u0190\7$\2\2\u0190\u0191\b9\3\2\u0191r\3\2\2\2")
        buf.write("\u0192\u0193\7a\2\2\u0193t\3\2\2\2\u0194\u0195\t\3\2\2")
        buf.write("\u0195v\3\2\2\2\u0196\u0197\t\4\2\2\u0197x\3\2\2\2\u0198")
        buf.write("\u019c\5i\65\2\u0199\u019b\5w<\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019dz\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a2\t\5\2")
        buf.write("\2\u01a0\u01a3\5\67\34\2\u01a1\u01a3\59\35\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a5\3\2\2\2\u01a4\u01a6\5w<\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8|\3\2\2\2\u01a9\u01ac\5\177@\2\u01aa\u01ac\n\6\2")
        buf.write("\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac~\3\2")
        buf.write("\2\2\u01ad\u01ae\7^\2\2\u01ae\u01af\t\7\2\2\u01af\u0080")
        buf.write("\3\2\2\2\u01b0\u01b3\5s:\2\u01b1\u01b3\5u;\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b9\3\2\2\2\u01b4")
        buf.write("\u01b8\5s:\2\u01b5\u01b8\5u;\2\u01b6\u01b8\5w<\2\u01b7")
        buf.write("\u01b4\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2")
        buf.write("\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3")
        buf.write("\2\2\2\u01ba\u0082\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01be")
        buf.write("\t\b\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01c2\bB\2\2\u01c2\u0084\3\2\2\2\u01c3\u01c4\13")
        buf.write("\2\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c6\13\2\2\2\u01c6")
        buf.write("\u0088\3\2\2\2\u01c7\u01c8\13\2\2\2\u01c8\u008a\3\2\2")
        buf.write("\2\25\2\u008f\u0093\u0097\u00a1\u016e\u0173\u017a\u0181")
        buf.write("\u0186\u018c\u019c\u01a2\u01a7\u01ab\u01b2\u01b7\u01b9")
        buf.write("\u01bf\4\b\2\2\39\2")
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
    STR_LIT = 56
    ID = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

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
            "FLOAT_LIT", "STR_LIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LINE_CMT", "BLOCK_CMT", "BOOLEAN", "BREAK", "CLASS", 
                  "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", 
                  "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                  "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                  "ADDOP", "SUBOP", "MULOP", "FLOAT_DIV", "INTEGER_DIV", 
                  "MOD", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                  "GREATER_OR_EQUAL", "OR", "AND", "NOT", "CONCATENATION", 
                  "ASSIGN", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI_COLONE", 
                  "COLON", "DOT", "COMMA", "INT_LIT", "FLOAT_LIT", "STR_LIT", 
                  "UNDERSCORE", "LETTER", "DIGIT", "DECIMAL", "EXPONENT", 
                  "CHAR", "ESC_SEQ", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[55] = self.STR_LIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[:];

     


