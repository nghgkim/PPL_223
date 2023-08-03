# Generated from /Users/nguyenkim/Downloads/initial 3/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01e7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\7\2\u008c\n\2\f\2\16\2\u008f\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\7\3\u0097\n\3\f\3\16\3\u009a\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\5\67\u0165\n\67\38\38\78\u0169\n8\f8\168\u016c")
        buf.write("\138\38\38\38\39\69\u0172\n9\r9\169\u0173\39\39\39\69")
        buf.write("\u0179\n9\r9\169\u017a\39\39\69\u017f\n9\r9\169\u0180")
        buf.write("\39\69\u0184\n9\r9\169\u0185\39\39\69\u018a\n9\r9\169")
        buf.write("\u018b\59\u018e\n9\39\39\59\u0192\n9\39\69\u0195\n9\r")
        buf.write("9\169\u0196\39\69\u019a\n9\r9\169\u019b\39\39\39\59\u01a1")
        buf.write("\n9\39\69\u01a4\n9\r9\169\u01a5\59\u01a8\n9\3:\6:\u01ab")
        buf.write("\n:\r:\16:\u01ac\3;\3;\7;\u01b1\n;\f;\16;\u01b4\13;\3")
        buf.write("<\3<\3=\3=\5=\u01ba\n=\3>\3>\3>\3?\3?\3?\5?\u01c2\n?\3")
        buf.write("@\6@\u01c5\n@\r@\16@\u01c6\3@\3@\3A\6A\u01cc\nA\rA\16")
        buf.write("A\u01cd\3A\3A\3B\3B\7B\u01d4\nB\fB\16B\u01d7\13B\3B\3")
        buf.write("B\3C\3C\7C\u01dd\nC\fC\16C\u01e0\13C\3C\3C\3C\3D\3D\3")
        buf.write("D\3\u0098\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:s;u<w\2y\2{\2}\2\177=\u0081>\u0083?\u0085@\u0087")
        buf.write("A\3\2\13\4\2\f\f\17\17\4\2GGgg\4\2--//\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2\62;\6\2\n\f\16\17$$^^\t\2$$^^ddhhpptt")
        buf.write("vv\5\2\13\13\16\17\"\"\2\u01fc\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u0092")
        buf.write("\3\2\2\2\7\u00a0\3\2\2\2\t\u00a8\3\2\2\2\13\u00ae\3\2")
        buf.write("\2\2\r\u00b4\3\2\2\2\17\u00bd\3\2\2\2\21\u00c0\3\2\2\2")
        buf.write("\23\u00c5\3\2\2\2\25\u00cd\3\2\2\2\27\u00d3\3\2\2\2\31")
        buf.write("\u00d6\3\2\2\2\33\u00da\3\2\2\2\35\u00de\3\2\2\2\37\u00e5")
        buf.write("\3\2\2\2!\u00ea\3\2\2\2#\u00ee\3\2\2\2%\u00f5\3\2\2\2")
        buf.write("\'\u00fa\3\2\2\2)\u00fe\3\2\2\2+\u0103\3\2\2\2-\u0109")
        buf.write("\3\2\2\2/\u0110\3\2\2\2\61\u0113\3\2\2\2\63\u011a\3\2")
        buf.write("\2\2\65\u011c\3\2\2\2\67\u011e\3\2\2\29\u0120\3\2\2\2")
        buf.write(";\u0122\3\2\2\2=\u0124\3\2\2\2?\u0126\3\2\2\2A\u0129\3")
        buf.write("\2\2\2C\u012c\3\2\2\2E\u012e\3\2\2\2G\u0130\3\2\2\2I\u0133")
        buf.write("\3\2\2\2K\u0136\3\2\2\2M\u0139\3\2\2\2O\u013c\3\2\2\2")
        buf.write("Q\u013e\3\2\2\2S\u0140\3\2\2\2U\u0142\3\2\2\2W\u0145\3")
        buf.write("\2\2\2Y\u0147\3\2\2\2[\u0149\3\2\2\2]\u014b\3\2\2\2_\u014d")
        buf.write("\3\2\2\2a\u014f\3\2\2\2c\u0151\3\2\2\2e\u0153\3\2\2\2")
        buf.write("g\u0155\3\2\2\2i\u0157\3\2\2\2k\u0159\3\2\2\2m\u0164\3")
        buf.write("\2\2\2o\u0166\3\2\2\2q\u01a7\3\2\2\2s\u01aa\3\2\2\2u\u01ae")
        buf.write("\3\2\2\2w\u01b5\3\2\2\2y\u01b9\3\2\2\2{\u01bb\3\2\2\2")
        buf.write("}\u01c1\3\2\2\2\177\u01c4\3\2\2\2\u0081\u01cb\3\2\2\2")
        buf.write("\u0083\u01d1\3\2\2\2\u0085\u01da\3\2\2\2\u0087\u01e4\3")
        buf.write("\2\2\2\u0089\u008d\7%\2\2\u008a\u008c\n\2\2\2\u008b\u008a")
        buf.write("\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0091\b\2\2\2\u0091\4\3\2\2\2\u0092\u0093\7\61")
        buf.write("\2\2\u0093\u0094\7,\2\2\u0094\u0098\3\2\2\2\u0095\u0097")
        buf.write("\13\2\2\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009b\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009b\u009c\7,\2\2\u009c\u009d\7")
        buf.write("\61\2\2\u009d\u009e\3\2\2\2\u009e\u009f\b\3\2\2\u009f")
        buf.write("\6\3\2\2\2\u00a0\u00a1\7d\2\2\u00a1\u00a2\7q\2\2\u00a2")
        buf.write("\u00a3\7q\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7g\2\2\u00a5")
        buf.write("\u00a6\7c\2\2\u00a6\u00a7\7p\2\2\u00a7\b\3\2\2\2\u00a8")
        buf.write("\u00a9\7d\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write("\u00ac\7c\2\2\u00ac\u00ad\7m\2\2\u00ad\n\3\2\2\2\u00ae")
        buf.write("\u00af\7e\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1\7c\2\2\u00b1")
        buf.write("\u00b2\7u\2\2\u00b2\u00b3\7u\2\2\u00b3\f\3\2\2\2\u00b4")
        buf.write("\u00b5\7e\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7p\2\2\u00b7")
        buf.write("\u00b8\7v\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba")
        buf.write("\u00bb\7w\2\2\u00bb\u00bc\7g\2\2\u00bc\16\3\2\2\2\u00bd")
        buf.write("\u00be\7f\2\2\u00be\u00bf\7q\2\2\u00bf\20\3\2\2\2\u00c0")
        buf.write("\u00c1\7g\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3\7u\2\2\u00c3")
        buf.write("\u00c4\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write("\u00c7\7z\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7g\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\24\3\2\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf\7n\2\2\u00cf")
        buf.write("\u00d0\7q\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\26\3\2\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7h\2\2\u00d5")
        buf.write("\30\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8")
        buf.write("\u00d9\7v\2\2\u00d9\32\3\2\2\2\u00da\u00db\7p\2\2\u00db")
        buf.write("\u00dc\7g\2\2\u00dc\u00dd\7y\2\2\u00dd\34\3\2\2\2\u00de")
        buf.write("\u00df\7u\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1")
        buf.write("\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4")
        buf.write("\36\3\2\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7j\2\2\u00e7")
        buf.write("\u00e8\7g\2\2\u00e8\u00e9\7p\2\2\u00e9 \3\2\2\2\u00ea")
        buf.write("\u00eb\7h\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\"\3\2\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0\7g\2\2\u00f0")
        buf.write("\u00f1\7v\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("\u00f4\7p\2\2\u00f4$\3\2\2\2\u00f5\u00f6\7x\2\2\u00f6")
        buf.write("\u00f7\7q\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7f\2\2\u00f9")
        buf.write("&\3\2\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7k\2\2\u00fc")
        buf.write("\u00fd\7n\2\2\u00fd(\3\2\2\2\u00fe\u00ff\7v\2\2\u00ff")
        buf.write("\u0100\7j\2\2\u0100\u0101\7k\2\2\u0101\u0102\7u\2\2\u0102")
        buf.write("*\3\2\2\2\u0103\u0104\7h\2\2\u0104\u0105\7k\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106\u0107\7c\2\2\u0107\u0108\7n\2\2\u0108")
        buf.write(",\3\2\2\2\u0109\u010a\7u\2\2\u010a\u010b\7v\2\2\u010b")
        buf.write("\u010c\7c\2\2\u010c\u010d\7v\2\2\u010d\u010e\7k\2\2\u010e")
        buf.write("\u010f\7e\2\2\u010f.\3\2\2\2\u0110\u0111\7v\2\2\u0111")
        buf.write("\u0112\7q\2\2\u0112\60\3\2\2\2\u0113\u0114\7f\2\2\u0114")
        buf.write("\u0115\7q\2\2\u0115\u0116\7y\2\2\u0116\u0117\7p\2\2\u0117")
        buf.write("\u0118\7v\2\2\u0118\u0119\7q\2\2\u0119\62\3\2\2\2\u011a")
        buf.write("\u011b\7-\2\2\u011b\64\3\2\2\2\u011c\u011d\7/\2\2\u011d")
        buf.write("\66\3\2\2\2\u011e\u011f\7,\2\2\u011f8\3\2\2\2\u0120\u0121")
        buf.write("\7\61\2\2\u0121:\3\2\2\2\u0122\u0123\7^\2\2\u0123<\3\2")
        buf.write("\2\2\u0124\u0125\7\'\2\2\u0125>\3\2\2\2\u0126\u0127\7")
        buf.write("#\2\2\u0127\u0128\7?\2\2\u0128@\3\2\2\2\u0129\u012a\7")
        buf.write("?\2\2\u012a\u012b\7?\2\2\u012bB\3\2\2\2\u012c\u012d\7")
        buf.write(">\2\2\u012dD\3\2\2\2\u012e\u012f\7@\2\2\u012fF\3\2\2\2")
        buf.write("\u0130\u0131\7>\2\2\u0131\u0132\7?\2\2\u0132H\3\2\2\2")
        buf.write("\u0133\u0134\7@\2\2\u0134\u0135\7?\2\2\u0135J\3\2\2\2")
        buf.write("\u0136\u0137\7~\2\2\u0137\u0138\7~\2\2\u0138L\3\2\2\2")
        buf.write("\u0139\u013a\7(\2\2\u013a\u013b\7(\2\2\u013bN\3\2\2\2")
        buf.write("\u013c\u013d\7#\2\2\u013dP\3\2\2\2\u013e\u013f\7`\2\2")
        buf.write("\u013fR\3\2\2\2\u0140\u0141\5\33\16\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7<\2\2\u0143\u0144\7?\2\2\u0144V\3\2\2\2\u0145")
        buf.write("\u0146\7?\2\2\u0146X\3\2\2\2\u0147\u0148\7]\2\2\u0148")
        buf.write("Z\3\2\2\2\u0149\u014a\7_\2\2\u014a\\\3\2\2\2\u014b\u014c")
        buf.write("\7}\2\2\u014c^\3\2\2\2\u014d\u014e\7\177\2\2\u014e`\3")
        buf.write("\2\2\2\u014f\u0150\7*\2\2\u0150b\3\2\2\2\u0151\u0152\7")
        buf.write("+\2\2\u0152d\3\2\2\2\u0153\u0154\7=\2\2\u0154f\3\2\2\2")
        buf.write("\u0155\u0156\7<\2\2\u0156h\3\2\2\2\u0157\u0158\7\60\2")
        buf.write("\2\u0158j\3\2\2\2\u0159\u015a\7.\2\2\u015al\3\2\2\2\u015b")
        buf.write("\u015c\7v\2\2\u015c\u015d\7t\2\2\u015d\u015e\7w\2\2\u015e")
        buf.write("\u0165\7g\2\2\u015f\u0160\7h\2\2\u0160\u0161\7c\2\2\u0161")
        buf.write("\u0162\7n\2\2\u0162\u0163\7u\2\2\u0163\u0165\7g\2\2\u0164")
        buf.write("\u015b\3\2\2\2\u0164\u015f\3\2\2\2\u0165n\3\2\2\2\u0166")
        buf.write("\u016a\7$\2\2\u0167\u0169\5y=\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016d\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\7")
        buf.write("$\2\2\u016e\u016f\b8\3\2\u016fp\3\2\2\2\u0170\u0172\5")
        buf.write("w<\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0176\5i\65\2\u0176\u01a8\3\2\2\2\u0177\u0179\5w<\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\5")
        buf.write("i\65\2\u017d\u017f\5w<\2\u017e\u017d\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u01a8\3\2\2\2\u0182\u0184\5w<\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u018d\3\2\2\2\u0187\u0189\5i\65\2\u0188\u018a\5")
        buf.write("w<\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u0187\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0191\t\3\2\2\u0190\u0192\t\4\2\2\u0191\u0190\3")
        buf.write("\2\2\2\u0191\u0192\3\2\2\2\u0192\u0194\3\2\2\2\u0193\u0195")
        buf.write("\5w<\2\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0194")
        buf.write("\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u01a8\3\2\2\2\u0198")
        buf.write("\u019a\5w<\2\u0199\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d\u019e\5i\65\2\u019e\u01a0\t\3\2\2\u019f\u01a1\t")
        buf.write("\4\2\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3")
        buf.write("\3\2\2\2\u01a2\u01a4\5w<\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a8\3\2\2\2\u01a7\u0171\3\2\2\2\u01a7\u0178\3\2\2\2")
        buf.write("\u01a7\u0183\3\2\2\2\u01a7\u0199\3\2\2\2\u01a8r\3\2\2")
        buf.write("\2\u01a9\u01ab\5w<\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01adt")
        buf.write("\3\2\2\2\u01ae\u01b2\t\5\2\2\u01af\u01b1\t\6\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3v\3\2\2\2\u01b4\u01b2\3\2\2")
        buf.write("\2\u01b5\u01b6\t\7\2\2\u01b6x\3\2\2\2\u01b7\u01ba\n\b")
        buf.write("\2\2\u01b8\u01ba\5{>\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01baz\3\2\2\2\u01bb\u01bc\7^\2\2\u01bc\u01bd")
        buf.write("\t\t\2\2\u01bd|\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c2")
        buf.write("\n\t\2\2\u01c0\u01c2\7^\2\2\u01c1\u01be\3\2\2\2\u01c1")
        buf.write("\u01c0\3\2\2\2\u01c2~\3\2\2\2\u01c3\u01c5\t\n\2\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\b")
        buf.write("@\2\2\u01c9\u0080\3\2\2\2\u01ca\u01cc\7\f\2\2\u01cb\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\bA\2\2")
        buf.write("\u01d0\u0082\3\2\2\2\u01d1\u01d5\7$\2\2\u01d2\u01d4\5")
        buf.write("y=\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01d9\bB\4\2\u01d9\u0084\3\2\2\2")
        buf.write("\u01da\u01de\7$\2\2\u01db\u01dd\5y=\2\u01dc\u01db\3\2")
        buf.write("\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df")
        buf.write("\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1")
        buf.write("\u01e2\5}?\2\u01e2\u01e3\bC\5\2\u01e3\u0086\3\2\2\2\u01e4")
        buf.write("\u01e5\13\2\2\2\u01e5\u01e6\bD\6\2\u01e6\u0088\3\2\2\2")
        buf.write("\33\2\u008d\u0098\u0164\u016a\u0173\u017a\u0180\u0185")
        buf.write("\u018b\u018d\u0191\u0196\u019b\u01a0\u01a5\u01a7\u01ac")
        buf.write("\u01b2\u01b9\u01c1\u01c6\u01cd\u01d5\u01de\7\b\2\2\38")
        buf.write("\2\3B\3\3C\4\3D\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMAT = 1
    BLOCK_COMMAT = 2
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
    VOID = 18
    NIL = 19
    THIS = 20
    FINAL = 21
    STATIC = 22
    TO = 23
    DOWNTO = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    INT_DIV = 29
    MOD = 30
    NOT_EQUAL = 31
    EQUAL = 32
    LT = 33
    GT = 34
    LE = 35
    GE = 36
    OR = 37
    AND = 38
    NOT = 39
    CONCATENATION = 40
    NEW_OP = 41
    ASSINGMENT = 42
    ASSIGN = 43
    LSB = 44
    RSB = 45
    LP = 46
    RP = 47
    LB = 48
    RB = 49
    SEMI = 50
    CL = 51
    DOT = 52
    COMMA = 53
    BOOLLIT = 54
    STRINGLIT = 55
    FLOATLIT = 56
    INTLIT = 57
    ID = 58
    WS = 59
    NEWLINE = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'void'", "'nil'", "'this'", 
            "'final'", "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
            "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", 
            "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", "'='", "'['", 
            "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMAT", "BLOCK_COMMAT", "BOOLEAN", "BREAK", "CLASS", 
            "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
            "STRING", "THEN", "FOR", "RETURN", "VOID", "NIL", "THIS", "FINAL", 
            "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", "DIV", "INT_DIV", 
            "MOD", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", "OR", "AND", 
            "NOT", "CONCATENATION", "NEW_OP", "ASSINGMENT", "ASSIGN", "LSB", 
            "RSB", "LP", "RP", "LB", "RB", "SEMI", "CL", "DOT", "COMMA", 
            "BOOLLIT", "STRINGLIT", "FLOATLIT", "INTLIT", "ID", "WS", "NEWLINE", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMAT", "BLOCK_COMMAT", "BOOLEAN", "BREAK", "CLASS", 
                  "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", 
                  "NEW", "STRING", "THEN", "FOR", "RETURN", "VOID", "NIL", 
                  "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", 
                  "MUL", "DIV", "INT_DIV", "MOD", "NOT_EQUAL", "EQUAL", 
                  "LT", "GT", "LE", "GE", "OR", "AND", "NOT", "CONCATENATION", 
                  "NEW_OP", "ASSINGMENT", "ASSIGN", "LSB", "RSB", "LP", 
                  "RP", "LB", "RB", "SEMI", "CL", "DOT", "COMMA", "BOOLLIT", 
                  "STRINGLIT", "FLOATLIT", "INTLIT", "ID", "DIGIT", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "WS", "NEWLINE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[54] = self.STRINGLIT_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[:]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise ErrorToken(self.text)
            	
     


