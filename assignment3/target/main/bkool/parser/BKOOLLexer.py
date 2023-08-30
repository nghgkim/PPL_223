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
        buf.write("\u01e4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\5")
        buf.write("\2\u0098\n\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00a0\n\3\f\3")
        buf.write("\16\3\u00a3\13\3\3\3\3\3\3\3\5\3\u00a8\n\3\3\4\3\4\7\4")
        buf.write("\u00ac\n\4\f\4\16\4\u00af\13\4\3\4\5\4\u00b2\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0184\n:\3;\3;\3<\6<\u0189")
        buf.write("\n<\r<\16<\u018a\3=\3=\3>\3>\3?\3?\5?\u0193\n?\3@\3@\5")
        buf.write("@\u0197\n@\3@\3@\3A\3A\5A\u019d\nA\3B\3B\7B\u01a1\nB\f")
        buf.write("B\16B\u01a4\13B\3B\3B\3C\3C\7C\u01aa\nC\fC\16C\u01ad\13")
        buf.write("C\3C\3C\3D\3D\7D\u01b3\nD\fD\16D\u01b6\13D\3D\3D\3D\3")
        buf.write("E\3E\5E\u01bd\nE\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\5F\u01cd\nF\3G\3G\3G\5G\u01d2\nG\3H\3H\7H\u01d6\n")
        buf.write("H\fH\16H\u01d9\13H\3I\6I\u01dc\nI\rI\16I\u01dd\3I\3I\3")
        buf.write("J\3J\3J\3\u00a1\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\2\61\2\63\31\65\32\67\339\34;\35=\36")
        buf.write("?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63")
        buf.write("i\64k\65m\66o\67q8s9u\2w\2y\2{\2}\2\177\2\u0081:\u0083")
        buf.write(";\u0085<\u0087=\u0089\2\u008b\2\u008d\2\u008f>\u0091?")
        buf.write("\u0093@\3\2\13\3\2\f\f\3\2\62;\4\2GGgg\4\2--//\6\2\n\f")
        buf.write("\16\17$$^^\t\2$$^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\5\2\13\f\17\17\"\"\2\u01f0\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\3\u0097\3\2\2\2\5\u009b\3\2\2")
        buf.write("\2\7\u00a9\3\2\2\2\t\u00b3\3\2\2\2\13\u00bb\3\2\2\2\r")
        buf.write("\u00bf\3\2\2\2\17\u00c5\3\2\2\2\21\u00cc\3\2\2\2\23\u00d1")
        buf.write("\3\2\2\2\25\u00d4\3\2\2\2\27\u00d9\3\2\2\2\31\u00de\3")
        buf.write("\2\2\2\33\u00e2\3\2\2\2\35\u00e5\3\2\2\2\37\u00ec\3\2")
        buf.write("\2\2!\u00ef\3\2\2\2#\u00f5\3\2\2\2%\u00fe\3\2\2\2\'\u0104")
        buf.write("\3\2\2\2)\u010c\3\2\2\2+\u0111\3\2\2\2-\u0117\3\2\2\2")
        buf.write("/\u011e\3\2\2\2\61\u0123\3\2\2\2\63\u0129\3\2\2\2\65\u012d")
        buf.write("\3\2\2\2\67\u0131\3\2\2\29\u0138\3\2\2\2;\u013a\3\2\2")
        buf.write("\2=\u013c\3\2\2\2?\u013e\3\2\2\2A\u0140\3\2\2\2C\u0142")
        buf.write("\3\2\2\2E\u0144\3\2\2\2G\u0147\3\2\2\2I\u014a\3\2\2\2")
        buf.write("K\u014c\3\2\2\2M\u014e\3\2\2\2O\u0151\3\2\2\2Q\u0154\3")
        buf.write("\2\2\2S\u0157\3\2\2\2U\u015a\3\2\2\2W\u015c\3\2\2\2Y\u015e")
        buf.write("\3\2\2\2[\u0161\3\2\2\2]\u0163\3\2\2\2_\u0165\3\2\2\2")
        buf.write("a\u0167\3\2\2\2c\u0169\3\2\2\2e\u016b\3\2\2\2g\u016d\3")
        buf.write("\2\2\2i\u016f\3\2\2\2k\u0171\3\2\2\2m\u0173\3\2\2\2o\u0175")
        buf.write("\3\2\2\2q\u0177\3\2\2\2s\u0183\3\2\2\2u\u0185\3\2\2\2")
        buf.write("w\u0188\3\2\2\2y\u018c\3\2\2\2{\u018e\3\2\2\2}\u0190\3")
        buf.write("\2\2\2\177\u0194\3\2\2\2\u0081\u019c\3\2\2\2\u0083\u019e")
        buf.write("\3\2\2\2\u0085\u01a7\3\2\2\2\u0087\u01b0\3\2\2\2\u0089")
        buf.write("\u01bc\3\2\2\2\u008b\u01cc\3\2\2\2\u008d\u01d1\3\2\2\2")
        buf.write("\u008f\u01d3\3\2\2\2\u0091\u01db\3\2\2\2\u0093\u01e1\3")
        buf.write("\2\2\2\u0095\u0098\5\5\3\2\u0096\u0098\5\7\4\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009a\b\2\2\2\u009a\4\3\2\2\2\u009b\u009c\7\61\2\2\u009c")
        buf.write("\u009d\7,\2\2\u009d\u00a1\3\2\2\2\u009e\u00a0\13\2\2\2")
        buf.write("\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a7\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a4\u00a5\7,\2\2\u00a5\u00a8\7\61\2\2\u00a6")
        buf.write("\u00a8\7\2\2\3\u00a7\u00a4\3\2\2\2\u00a7\u00a6\3\2\2\2")
        buf.write("\u00a8\6\3\2\2\2\u00a9\u00ad\7%\2\2\u00aa\u00ac\n\2\2")
        buf.write("\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00b0\u00b2\7\2\2\3\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\b\3\2\2\2\u00b3\u00b4\7d\2")
        buf.write("\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7")
        buf.write("n\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\n\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\u00be\7v\2\2\u00be\f\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\16\3\2\2\2\u00c5\u00c6")
        buf.write("\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\20")
        buf.write("\3\2\2\2\u00cc\u00cd\7x\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7f\2\2\u00d0\22\3\2\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7h\2\2\u00d3\24\3\2\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\u00d6\7j\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\26\3\2\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7g\2\2\u00dd\30")
        buf.write("\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\32\3\2\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7y\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\u00eb\7q\2\2\u00eb\36\3\2\2\2\u00ec\u00ed")
        buf.write("\7f\2\2\u00ed\u00ee\7q\2\2\u00ee \3\2\2\2\u00ef\u00f0")
        buf.write("\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7m\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7e\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7w\2\2\u00fc\u00fd\7g\2\2\u00fd$\3\2\2\2\u00fe\u00ff")
        buf.write("\7e\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7c\2\2\u0101\u0102")
        buf.write("\7u\2\2\u0102\u0103\7u\2\2\u0103&\3\2\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105\u0106\7z\2\2\u0106\u0107\7v\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7p\2\2\u0109\u010a\7f\2\2\u010a\u010b")
        buf.write("\7u\2\2\u010b(\3\2\2\2\u010c\u010d\7v\2\2\u010d\u010e")
        buf.write("\7j\2\2\u010e\u010f\7k\2\2\u010f\u0110\7u\2\2\u0110*\3")
        buf.write("\2\2\2\u0111\u0112\7h\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7c\2\2\u0115\u0116\7n\2\2\u0116,\3")
        buf.write("\2\2\2\u0117\u0118\7u\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7v\2\2\u011b\u011c\7k\2\2\u011c\u011d")
        buf.write("\7e\2\2\u011d.\3\2\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120\u0121\7w\2\2\u0121\u0122\7g\2\2\u0122\60")
        buf.write("\3\2\2\2\u0123\u0124\7h\2\2\u0124\u0125\7c\2\2\u0125\u0126")
        buf.write("\7n\2\2\u0126\u0127\7u\2\2\u0127\u0128\7g\2\2\u0128\62")
        buf.write("\3\2\2\2\u0129\u012a\7p\2\2\u012a\u012b\7k\2\2\u012b\u012c")
        buf.write("\7n\2\2\u012c\64\3\2\2\2\u012d\u012e\7p\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012f\u0130\7y\2\2\u0130\66\3\2\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7w\2\2\u0135\u0136\7t\2\2\u0136\u0137\7p\2\2\u01378\3")
        buf.write("\2\2\2\u0138\u0139\7-\2\2\u0139:\3\2\2\2\u013a\u013b\7")
        buf.write("/\2\2\u013b<\3\2\2\2\u013c\u013d\7,\2\2\u013d>\3\2\2\2")
        buf.write("\u013e\u013f\7\61\2\2\u013f@\3\2\2\2\u0140\u0141\7^\2")
        buf.write("\2\u0141B\3\2\2\2\u0142\u0143\7\'\2\2\u0143D\3\2\2\2\u0144")
        buf.write("\u0145\7#\2\2\u0145\u0146\7?\2\2\u0146F\3\2\2\2\u0147")
        buf.write("\u0148\7?\2\2\u0148\u0149\7?\2\2\u0149H\3\2\2\2\u014a")
        buf.write("\u014b\7>\2\2\u014bJ\3\2\2\2\u014c\u014d\7@\2\2\u014d")
        buf.write("L\3\2\2\2\u014e\u014f\7>\2\2\u014f\u0150\7?\2\2\u0150")
        buf.write("N\3\2\2\2\u0151\u0152\7@\2\2\u0152\u0153\7?\2\2\u0153")
        buf.write("P\3\2\2\2\u0154\u0155\7~\2\2\u0155\u0156\7~\2\2\u0156")
        buf.write("R\3\2\2\2\u0157\u0158\7(\2\2\u0158\u0159\7(\2\2\u0159")
        buf.write("T\3\2\2\2\u015a\u015b\7#\2\2\u015bV\3\2\2\2\u015c\u015d")
        buf.write("\7`\2\2\u015dX\3\2\2\2\u015e\u015f\7<\2\2\u015f\u0160")
        buf.write("\7?\2\2\u0160Z\3\2\2\2\u0161\u0162\7?\2\2\u0162\\\3\2")
        buf.write("\2\2\u0163\u0164\7]\2\2\u0164^\3\2\2\2\u0165\u0166\7_")
        buf.write("\2\2\u0166`\3\2\2\2\u0167\u0168\7}\2\2\u0168b\3\2\2\2")
        buf.write("\u0169\u016a\7\177\2\2\u016ad\3\2\2\2\u016b\u016c\7*\2")
        buf.write("\2\u016cf\3\2\2\2\u016d\u016e\7+\2\2\u016eh\3\2\2\2\u016f")
        buf.write("\u0170\7=\2\2\u0170j\3\2\2\2\u0171\u0172\7<\2\2\u0172")
        buf.write("l\3\2\2\2\u0173\u0174\7\60\2\2\u0174n\3\2\2\2\u0175\u0176")
        buf.write("\7.\2\2\u0176p\3\2\2\2\u0177\u0178\5w<\2\u0178r\3\2\2")
        buf.write("\2\u0179\u017a\5w<\2\u017a\u017b\5}?\2\u017b\u017c\5\177")
        buf.write("@\2\u017c\u0184\3\2\2\2\u017d\u017e\5w<\2\u017e\u017f")
        buf.write("\5}?\2\u017f\u0184\3\2\2\2\u0180\u0181\5w<\2\u0181\u0182")
        buf.write("\5\177@\2\u0182\u0184\3\2\2\2\u0183\u0179\3\2\2\2\u0183")
        buf.write("\u017d\3\2\2\2\u0183\u0180\3\2\2\2\u0184t\3\2\2\2\u0185")
        buf.write("\u0186\t\3\2\2\u0186v\3\2\2\2\u0187\u0189\5u;\2\u0188")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u0188\3\2\2\2")
        buf.write("\u018a\u018b\3\2\2\2\u018bx\3\2\2\2\u018c\u018d\t\4\2")
        buf.write("\2\u018dz\3\2\2\2\u018e\u018f\t\5\2\2\u018f|\3\2\2\2\u0190")
        buf.write("\u0192\5m\67\2\u0191\u0193\5w<\2\u0192\u0191\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193~\3\2\2\2\u0194\u0196\5y=\2\u0195")
        buf.write("\u0197\5{>\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u0199\5w<\2\u0199\u0080\3\2\2\2\u019a")
        buf.write("\u019d\5/\30\2\u019b\u019d\5\61\31\2\u019c\u019a\3\2\2")
        buf.write("\2\u019c\u019b\3\2\2\2\u019d\u0082\3\2\2\2\u019e\u01a2")
        buf.write("\7$\2\2\u019f\u01a1\5\u0089E\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a5\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\7")
        buf.write("$\2\2\u01a6\u0084\3\2\2\2\u01a7\u01ab\7$\2\2\u01a8\u01aa")
        buf.write("\5\u0089E\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2")
        buf.write("\u01ad\u01ab\3\2\2\2\u01ae\u01af\bC\3\2\u01af\u0086\3")
        buf.write("\2\2\2\u01b0\u01b4\7$\2\2\u01b1\u01b3\5\u0089E\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01b4\3")
        buf.write("\2\2\2\u01b7\u01b8\5\u008dG\2\u01b8\u01b9\bD\4\2\u01b9")
        buf.write("\u0088\3\2\2\2\u01ba\u01bd\n\6\2\2\u01bb\u01bd\5\u008b")
        buf.write("F\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd\u008a")
        buf.write("\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01cd\7d\2\2\u01c0\u01c1")
        buf.write("\7^\2\2\u01c1\u01cd\7h\2\2\u01c2\u01c3\7^\2\2\u01c3\u01cd")
        buf.write("\7t\2\2\u01c4\u01c5\7^\2\2\u01c5\u01cd\7p\2\2\u01c6\u01c7")
        buf.write("\7^\2\2\u01c7\u01cd\7v\2\2\u01c8\u01c9\7^\2\2\u01c9\u01cd")
        buf.write("\7$\2\2\u01ca\u01cb\7^\2\2\u01cb\u01cd\7^\2\2\u01cc\u01be")
        buf.write("\3\2\2\2\u01cc\u01c0\3\2\2\2\u01cc\u01c2\3\2\2\2\u01cc")
        buf.write("\u01c4\3\2\2\2\u01cc\u01c6\3\2\2\2\u01cc\u01c8\3\2\2\2")
        buf.write("\u01cc\u01ca\3\2\2\2\u01cd\u008c\3\2\2\2\u01ce\u01cf\7")
        buf.write("^\2\2\u01cf\u01d2\n\7\2\2\u01d0\u01d2\7^\2\2\u01d1\u01ce")
        buf.write("\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2\u008e\3\2\2\2\u01d3")
        buf.write("\u01d7\t\b\2\2\u01d4\u01d6\t\t\2\2\u01d5\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3")
        buf.write("\2\2\2\u01d8\u0090\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01dc")
        buf.write("\t\n\2\2\u01db\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e0\bI\2\2\u01e0\u0092\3\2\2\2\u01e1\u01e2\13")
        buf.write("\2\2\2\u01e2\u01e3\bJ\5\2\u01e3\u0094\3\2\2\2\25\2\u0097")
        buf.write("\u00a1\u00a7\u00ad\u00b1\u0183\u018a\u0192\u0196\u019c")
        buf.write("\u01a2\u01ab\u01b4\u01bc\u01cc\u01d1\u01d7\u01dd\6\b\2")
        buf.write("\2\3C\2\3D\3\3J\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    BOOLEAN = 4
    INT = 5
    FLOAT = 6
    STRING = 7
    VOID = 8
    IF = 9
    THEN = 10
    ELSE = 11
    FOR = 12
    TO = 13
    DOWNTO = 14
    DO = 15
    BREAK = 16
    CONTINUE = 17
    CLASS = 18
    EXTENDS = 19
    THIS = 20
    FINAL = 21
    STATIC = 22
    NIL = 23
    NEW = 24
    RETURN = 25
    ADD = 26
    SUB = 27
    MUL = 28
    FLOAT_DIV = 29
    INT_DIV = 30
    MOD = 31
    NE = 32
    EQUAL = 33
    LT = 34
    GT = 35
    LTE = 36
    GTE = 37
    OR = 38
    AND = 39
    NOT = 40
    CONCATENATION = 41
    ASSIGN = 42
    INIT = 43
    LSB = 44
    RSB = 45
    LCB = 46
    RCB = 47
    LP = 48
    RP = 49
    SEMI = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    INTLIT = 54
    FLOATLIT = 55
    BOOLLIT = 56
    STRINGLIT = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ID = 60
    WS = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'int'", "'float'", "'string'", "'void'", "'if'", 
            "'then'", "'else'", "'for'", "'to'", "'downto'", "'do'", "'break'", 
            "'continue'", "'class'", "'extends'", "'this'", "'final'", "'static'", 
            "'nil'", "'new'", "'return'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
            "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", 
            "'&&'", "'!'", "'^'", "':='", "'='", "'['", "']'", "'{'", "'}'", 
            "'('", "')'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BLOCK_CMT", "LINE_CMT", "BOOLEAN", "INT", "FLOAT", 
            "STRING", "VOID", "IF", "THEN", "ELSE", "FOR", "TO", "DOWNTO", 
            "DO", "BREAK", "CONTINUE", "CLASS", "EXTENDS", "THIS", "FINAL", 
            "STATIC", "NIL", "NEW", "RETURN", "ADD", "SUB", "MUL", "FLOAT_DIV", 
            "INT_DIV", "MOD", "NE", "EQUAL", "LT", "GT", "LTE", "GTE", "OR", 
            "AND", "NOT", "CONCATENATION", "ASSIGN", "INIT", "LSB", "RSB", 
            "LCB", "RCB", "LP", "RP", "SEMI", "COLON", "DOT", "COMMA", "INTLIT", 
            "FLOATLIT", "BOOLLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "BLOCK_CMT", "LINE_CMT", "BOOLEAN", "INT", 
                  "FLOAT", "STRING", "VOID", "IF", "THEN", "ELSE", "FOR", 
                  "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", "CLASS", "EXTENDS", 
                  "THIS", "FINAL", "STATIC", "TRUE", "FALSE", "NIL", "NEW", 
                  "RETURN", "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", 
                  "MOD", "NE", "EQUAL", "LT", "GT", "LTE", "GTE", "OR", 
                  "AND", "NOT", "CONCATENATION", "ASSIGN", "INIT", "LSB", 
                  "RSB", "LCB", "RCB", "LP", "RP", "SEMI", "COLON", "DOT", 
                  "COMMA", "INTLIT", "FLOATLIT", "DIGIT", "DigitSequence", 
                  "Exponent", "SIGN", "DecimalPart", "ExponentPart", "BOOLLIT", 
                  "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "CHAR", 
                  "ESCAPE_SEQUENCE", "ESC_ILLEGAL", "ID", "WS", "ERROR_CHAR" ]

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
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                raise UncloseString(self.text[:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(self.text[:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


