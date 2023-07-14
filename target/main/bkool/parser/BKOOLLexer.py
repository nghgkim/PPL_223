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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01ea\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\7\2\u0092\n\2\f\2\16")
        buf.write("\2\u0095\13\2\3\2\5\2\u0098\n\2\3\2\3\2\5\2\u009c\n\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00a4\n\3\f\3\16\3\u00a7")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\6\67\u0171\n\67\r\67\16\67\u0172\38\38\58\u0177")
        buf.write("\n8\39\69\u017a\n9\r9\169\u017b\39\39\39\69\u0181\n9\r")
        buf.write("9\169\u0182\39\39\39\69\u0188\n9\r9\169\u0189\39\39\3")
        buf.write("9\59\u018f\n9\3:\3:\7:\u0193\n:\f:\16:\u0196\13:\3:\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3>\3>\7>\u01a3\n>\f>\16>\u01a6")
        buf.write("\13>\3?\3?\3?\5?\u01ab\n?\3?\6?\u01ae\n?\r?\16?\u01af")
        buf.write("\3@\3@\5@\u01b4\n@\3A\3A\3A\3B\3B\3B\5B\u01bc\nB\3C\3")
        buf.write("C\5C\u01c0\nC\3C\3C\3C\7C\u01c5\nC\fC\16C\u01c8\13C\3")
        buf.write("D\3D\7D\u01cc\nD\fD\16D\u01cf\13D\3D\3D\5D\u01d3\nD\3")
        buf.write("D\3D\3E\3E\7E\u01d9\nE\fE\16E\u01dc\13E\3E\3E\3E\3F\3")
        buf.write("F\3F\3G\6G\u01e5\nG\rG\16G\u01e6\3G\3G\3\u00a5\2H\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085<\u0087=\u0089")
        buf.write(">\u008b?\u008d@\3\2\f\4\2\f\f\17\17\4\2C\\c|\3\2\62;\4")
        buf.write("\2GGgg\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\3\2^^\6\2\f")
        buf.write("\f\17\17GHQQ\3\2$$\5\2\13\f\17\17\"\"\2\u01fb\2\3\3\2")
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
        buf.write("\2s\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3")
        buf.write("\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2")
        buf.write("\5\u009f\3\2\2\2\7\u00ad\3\2\2\2\t\u00b5\3\2\2\2\13\u00bb")
        buf.write("\3\2\2\2\r\u00c1\3\2\2\2\17\u00ca\3\2\2\2\21\u00cd\3\2")
        buf.write("\2\2\23\u00d2\3\2\2\2\25\u00da\3\2\2\2\27\u00e0\3\2\2")
        buf.write("\2\31\u00e3\3\2\2\2\33\u00e7\3\2\2\2\35\u00eb\3\2\2\2")
        buf.write("\37\u00f2\3\2\2\2!\u00f7\3\2\2\2#\u00fb\3\2\2\2%\u0102")
        buf.write("\3\2\2\2\'\u0107\3\2\2\2)\u010d\3\2\2\2+\u0112\3\2\2\2")
        buf.write("-\u0116\3\2\2\2/\u011b\3\2\2\2\61\u0121\3\2\2\2\63\u0128")
        buf.write("\3\2\2\2\65\u012b\3\2\2\2\67\u0132\3\2\2\29\u0134\3\2")
        buf.write("\2\2;\u0136\3\2\2\2=\u0138\3\2\2\2?\u013a\3\2\2\2A\u013c")
        buf.write("\3\2\2\2C\u013e\3\2\2\2E\u0141\3\2\2\2G\u0144\3\2\2\2")
        buf.write("I\u0146\3\2\2\2K\u0148\3\2\2\2M\u014b\3\2\2\2O\u014e\3")
        buf.write("\2\2\2Q\u0151\3\2\2\2S\u0154\3\2\2\2U\u0156\3\2\2\2W\u0158")
        buf.write("\3\2\2\2Y\u015b\3\2\2\2[\u015d\3\2\2\2]\u015f\3\2\2\2")
        buf.write("_\u0161\3\2\2\2a\u0163\3\2\2\2c\u0165\3\2\2\2e\u0167\3")
        buf.write("\2\2\2g\u0169\3\2\2\2i\u016b\3\2\2\2k\u016d\3\2\2\2m\u0170")
        buf.write("\3\2\2\2o\u0176\3\2\2\2q\u018e\3\2\2\2s\u0190\3\2\2\2")
        buf.write("u\u019a\3\2\2\2w\u019c\3\2\2\2y\u019e\3\2\2\2{\u01a0\3")
        buf.write("\2\2\2}\u01a7\3\2\2\2\177\u01b3\3\2\2\2\u0081\u01b5\3")
        buf.write("\2\2\2\u0083\u01bb\3\2\2\2\u0085\u01bf\3\2\2\2\u0087\u01c9")
        buf.write("\3\2\2\2\u0089\u01d6\3\2\2\2\u008b\u01e0\3\2\2\2\u008d")
        buf.write("\u01e4\3\2\2\2\u008f\u0093\7%\2\2\u0090\u0092\n\2\2\2")
        buf.write("\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\u009b\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0096\u0098\7\17\2\2\u0097\u0096\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009c\7\f\2\2")
        buf.write("\u009a\u009c\7\2\2\3\u009b\u0097\3\2\2\2\u009b\u009a\3")
        buf.write("\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\b\2\2\2\u009e\4")
        buf.write("\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0\u00a1\7,\2\2\u00a1")
        buf.write("\u00a5\3\2\2\2\u00a2\u00a4\13\2\2\2\u00a3\u00a2\3\2\2")
        buf.write("\2\u00a4\u00a7\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8")
        buf.write("\u00a9\7,\2\2\u00a9\u00aa\7\61\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\b\3\2\2\u00ac\6\3\2\2\2\u00ad\u00ae\7d\2")
        buf.write("\2\u00ae\u00af\7q\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7")
        buf.write("n\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\b\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7m\2\2\u00ba\n\3\2\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd")
        buf.write("\7n\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\f\3\2\2\2\u00c1\u00c2\7e\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\16\3\2\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\20\3\2\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7g\2\2\u00d1\22")
        buf.write("\3\2\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7z\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7u\2\2\u00d9\24\3\2\2\2\u00da\u00db")
        buf.write("\7h\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7v\2\2\u00df\26\3\2\2\2\u00e0\u00e1")
        buf.write("\7k\2\2\u00e1\u00e2\7h\2\2\u00e2\30\3\2\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6\32")
        buf.write("\3\2\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7y\2\2\u00ea\34\3\2\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7i\2\2\u00f1\36\3\2\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7j\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6 \3\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9")
        buf.write("\7q\2\2\u00f9\u00fa\7t\2\2\u00fa\"\3\2\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7w\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7p\2\2\u0101$\3")
        buf.write("\2\2\2\u0102\u0103\7v\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7w\2\2\u0105\u0106\7g\2\2\u0106&\3\2\2\2\u0107\u0108")
        buf.write("\7h\2\2\u0108\u0109\7c\2\2\u0109\u010a\7n\2\2\u010a\u010b")
        buf.write("\7u\2\2\u010b\u010c\7g\2\2\u010c(\3\2\2\2\u010d\u010e")
        buf.write("\7x\2\2\u010e\u010f\7q\2\2\u010f\u0110\7k\2\2\u0110\u0111")
        buf.write("\7f\2\2\u0111*\3\2\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7n\2\2\u0115,\3\2\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117\u0118\7j\2\2\u0118\u0119\7k\2\2\u0119\u011a")
        buf.write("\7u\2\2\u011a.\3\2\2\2\u011b\u011c\7h\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7p\2\2\u011e\u011f\7c\2\2\u011f\u0120")
        buf.write("\7n\2\2\u0120\60\3\2\2\2\u0121\u0122\7u\2\2\u0122\u0123")
        buf.write("\7v\2\2\u0123\u0124\7c\2\2\u0124\u0125\7v\2\2\u0125\u0126")
        buf.write("\7k\2\2\u0126\u0127\7e\2\2\u0127\62\3\2\2\2\u0128\u0129")
        buf.write("\7v\2\2\u0129\u012a\7q\2\2\u012a\64\3\2\2\2\u012b\u012c")
        buf.write("\7f\2\2\u012c\u012d\7q\2\2\u012d\u012e\7y\2\2\u012e\u012f")
        buf.write("\7p\2\2\u012f\u0130\7v\2\2\u0130\u0131\7q\2\2\u0131\66")
        buf.write("\3\2\2\2\u0132\u0133\7-\2\2\u01338\3\2\2\2\u0134\u0135")
        buf.write("\7/\2\2\u0135:\3\2\2\2\u0136\u0137\7,\2\2\u0137<\3\2\2")
        buf.write("\2\u0138\u0139\7\61\2\2\u0139>\3\2\2\2\u013a\u013b\7^")
        buf.write("\2\2\u013b@\3\2\2\2\u013c\u013d\7\'\2\2\u013dB\3\2\2\2")
        buf.write("\u013e\u013f\7#\2\2\u013f\u0140\7?\2\2\u0140D\3\2\2\2")
        buf.write("\u0141\u0142\7?\2\2\u0142\u0143\7?\2\2\u0143F\3\2\2\2")
        buf.write("\u0144\u0145\7>\2\2\u0145H\3\2\2\2\u0146\u0147\7@\2\2")
        buf.write("\u0147J\3\2\2\2\u0148\u0149\7>\2\2\u0149\u014a\7?\2\2")
        buf.write("\u014aL\3\2\2\2\u014b\u014c\7@\2\2\u014c\u014d\7?\2\2")
        buf.write("\u014dN\3\2\2\2\u014e\u014f\7~\2\2\u014f\u0150\7~\2\2")
        buf.write("\u0150P\3\2\2\2\u0151\u0152\7(\2\2\u0152\u0153\7(\2\2")
        buf.write("\u0153R\3\2\2\2\u0154\u0155\7#\2\2\u0155T\3\2\2\2\u0156")
        buf.write("\u0157\7`\2\2\u0157V\3\2\2\2\u0158\u0159\7<\2\2\u0159")
        buf.write("\u015a\7?\2\2\u015aX\3\2\2\2\u015b\u015c\7]\2\2\u015c")
        buf.write("Z\3\2\2\2\u015d\u015e\7_\2\2\u015e\\\3\2\2\2\u015f\u0160")
        buf.write("\7}\2\2\u0160^\3\2\2\2\u0161\u0162\7\177\2\2\u0162`\3")
        buf.write("\2\2\2\u0163\u0164\7*\2\2\u0164b\3\2\2\2\u0165\u0166\7")
        buf.write("+\2\2\u0166d\3\2\2\2\u0167\u0168\7=\2\2\u0168f\3\2\2\2")
        buf.write("\u0169\u016a\7<\2\2\u016ah\3\2\2\2\u016b\u016c\7\60\2")
        buf.write("\2\u016cj\3\2\2\2\u016d\u016e\7.\2\2\u016el\3\2\2\2\u016f")
        buf.write("\u0171\5y=\2\u0170\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173n\3\2\2\2\u0174")
        buf.write("\u0177\5%\23\2\u0175\u0177\5\'\24\2\u0176\u0174\3\2\2")
        buf.write("\2\u0176\u0175\3\2\2\2\u0177p\3\2\2\2\u0178\u017a\5y=")
        buf.write("\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017e\5{>\2\u017e\u018f\3\2\2\2\u017f\u0181\5y=\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\5")
        buf.write("}?\2\u0185\u018f\3\2\2\2\u0186\u0188\5y=\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\5{>\2\u018c")
        buf.write("\u018d\5}?\2\u018d\u018f\3\2\2\2\u018e\u0179\3\2\2\2\u018e")
        buf.write("\u0180\3\2\2\2\u018e\u0187\3\2\2\2\u018fr\3\2\2\2\u0190")
        buf.write("\u0194\7$\2\2\u0191\u0193\5\177@\2\u0192\u0191\3\2\2\2")
        buf.write("\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3")
        buf.write("\2\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0198")
        buf.write("\7$\2\2\u0198\u0199\b:\3\2\u0199t\3\2\2\2\u019a\u019b")
        buf.write("\7a\2\2\u019bv\3\2\2\2\u019c\u019d\t\3\2\2\u019dx\3\2")
        buf.write("\2\2\u019e\u019f\t\4\2\2\u019fz\3\2\2\2\u01a0\u01a4\5")
        buf.write("i\65\2\u01a1\u01a3\5y=\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("|\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01aa\t\5\2\2\u01a8")
        buf.write("\u01ab\5\67\34\2\u01a9\u01ab\59\35\2\u01aa\u01a8\3\2\2")
        buf.write("\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad")
        buf.write("\3\2\2\2\u01ac\u01ae\5y=\2\u01ad\u01ac\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("~\3\2\2\2\u01b1\u01b4\5\u0081A\2\u01b2\u01b4\n\6\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4\u0080\3\2\2\2")
        buf.write("\u01b5\u01b6\7^\2\2\u01b6\u01b7\t\7\2\2\u01b7\u0082\3")
        buf.write("\2\2\2\u01b8\u01b9\7^\2\2\u01b9\u01bc\n\7\2\2\u01ba\u01bc")
        buf.write("\n\b\2\2\u01bb\u01b8\3\2\2\2\u01bb\u01ba\3\2\2\2\u01bc")
        buf.write("\u0084\3\2\2\2\u01bd\u01c0\5u;\2\u01be\u01c0\5w<\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c6\3\2\2\2")
        buf.write("\u01c1\u01c5\5u;\2\u01c2\u01c5\5w<\2\u01c3\u01c5\5y=\2")
        buf.write("\u01c4\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3")
        buf.write("\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u0086\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9")
        buf.write("\u01cd\7$\2\2\u01ca\u01cc\5\177@\2\u01cb\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01d2\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d3")
        buf.write("\t\t\2\2\u01d1\u01d3\n\n\2\2\u01d2\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\bD\4\2")
        buf.write("\u01d5\u0088\3\2\2\2\u01d6\u01da\7$\2\2\u01d7\u01d9\5")
        buf.write("\177@\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dd\u01de\5\u0083B\2\u01de\u01df")
        buf.write("\bE\5\2\u01df\u008a\3\2\2\2\u01e0\u01e1\13\2\2\2\u01e1")
        buf.write("\u01e2\bF\6\2\u01e2\u008c\3\2\2\2\u01e3\u01e5\t\13\2\2")
        buf.write("\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e4\3")
        buf.write("\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9")
        buf.write("\bG\2\2\u01e9\u008e\3\2\2\2\32\2\u0093\u0097\u009b\u00a5")
        buf.write("\u0172\u0176\u017b\u0182\u0189\u018e\u0194\u01a4\u01aa")
        buf.write("\u01af\u01b3\u01bb\u01bf\u01c4\u01c6\u01cd\u01d2\u01da")
        buf.write("\u01e6\7\b\2\2\3:\2\3D\3\3E\4\3F\5")
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
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61
    WS = 62

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
            "FLOAT_LIT", "STR_LIT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR", "WS" ]

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
                  "EXPONENT", "CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ID", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR", "WS" ]

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
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1];

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	err_char = ['\r','\n',EOFError]
            	if self.text[-1] in err_char:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text)

     


