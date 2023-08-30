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
        buf.write("\u020e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\6\2~\n\2\r\2\16\2\177\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u0088\n\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\5\5\u0094\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u009c\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u00b8\n\n\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00bf\n\13\3\f\3\f\3\f\5\f\u00c4\n\f\3\r\5\r\u00c7\n")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00d2\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\5\17\u00d9\n\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\5\21\u00e2\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\5\23\u00ec\n\23\3\24\3\24")
        buf.write("\3\24\5\24\u00f1\n\24\3\25\3\25\3\26\3\26\5\26\u00f7\n")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0105\n\27\3\30\3\30\5\30\u0109\n\30\3")
        buf.write("\30\5\30\u010c\n\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0114\n\31\3\32\3\32\5\32\u0118\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0128\n\35\3\36\3\36\3\36\5\36\u012d\n\36\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0133\n\37\3 \3 \3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\5!\u013f\n!\3\"\3\"\3\"\5\"\u0144\n\"\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\5#\u014e\n#\3$\3$\3$\3$\3$\3%\3%\5%\u0157")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\5.\u0185\n.\3/\3/\3")
        buf.write("/\3/\3/\5/\u018c\n/\3\60\3\60\3\60\3\60\3\60\3\60\7\60")
        buf.write("\u0194\n\60\f\60\16\60\u0197\13\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\7\61\u019f\n\61\f\61\16\61\u01a2\13\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\7\62\u01aa\n\62\f\62\16\62\u01ad")
        buf.write("\13\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u01b5\n\63\f")
        buf.write("\63\16\63\u01b8\13\63\3\64\3\64\3\64\5\64\u01bd\n\64\3")
        buf.write("\65\3\65\3\65\5\65\u01c2\n\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\5\66\u01ca\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\7\67\u01d5\n\67\f\67\16\67\u01d8\13\67\3")
        buf.write("8\38\38\38\58\u01de\n8\38\38\58\u01e2\n8\39\39\39\39\3")
        buf.write("9\39\39\39\59\u01ec\n9\3:\3:\3:\5:\u01f1\n:\3:\3:\3;\3")
        buf.write(";\3;\3;\3;\5;\u01fa\n;\3<\3<\3<\3<\3<\5<\u0201\n<\3=\3")
        buf.write("=\3=\3=\3>\3>\3>\3>\3>\5>\u020c\n>\3>\2\7^`bdl?\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\t\3\2\6\t\3\2\17")
        buf.write("\20\3\2$\'\3\2\"#\3\2()\3\2\34\35\3\2\36!\2\u020e\2}\3")
        buf.write("\2\2\2\4\u0083\3\2\2\2\6\u008b\3\2\2\2\b\u0093\3\2\2\2")
        buf.write("\n\u009b\3\2\2\2\f\u009d\3\2\2\2\16\u00a1\3\2\2\2\20\u00a6")
        buf.write("\3\2\2\2\22\u00b7\3\2\2\2\24\u00be\3\2\2\2\26\u00c0\3")
        buf.write("\2\2\2\30\u00c6\3\2\2\2\32\u00d1\3\2\2\2\34\u00d8\3\2")
        buf.write("\2\2\36\u00da\3\2\2\2 \u00e1\3\2\2\2\"\u00e3\3\2\2\2$")
        buf.write("\u00eb\3\2\2\2&\u00f0\3\2\2\2(\u00f2\3\2\2\2*\u00f6\3")
        buf.write("\2\2\2,\u0104\3\2\2\2.\u0106\3\2\2\2\60\u0113\3\2\2\2")
        buf.write("\62\u0117\3\2\2\2\64\u0119\3\2\2\2\66\u011d\3\2\2\28\u0127")
        buf.write("\3\2\2\2:\u0129\3\2\2\2<\u0132\3\2\2\2>\u0134\3\2\2\2")
        buf.write("@\u013e\3\2\2\2B\u0143\3\2\2\2D\u014d\3\2\2\2F\u014f\3")
        buf.write("\2\2\2H\u0156\3\2\2\2J\u0158\3\2\2\2L\u015f\3\2\2\2N\u0164")
        buf.write("\3\2\2\2P\u016e\3\2\2\2R\u0171\3\2\2\2T\u0174\3\2\2\2")
        buf.write("V\u0178\3\2\2\2X\u017d\3\2\2\2Z\u0184\3\2\2\2\\\u018b")
        buf.write("\3\2\2\2^\u018d\3\2\2\2`\u0198\3\2\2\2b\u01a3\3\2\2\2")
        buf.write("d\u01ae\3\2\2\2f\u01bc\3\2\2\2h\u01c1\3\2\2\2j\u01c9\3")
        buf.write("\2\2\2l\u01cb\3\2\2\2n\u01e1\3\2\2\2p\u01eb\3\2\2\2r\u01ed")
        buf.write("\3\2\2\2t\u01f9\3\2\2\2v\u0200\3\2\2\2x\u0202\3\2\2\2")
        buf.write("z\u020b\3\2\2\2|~\5\4\3\2}|\3\2\2\2~\177\3\2\2\2\177}")
        buf.write("\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082")
        buf.write("\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\7\24\2\2\u0084\u0087")
        buf.write("\7>\2\2\u0085\u0086\7\25\2\2\u0086\u0088\7>\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u008a\5\6\4\2\u008a\5\3\2\2\2\u008b\u008c\7\60")
        buf.write("\2\2\u008c\u008d\5\b\5\2\u008d\u008e\7\61\2\2\u008e\7")
        buf.write("\3\2\2\2\u008f\u0090\5\n\6\2\u0090\u0091\5\b\5\2\u0091")
        buf.write("\u0094\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u008f\3\2\2\2")
        buf.write("\u0093\u0092\3\2\2\2\u0094\t\3\2\2\2\u0095\u009c\5\30")
        buf.write("\r\2\u0096\u009c\5\16\b\2\u0097\u009c\5\20\t\2\u0098\u009c")
        buf.write("\5\22\n\2\u0099\u009c\5\f\7\2\u009a\u009c\5\"\22\2\u009b")
        buf.write("\u0095\3\2\2\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2")
        buf.write("\u009b\u0098\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3")
        buf.write("\2\2\2\u009c\13\3\2\2\2\u009d\u009e\5&\24\2\u009e\u009f")
        buf.write("\5\24\13\2\u009f\u00a0\7\64\2\2\u00a0\r\3\2\2\2\u00a1")
        buf.write("\u00a2\7\27\2\2\u00a2\u00a3\5&\24\2\u00a3\u00a4\5\24\13")
        buf.write("\2\u00a4\u00a5\7\64\2\2\u00a5\17\3\2\2\2\u00a6\u00a7\7")
        buf.write("\30\2\2\u00a7\u00a8\5&\24\2\u00a8\u00a9\5\24\13\2\u00a9")
        buf.write("\u00aa\7\64\2\2\u00aa\21\3\2\2\2\u00ab\u00ac\7\27\2\2")
        buf.write("\u00ac\u00ad\7\30\2\2\u00ad\u00ae\5&\24\2\u00ae\u00af")
        buf.write("\5\24\13\2\u00af\u00b0\7\64\2\2\u00b0\u00b8\3\2\2\2\u00b1")
        buf.write("\u00b2\7\30\2\2\u00b2\u00b3\7\27\2\2\u00b3\u00b4\5&\24")
        buf.write("\2\u00b4\u00b5\5\24\13\2\u00b5\u00b6\7\64\2\2\u00b6\u00b8")
        buf.write("\3\2\2\2\u00b7\u00ab\3\2\2\2\u00b7\u00b1\3\2\2\2\u00b8")
        buf.write("\23\3\2\2\2\u00b9\u00ba\5\26\f\2\u00ba\u00bb\7\67\2\2")
        buf.write("\u00bb\u00bc\5\24\13\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf")
        buf.write("\5\26\f\2\u00be\u00b9\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\25\3\2\2\2\u00c0\u00c3\7>\2\2\u00c1\u00c2\7-\2\2\u00c2")
        buf.write("\u00c4\5X-\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\27\3\2\2\2\u00c5\u00c7\7\30\2\2\u00c6\u00c5\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\5$\23\2")
        buf.write("\u00c9\u00ca\7>\2\2\u00ca\u00cb\7\62\2\2\u00cb\u00cc\5")
        buf.write("\32\16\2\u00cc\u00cd\7\63\2\2\u00cd\u00ce\5.\30\2\u00ce")
        buf.write("\31\3\2\2\2\u00cf\u00d2\5\34\17\2\u00d0\u00d2\3\2\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\33\3\2")
        buf.write("\2\2\u00d3\u00d4\5\36\20\2\u00d4\u00d5\7\64\2\2\u00d5")
        buf.write("\u00d6\5\34\17\2\u00d6\u00d9\3\2\2\2\u00d7\u00d9\5\36")
        buf.write("\20\2\u00d8\u00d3\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\35")
        buf.write("\3\2\2\2\u00da\u00db\5&\24\2\u00db\u00dc\5 \21\2\u00dc")
        buf.write("\37\3\2\2\2\u00dd\u00de\7>\2\2\u00de\u00df\7\67\2\2\u00df")
        buf.write("\u00e2\5 \21\2\u00e0\u00e2\7>\2\2\u00e1\u00dd\3\2\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2!\3\2\2\2\u00e3\u00e4\7>\2\2")
        buf.write("\u00e4\u00e5\7\62\2\2\u00e5\u00e6\5\32\16\2\u00e6\u00e7")
        buf.write("\7\63\2\2\u00e7\u00e8\5.\30\2\u00e8#\3\2\2\2\u00e9\u00ec")
        buf.write("\5&\24\2\u00ea\u00ec\7\n\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec%\3\2\2\2\u00ed\u00f1\5(\25\2\u00ee")
        buf.write("\u00f1\5*\26\2\u00ef\u00f1\7>\2\2\u00f0\u00ed\3\2\2\2")
        buf.write("\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\'\3\2\2")
        buf.write("\2\u00f2\u00f3\t\2\2\2\u00f3)\3\2\2\2\u00f4\u00f7\5(\25")
        buf.write("\2\u00f5\u00f7\7>\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7.\2\2\u00f9")
        buf.write("\u00fa\78\2\2\u00fa\u00fb\7/\2\2\u00fb+\3\2\2\2\u00fc")
        buf.write("\u0105\5.\30\2\u00fd\u0105\5> \2\u00fe\u0105\5H%\2\u00ff")
        buf.write("\u0105\5N(\2\u0100\u0105\5P)\2\u0101\u0105\5R*\2\u0102")
        buf.write("\u0105\5T+\2\u0103\u0105\5V,\2\u0104\u00fc\3\2\2\2\u0104")
        buf.write("\u00fd\3\2\2\2\u0104\u00fe\3\2\2\2\u0104\u00ff\3\2\2\2")
        buf.write("\u0104\u0100\3\2\2\2\u0104\u0101\3\2\2\2\u0104\u0102\3")
        buf.write("\2\2\2\u0104\u0103\3\2\2\2\u0105-\3\2\2\2\u0106\u0108")
        buf.write("\7\60\2\2\u0107\u0109\5\60\31\2\u0108\u0107\3\2\2\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u010c\5<\37\2")
        buf.write("\u010b\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d\u010e\7\61\2\2\u010e/\3\2\2\2\u010f\u0110")
        buf.write("\5\62\32\2\u0110\u0111\5\60\31\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0114\5\62\32\2\u0113\u010f\3\2\2\2\u0113\u0112\3\2\2")
        buf.write("\2\u0114\61\3\2\2\2\u0115\u0118\5\64\33\2\u0116\u0118")
        buf.write("\5\66\34\2\u0117\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\63\3\2\2\2\u0119\u011a\5&\24\2\u011a\u011b\58\35\2\u011b")
        buf.write("\u011c\7\64\2\2\u011c\65\3\2\2\2\u011d\u011e\7\27\2\2")
        buf.write("\u011e\u011f\5&\24\2\u011f\u0120\58\35\2\u0120\u0121\7")
        buf.write("\64\2\2\u0121\67\3\2\2\2\u0122\u0123\5:\36\2\u0123\u0124")
        buf.write("\7\67\2\2\u0124\u0125\58\35\2\u0125\u0128\3\2\2\2\u0126")
        buf.write("\u0128\5:\36\2\u0127\u0122\3\2\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u01289\3\2\2\2\u0129\u012c\7>\2\2\u012a\u012b\7-\2\2")
        buf.write("\u012b\u012d\5X-\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2")
        buf.write("\2\2\u012d;\3\2\2\2\u012e\u012f\5,\27\2\u012f\u0130\5")
        buf.write("<\37\2\u0130\u0133\3\2\2\2\u0131\u0133\5,\27\2\u0132\u012e")
        buf.write("\3\2\2\2\u0132\u0131\3\2\2\2\u0133=\3\2\2\2\u0134\u0135")
        buf.write("\5@!\2\u0135\u0136\7,\2\2\u0136\u0137\5X-\2\u0137\u0138")
        buf.write("\7\64\2\2\u0138?\3\2\2\2\u0139\u013a\7\62\2\2\u013a\u013b")
        buf.write("\5@!\2\u013b\u013c\7\63\2\2\u013c\u013f\3\2\2\2\u013d")
        buf.write("\u013f\5B\"\2\u013e\u0139\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013fA\3\2\2\2\u0140\u0144\7>\2\2\u0141\u0144\5F$\2\u0142")
        buf.write("\u0144\5D#\2\u0143\u0140\3\2\2\2\u0143\u0141\3\2\2\2\u0143")
        buf.write("\u0142\3\2\2\2\u0144C\3\2\2\2\u0145\u0146\5n8\2\u0146")
        buf.write("\u0147\7\66\2\2\u0147\u0148\5r:\2\u0148\u014e\3\2\2\2")
        buf.write("\u0149\u014a\5n8\2\u014a\u014b\7\66\2\2\u014b\u014c\7")
        buf.write(">\2\2\u014c\u014e\3\2\2\2\u014d\u0145\3\2\2\2\u014d\u0149")
        buf.write("\3\2\2\2\u014eE\3\2\2\2\u014f\u0150\5l\67\2\u0150\u0151")
        buf.write("\7.\2\2\u0151\u0152\5X-\2\u0152\u0153\7/\2\2\u0153G\3")
        buf.write("\2\2\2\u0154\u0157\5L\'\2\u0155\u0157\5J&\2\u0156\u0154")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157I\3\2\2\2\u0158\u0159")
        buf.write("\7\13\2\2\u0159\u015a\5X-\2\u015a\u015b\7\f\2\2\u015b")
        buf.write("\u015c\5,\27\2\u015c\u015d\7\r\2\2\u015d\u015e\5,\27\2")
        buf.write("\u015eK\3\2\2\2\u015f\u0160\7\13\2\2\u0160\u0161\5X-\2")
        buf.write("\u0161\u0162\7\f\2\2\u0162\u0163\5,\27\2\u0163M\3\2\2")
        buf.write("\2\u0164\u0165\7\16\2\2\u0165\u0166\7>\2\2\u0166\u0167")
        buf.write("\7,\2\2\u0167\u0168\5X-\2\u0168\u0169\3\2\2\2\u0169\u016a")
        buf.write("\t\3\2\2\u016a\u016b\5X-\2\u016b\u016c\7\21\2\2\u016c")
        buf.write("\u016d\5,\27\2\u016dO\3\2\2\2\u016e\u016f\7\22\2\2\u016f")
        buf.write("\u0170\7\64\2\2\u0170Q\3\2\2\2\u0171\u0172\7\23\2\2\u0172")
        buf.write("\u0173\7\64\2\2\u0173S\3\2\2\2\u0174\u0175\7\33\2\2\u0175")
        buf.write("\u0176\5X-\2\u0176\u0177\7\64\2\2\u0177U\3\2\2\2\u0178")
        buf.write("\u0179\5X-\2\u0179\u017a\7\66\2\2\u017a\u017b\5r:\2\u017b")
        buf.write("\u017c\7\64\2\2\u017cW\3\2\2\2\u017d\u017e\5Z.\2\u017e")
        buf.write("Y\3\2\2\2\u017f\u0180\5\\/\2\u0180\u0181\t\4\2\2\u0181")
        buf.write("\u0182\5\\/\2\u0182\u0185\3\2\2\2\u0183\u0185\5\\/\2\u0184")
        buf.write("\u017f\3\2\2\2\u0184\u0183\3\2\2\2\u0185[\3\2\2\2\u0186")
        buf.write("\u0187\5^\60\2\u0187\u0188\t\5\2\2\u0188\u0189\5^\60\2")
        buf.write("\u0189\u018c\3\2\2\2\u018a\u018c\5^\60\2\u018b\u0186\3")
        buf.write("\2\2\2\u018b\u018a\3\2\2\2\u018c]\3\2\2\2\u018d\u018e")
        buf.write("\b\60\1\2\u018e\u018f\5`\61\2\u018f\u0195\3\2\2\2\u0190")
        buf.write("\u0191\f\4\2\2\u0191\u0192\t\6\2\2\u0192\u0194\5`\61\2")
        buf.write("\u0193\u0190\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3")
        buf.write("\2\2\2\u0195\u0196\3\2\2\2\u0196_\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0198\u0199\b\61\1\2\u0199\u019a\5b\62\2\u019a")
        buf.write("\u01a0\3\2\2\2\u019b\u019c\f\4\2\2\u019c\u019d\t\7\2\2")
        buf.write("\u019d\u019f\5b\62\2\u019e\u019b\3\2\2\2\u019f\u01a2\3")
        buf.write("\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1a")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a4\b\62\1\2\u01a4")
        buf.write("\u01a5\5d\63\2\u01a5\u01ab\3\2\2\2\u01a6\u01a7\f\4\2\2")
        buf.write("\u01a7\u01a8\t\b\2\2\u01a8\u01aa\5d\63\2\u01a9\u01a6\3")
        buf.write("\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01acc\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af")
        buf.write("\b\63\1\2\u01af\u01b0\5f\64\2\u01b0\u01b6\3\2\2\2\u01b1")
        buf.write("\u01b2\f\4\2\2\u01b2\u01b3\7+\2\2\u01b3\u01b5\5f\64\2")
        buf.write("\u01b4\u01b1\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3")
        buf.write("\2\2\2\u01b6\u01b7\3\2\2\2\u01b7e\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b9\u01ba\7*\2\2\u01ba\u01bd\5f\64\2\u01bb")
        buf.write("\u01bd\5h\65\2\u01bc\u01b9\3\2\2\2\u01bc\u01bb\3\2\2\2")
        buf.write("\u01bdg\3\2\2\2\u01be\u01bf\t\7\2\2\u01bf\u01c2\5h\65")
        buf.write("\2\u01c0\u01c2\5j\66\2\u01c1\u01be\3\2\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2i\3\2\2\2\u01c3\u01c4\5l\67\2\u01c4\u01c5")
        buf.write("\7.\2\2\u01c5\u01c6\5X-\2\u01c6\u01c7\7/\2\2\u01c7\u01ca")
        buf.write("\3\2\2\2\u01c8\u01ca\5l\67\2\u01c9\u01c3\3\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01cak\3\2\2\2\u01cb\u01cc\b\67\1\2\u01cc")
        buf.write("\u01cd\5n8\2\u01cd\u01d6\3\2\2\2\u01ce\u01cf\f\5\2\2\u01cf")
        buf.write("\u01d0\7\66\2\2\u01d0\u01d5\5r:\2\u01d1\u01d2\f\4\2\2")
        buf.write("\u01d2\u01d3\7\66\2\2\u01d3\u01d5\7>\2\2\u01d4\u01ce\3")
        buf.write("\2\2\2\u01d4\u01d1\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7m\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d9\u01da\7\32\2\2\u01da\u01db\7>\2\2\u01db")
        buf.write("\u01dd\7\62\2\2\u01dc\u01de\5t;\2\u01dd\u01dc\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e2\7")
        buf.write("\63\2\2\u01e0\u01e2\5p9\2\u01e1\u01d9\3\2\2\2\u01e1\u01e0")
        buf.write("\3\2\2\2\u01e2o\3\2\2\2\u01e3\u01ec\5v<\2\u01e4\u01ec")
        buf.write("\7>\2\2\u01e5\u01ec\7\26\2\2\u01e6\u01e7\7\62\2\2\u01e7")
        buf.write("\u01e8\5X-\2\u01e8\u01e9\7\63\2\2\u01e9\u01ec\3\2\2\2")
        buf.write("\u01ea\u01ec\7\31\2\2\u01eb\u01e3\3\2\2\2\u01eb\u01e4")
        buf.write("\3\2\2\2\u01eb\u01e5\3\2\2\2\u01eb\u01e6\3\2\2\2\u01eb")
        buf.write("\u01ea\3\2\2\2\u01ecq\3\2\2\2\u01ed\u01ee\7>\2\2\u01ee")
        buf.write("\u01f0\7\62\2\2\u01ef\u01f1\5t;\2\u01f0\u01ef\3\2\2\2")
        buf.write("\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\7")
        buf.write("\63\2\2\u01f3s\3\2\2\2\u01f4\u01f5\5X-\2\u01f5\u01f6\7")
        buf.write("\67\2\2\u01f6\u01f7\5t;\2\u01f7\u01fa\3\2\2\2\u01f8\u01fa")
        buf.write("\5X-\2\u01f9\u01f4\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fau")
        buf.write("\3\2\2\2\u01fb\u0201\78\2\2\u01fc\u0201\79\2\2\u01fd\u0201")
        buf.write("\7;\2\2\u01fe\u0201\7:\2\2\u01ff\u0201\5x=\2\u0200\u01fb")
        buf.write("\3\2\2\2\u0200\u01fc\3\2\2\2\u0200\u01fd\3\2\2\2\u0200")
        buf.write("\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2\u0201w\3\2\2\2\u0202")
        buf.write("\u0203\7\60\2\2\u0203\u0204\5z>\2\u0204\u0205\7\61\2\2")
        buf.write("\u0205y\3\2\2\2\u0206\u0207\5v<\2\u0207\u0208\7\67\2\2")
        buf.write("\u0208\u0209\5z>\2\u0209\u020c\3\2\2\2\u020a\u020c\5v")
        buf.write("<\2\u020b\u0206\3\2\2\2\u020b\u020a\3\2\2\2\u020c{\3\2")
        buf.write("\2\2.\177\u0087\u0093\u009b\u00b7\u00be\u00c3\u00c6\u00d1")
        buf.write("\u00d8\u00e1\u00eb\u00f0\u00f6\u0104\u0108\u010b\u0113")
        buf.write("\u0117\u0127\u012c\u0132\u013e\u0143\u014d\u0156\u0184")
        buf.write("\u018b\u0195\u01a0\u01ab\u01b6\u01bc\u01c1\u01c9\u01d4")
        buf.write("\u01d6\u01dd\u01e1\u01eb\u01f0\u01f9\u0200\u020b")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'boolean'", "'int'", "'float'", "'string'", "'void'", 
                     "'if'", "'then'", "'else'", "'for'", "'to'", "'downto'", 
                     "'do'", "'break'", "'continue'", "'class'", "'extends'", 
                     "'this'", "'final'", "'static'", "'nil'", "'new'", 
                     "'return'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", 
                     "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", 
                     "'&&'", "'!'", "'^'", "':='", "'='", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "BLOCK_CMT", "LINE_CMT", "BOOLEAN", 
                      "INT", "FLOAT", "STRING", "VOID", "IF", "THEN", "ELSE", 
                      "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", 
                      "CLASS", "EXTENDS", "THIS", "FINAL", "STATIC", "NIL", 
                      "NEW", "RETURN", "ADD", "SUB", "MUL", "FLOAT_DIV", 
                      "INT_DIV", "MOD", "NE", "EQUAL", "LT", "GT", "LTE", 
                      "GTE", "OR", "AND", "NOT", "CONCATENATION", "ASSIGN", 
                      "INIT", "LSB", "RSB", "LCB", "RCB", "LP", "RP", "SEMI", 
                      "COLON", "DOT", "COMMA", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ID", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_mem = 2
    RULE_class_mem_list = 3
    RULE_class_mem_decl = 4
    RULE_attr_decl = 5
    RULE_const_attr_decl = 6
    RULE_static_attr_decl = 7
    RULE_static_const_attr_decl = 8
    RULE_attr_decl_list = 9
    RULE_attr_decl_unit = 10
    RULE_method_decl = 11
    RULE_param_list = 12
    RULE_param_decl = 13
    RULE_param = 14
    RULE_idlist = 15
    RULE_constructor_decl = 16
    RULE_class_type = 17
    RULE_decl_type = 18
    RULE_primitive_type = 19
    RULE_array_type = 20
    RULE_stmt = 21
    RULE_block_stmt = 22
    RULE_local_var_decls = 23
    RULE_local_var_decl = 24
    RULE_var_decl = 25
    RULE_const_decl = 26
    RULE_decl_list = 27
    RULE_decl_unit = 28
    RULE_stmts = 29
    RULE_assign_stmt = 30
    RULE_lhs = 31
    RULE_lhs_unit = 32
    RULE_lhs_member_access_expr = 33
    RULE_lhs_index_expr = 34
    RULE_if_stmt = 35
    RULE_if_then_else_stmt = 36
    RULE_if_then_stmt = 37
    RULE_for_stmt = 38
    RULE_break_stmt = 39
    RULE_continue_stmt = 40
    RULE_return_stmt = 41
    RULE_method_invocation_stmt = 42
    RULE_expr = 43
    RULE_expr1 = 44
    RULE_expr2 = 45
    RULE_expr3 = 46
    RULE_expr4 = 47
    RULE_expr5 = 48
    RULE_expr6 = 49
    RULE_expr7 = 50
    RULE_expr8 = 51
    RULE_expr9 = 52
    RULE_expr10 = 53
    RULE_expr11 = 54
    RULE_expr12 = 55
    RULE_method_call = 56
    RULE_expr_list = 57
    RULE_literal = 58
    RULE_arrlit = 59
    RULE_literal_list = 60

    ruleNames =  [ "program", "class_decl", "class_mem", "class_mem_list", 
                   "class_mem_decl", "attr_decl", "const_attr_decl", "static_attr_decl", 
                   "static_const_attr_decl", "attr_decl_list", "attr_decl_unit", 
                   "method_decl", "param_list", "param_decl", "param", "idlist", 
                   "constructor_decl", "class_type", "decl_type", "primitive_type", 
                   "array_type", "stmt", "block_stmt", "local_var_decls", 
                   "local_var_decl", "var_decl", "const_decl", "decl_list", 
                   "decl_unit", "stmts", "assign_stmt", "lhs", "lhs_unit", 
                   "lhs_member_access_expr", "lhs_index_expr", "if_stmt", 
                   "if_then_else_stmt", "if_then_stmt", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "method_invocation_stmt", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "expr12", "method_call", "expr_list", "literal", "arrlit", 
                   "literal_list" ]

    EOF = Token.EOF
    COMMENT=1
    BLOCK_CMT=2
    LINE_CMT=3
    BOOLEAN=4
    INT=5
    FLOAT=6
    STRING=7
    VOID=8
    IF=9
    THEN=10
    ELSE=11
    FOR=12
    TO=13
    DOWNTO=14
    DO=15
    BREAK=16
    CONTINUE=17
    CLASS=18
    EXTENDS=19
    THIS=20
    FINAL=21
    STATIC=22
    NIL=23
    NEW=24
    RETURN=25
    ADD=26
    SUB=27
    MUL=28
    FLOAT_DIV=29
    INT_DIV=30
    MOD=31
    NE=32
    EQUAL=33
    LT=34
    GT=35
    LTE=36
    GTE=37
    OR=38
    AND=39
    NOT=40
    CONCATENATION=41
    ASSIGN=42
    INIT=43
    LSB=44
    RSB=45
    LCB=46
    RCB=47
    LP=48
    RP=49
    SEMI=50
    COLON=51
    DOT=52
    COMMA=53
    INTLIT=54
    FLOATLIT=55
    BOOLLIT=56
    STRINGLIT=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59
    ID=60
    WS=61
    ERROR_CHAR=62

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
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.class_decl()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 127
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

        def class_mem(self):
            return self.getTypedRuleContext(BKOOLParser.Class_memContext,0)


        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

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
            self.state = 129
            self.match(BKOOLParser.CLASS)
            self.state = 130
            self.match(BKOOLParser.ID)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 131
                self.match(BKOOLParser.EXTENDS)
                self.state = 132
                self.match(BKOOLParser.ID)


            self.state = 135
            self.class_mem()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def class_mem_list(self):
            return self.getTypedRuleContext(BKOOLParser.Class_mem_listContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_mem" ):
                return visitor.visitClass_mem(self)
            else:
                return visitor.visitChildren(self)




    def class_mem(self):

        localctx = BKOOLParser.Class_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BKOOLParser.LCB)
            self.state = 138
            self.class_mem_list()
            self.state = 139
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_mem_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_mem_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Class_mem_declContext,0)


        def class_mem_list(self):
            return self.getTypedRuleContext(BKOOLParser.Class_mem_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_mem_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_mem_list" ):
                return visitor.visitClass_mem_list(self)
            else:
                return visitor.visitChildren(self)




    def class_mem_list(self):

        localctx = BKOOLParser.Class_mem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_mem_list)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.class_mem_decl()
                self.state = 142
                self.class_mem_list()
                pass
            elif token in [BKOOLParser.RCB]:
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


    class Class_mem_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def const_attr_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Const_attr_declContext,0)


        def static_attr_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Static_attr_declContext,0)


        def static_const_attr_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Static_const_attr_declContext,0)


        def attr_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_declContext,0)


        def constructor_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Constructor_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_mem_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_mem_decl" ):
                return visitor.visitClass_mem_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_mem_decl(self):

        localctx = BKOOLParser.Class_mem_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_mem_decl)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.method_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.const_attr_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.static_attr_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.static_const_attr_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 151
                self.attr_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 152
                self.constructor_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def attr_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = BKOOLParser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.decl_type()
            self.state = 156
            self.attr_decl_list()
            self.state = 157
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def attr_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_const_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_attr_decl" ):
                return visitor.visitConst_attr_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_attr_decl(self):

        localctx = BKOOLParser.Const_attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_attr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BKOOLParser.FINAL)
            self.state = 160
            self.decl_type()
            self.state = 161
            self.attr_decl_list()
            self.state = 162
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def attr_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_static_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attr_decl" ):
                return visitor.visitStatic_attr_decl(self)
            else:
                return visitor.visitChildren(self)




    def static_attr_decl(self):

        localctx = BKOOLParser.Static_attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_static_attr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKOOLParser.STATIC)
            self.state = 165
            self.decl_type()
            self.state = 166
            self.attr_decl_list()
            self.state = 167
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_const_attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def attr_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_static_const_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_const_attr_decl" ):
                return visitor.visitStatic_const_attr_decl(self)
            else:
                return visitor.visitChildren(self)




    def static_const_attr_decl(self):

        localctx = BKOOLParser.Static_const_attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_static_const_attr_decl)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(BKOOLParser.FINAL)
                self.state = 170
                self.match(BKOOLParser.STATIC)
                self.state = 171
                self.decl_type()
                self.state = 172
                self.attr_decl_list()
                self.state = 173
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(BKOOLParser.STATIC)
                self.state = 176
                self.match(BKOOLParser.FINAL)
                self.state = 177
                self.decl_type()
                self.state = 178
                self.attr_decl_list()
                self.state = 179
                self.match(BKOOLParser.SEMI)
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


    class Attr_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl_unit(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_decl_unitContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attr_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_decl_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attr_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_list" ):
                return visitor.visitAttr_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_list(self):

        localctx = BKOOLParser.Attr_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr_decl_list)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.attr_decl_unit()
                self.state = 184
                self.match(BKOOLParser.COMMA)
                self.state = 185
                self.attr_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.attr_decl_unit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_decl_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT(self):
            return self.getToken(BKOOLParser.INIT, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attr_decl_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl_unit" ):
                return visitor.visitAttr_decl_unit(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl_unit(self):

        localctx = BKOOLParser.Attr_decl_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr_decl_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(BKOOLParser.ID)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INIT:
                self.state = 191
                self.match(BKOOLParser.INIT)
                self.state = 192
                self.expr()


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

        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


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
        self.enterRule(localctx, 22, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 195
                self.match(BKOOLParser.STATIC)


            self.state = 198
            self.class_type()
            self.state = 199
            self.match(BKOOLParser.ID)
            self.state = 200
            self.match(BKOOLParser.LP)
            self.state = 201
            self.param_list()
            self.state = 202
            self.match(BKOOLParser.RP)
            self.state = 203
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Param_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.param_decl()
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


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def param_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Param_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = BKOOLParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param_decl)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.param()
                self.state = 210
                self.match(BKOOLParser.SEMI)
                self.state = 211
                self.param_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.decl_type()
            self.state = 217
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idlist)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(BKOOLParser.ID)
                self.state = 220
                self.match(BKOOLParser.COMMA)
                self.state = 221
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = BKOOLParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(BKOOLParser.ID)
            self.state = 226
            self.match(BKOOLParser.LP)
            self.state = 227
            self.param_list()
            self.state = 228
            self.match(BKOOLParser.RP)
            self.state = 229
            self.block_stmt()
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

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_class_type)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.decl_type()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(BKOOLParser.VOID)
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


    class Decl_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_decl_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_type" ):
                return visitor.visitDecl_type(self)
            else:
                return visitor.visitChildren(self)




    def decl_type(self):

        localctx = BKOOLParser.Decl_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_decl_type)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0)):
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

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING]:
                self.state = 242
                self.primitive_type()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 243
                self.match(BKOOLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 246
            self.match(BKOOLParser.LSB)
            self.state = 247
            self.match(BKOOLParser.INTLIT)
            self.state = 248
            self.match(BKOOLParser.RSB)
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


        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


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


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 257
                self.method_invocation_stmt()
                pass


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

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def local_var_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Local_var_declsContext,0)


        def stmts(self):
            return self.getTypedRuleContext(BKOOLParser.StmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(BKOOLParser.LCB)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 261
                self.local_var_decls()


            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 264
                self.stmts()


            self.state = 267
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_var_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Local_var_declContext,0)


        def local_var_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Local_var_declsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_local_var_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_var_decls" ):
                return visitor.visitLocal_var_decls(self)
            else:
                return visitor.visitChildren(self)




    def local_var_decls(self):

        localctx = BKOOLParser.Local_var_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_local_var_decls)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.local_var_decl()
                self.state = 270
                self.local_var_decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.local_var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Const_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_local_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_var_decl" ):
                return visitor.visitLocal_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def local_var_decl(self):

        localctx = BKOOLParser.Local_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_local_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.state = 275
                self.var_decl()
                pass
            elif token in [BKOOLParser.FINAL]:
                self.state = 276
                self.const_decl()
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


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.decl_type()
            self.state = 280
            self.decl_list()
            self.state = 281
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def decl_type(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_typeContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = BKOOLParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BKOOLParser.FINAL)
            self.state = 284
            self.decl_type()
            self.state = 285
            self.decl_list()
            self.state = 286
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_unit(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_unitContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = BKOOLParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_decl_list)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.decl_unit()
                self.state = 289
                self.match(BKOOLParser.COMMA)
                self.state = 290
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.decl_unit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT(self):
            return self.getToken(BKOOLParser.INIT, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_unit" ):
                return visitor.visitDecl_unit(self)
            else:
                return visitor.visitChildren(self)




    def decl_unit(self):

        localctx = BKOOLParser.Decl_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_decl_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BKOOLParser.ID)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INIT:
                self.state = 296
                self.match(BKOOLParser.INIT)
                self.state = 297
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmts(self):
            return self.getTypedRuleContext(BKOOLParser.StmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = BKOOLParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmts)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.stmt()
                self.state = 301
                self.stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.lhs()
            self.state = 307
            self.match(BKOOLParser.ASSIGN)
            self.state = 308
            self.expr()
            self.state = 309
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def lhs_unit(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_unitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(BKOOLParser.LP)
                self.state = 312
                self.lhs()
                self.state = 313
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.lhs_unit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def lhs_index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_index_exprContext,0)


        def lhs_member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_member_access_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_unit" ):
                return visitor.visitLhs_unit(self)
            else:
                return visitor.visitChildren(self)




    def lhs_unit(self):

        localctx = BKOOLParser.Lhs_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lhs_unit)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.lhs_index_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.lhs_member_access_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_member_access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_member_access_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_member_access_expr" ):
                return visitor.visitLhs_member_access_expr(self)
            else:
                return visitor.visitChildren(self)




    def lhs_member_access_expr(self):

        localctx = BKOOLParser.Lhs_member_access_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_lhs_member_access_expr)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.expr11()
                self.state = 324
                localctx.bop = self.match(BKOOLParser.DOT)

                self.state = 325
                self.method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.expr11()
                self.state = 328
                localctx.bop = self.match(BKOOLParser.DOT)

                self.state = 329
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_index_expr" ):
                return visitor.visitLhs_index_expr(self)
            else:
                return visitor.visitChildren(self)




    def lhs_index_expr(self):

        localctx = BKOOLParser.Lhs_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_lhs_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.expr10(0)

            self.state = 334
            self.match(BKOOLParser.LSB)
            self.state = 335
            self.expr()
            self.state = 336
            self.match(BKOOLParser.RSB)
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

        def if_then_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_stmtContext,0)


        def if_then_else_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_else_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_stmt)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.if_then_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.if_then_else_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_else_stmtContext(ParserRuleContext):
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
            return BKOOLParser.RULE_if_then_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_then_else_stmt" ):
                return visitor.visitIf_then_else_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_then_else_stmt(self):

        localctx = BKOOLParser.If_then_else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_then_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKOOLParser.IF)
            self.state = 343
            self.expr()
            self.state = 344
            self.match(BKOOLParser.THEN)
            self.state = 345
            self.stmt()
            self.state = 346
            self.match(BKOOLParser.ELSE)
            self.state = 347
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_stmtContext(ParserRuleContext):
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

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_then_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_then_stmt" ):
                return visitor.visitIf_then_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_then_stmt(self):

        localctx = BKOOLParser.If_then_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_if_then_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(BKOOLParser.IF)
            self.state = 350
            self.expr()
            self.state = 351
            self.match(BKOOLParser.THEN)
            self.state = 352
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(BKOOLParser.FOR)

            self.state = 355
            self.match(BKOOLParser.ID)
            self.state = 356
            self.match(BKOOLParser.ASSIGN)
            self.state = 357
            self.expr()
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 360
            self.expr()
            self.state = 361
            self.match(BKOOLParser.DO)
            self.state = 362
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
        self.enterRule(localctx, 78, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(BKOOLParser.BREAK)
            self.state = 365
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
        self.enterRule(localctx, 80, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(BKOOLParser.CONTINUE)
            self.state = 368
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
        self.enterRule(localctx, 82, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(BKOOLParser.RETURN)
            self.state = 371
            self.expr()
            self.state = 372
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

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = BKOOLParser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.expr()
            self.state = 375
            self.match(BKOOLParser.DOT)
            self.state = 376
            self.method_call()
            self.state = 377
            self.match(BKOOLParser.SEMI)
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

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.expr1()
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


        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.expr2()
                self.state = 382
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 383
                self.expr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.expr2()
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

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr3Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr3Context,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NE(self):
            return self.getToken(BKOOLParser.NE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = BKOOLParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.expr3(0)
                self.state = 389
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NE or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 390
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.expr3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 398
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 399
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 400
                    self.expr4(0) 
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 411
                    self.expr5(0) 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FLOAT_DIV(self):
            return self.getToken(BKOOLParser.FLOAT_DIV, 0)

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 420
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 421
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 422
                    self.expr6(0) 
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def CONCATENATION(self):
            return self.getToken(BKOOLParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 432
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 433
                    self.expr7() 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

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
        self.enterRule(localctx, 100, self.RULE_expr7)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(BKOOLParser.NOT)
                self.state = 440
                self.expr7()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NIL, BKOOLParser.NEW, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LCB, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
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

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 445
                self.expr8()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NIL, BKOOLParser.NEW, BKOOLParser.LCB, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.expr9()
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


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = BKOOLParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expr9)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.expr10(0)
                self.state = 450
                self.match(BKOOLParser.LSB)
                self.state = 451
                self.expr()
                self.state = 452
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.expr10(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)



    def expr10(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr10Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expr10, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.expr11()
            self._ctx.stop = self._input.LT(-1)
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 466
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr10Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr10)
                        self.state = 460
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 461
                        localctx.bop = self.match(BKOOLParser.DOT)
                        self.state = 462
                        self.method_call()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr10Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr10)
                        self.state = 463
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 464
                        localctx.bop = self.match(BKOOLParser.DOT)
                        self.state = 465
                        self.match(BKOOLParser.ID)
                        pass

             
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def expr12(self):
            return self.getTypedRuleContext(BKOOLParser.Expr12Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_expr11)
        self._la = 0 # Token type
        try:
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(BKOOLParser.NEW)
                self.state = 472
                self.match(BKOOLParser.ID)
                self.state = 473
                self.match(BKOOLParser.LP)
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 474
                    self.expr_list()


                self.state = 477
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NIL, BKOOLParser.LCB, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.expr12()
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


    class Expr12Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr12" ):
                return visitor.visitExpr12(self)
            else:
                return visitor.visitChildren(self)




    def expr12(self):

        localctx = BKOOLParser.Expr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expr12)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LCB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.literal()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.match(BKOOLParser.LP)
                self.state = 485
                self.expr()
                self.state = 486
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 488
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


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = BKOOLParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(BKOOLParser.ID)
            self.state = 492
            self.match(BKOOLParser.LP)
            self.state = 494
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 493
                self.expr_list()


            self.state = 496
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = BKOOLParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_expr_list)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.expr()
                self.state = 499
                self.match(BKOOLParser.COMMA)
                self.state = 500
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.expr()
                pass


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

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def arrlit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrlitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_literal)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 508
                self.match(BKOOLParser.BOOLLIT)
                pass
            elif token in [BKOOLParser.LCB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 509
                self.arrlit()
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


    class ArrlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def literal_list(self):
            return self.getTypedRuleContext(BKOOLParser.Literal_listContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlit" ):
                return visitor.visitArrlit(self)
            else:
                return visitor.visitChildren(self)




    def arrlit(self):

        localctx = BKOOLParser.ArrlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arrlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(BKOOLParser.LCB)
            self.state = 513
            self.literal_list()
            self.state = 514
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def literal_list(self):
            return self.getTypedRuleContext(BKOOLParser.Literal_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_list" ):
                return visitor.visitLiteral_list(self)
            else:
                return visitor.visitChildren(self)




    def literal_list(self):

        localctx = BKOOLParser.Literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_literal_list)
        try:
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.literal()
                self.state = 517
                self.match(BKOOLParser.COMMA)
                self.state = 518
                self.literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.literal()
                pass


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
        self._predicates[46] = self.expr3_sempred
        self._predicates[47] = self.expr4_sempred
        self._predicates[48] = self.expr5_sempred
        self._predicates[49] = self.expr6_sempred
        self._predicates[53] = self.expr10_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr10_sempred(self, localctx:Expr10Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




