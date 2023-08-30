# Generated from /Users/nguyenkim/Downloads/PPL_223/assignment1/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\u0230\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\7\2~\n\2\f\2\16\2\u0081\13\2\3")
        buf.write("\2\3\2\3\3\6\3\u0086\n\3\r\3\16\3\u0087\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\5\4\u0090\n\4\3\4\3\4\3\5\3\5\7\5\u0096\n\5")
        buf.write("\f\5\16\5\u0099\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u00a3\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u00bf\n\n\3\13\3\13\3\13\7\13\u00c4\n\13")
        buf.write("\f\13\16\13\u00c7\13\13\3\f\3\f\3\f\5\f\u00cc\n\f\3\r")
        buf.write("\3\r\3\r\7\r\u00d1\n\r\f\r\16\r\u00d4\13\r\3\16\3\16\3")
        buf.write("\16\5\16\u00d9\n\16\3\17\5\17\u00dc\n\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00e2\n\17\3\17\3\17\3\17\3\20\3\20\3\20\7")
        buf.write("\20\u00ea\n\20\f\20\16\20\u00ed\13\20\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\7\22\u00f5\n\22\f\22\16\22\u00f8\13\22\3")
        buf.write("\23\3\23\3\23\5\23\u00fd\n\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\5\24\u0105\n\24\3\25\3\25\5\25\u0109\n\25\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u011a\n\27\3\30\3\30\5\30\u011e\n")
        buf.write("\30\3\30\5\30\u0121\n\30\3\30\3\30\3\31\6\31\u0126\n\31")
        buf.write("\r\31\16\31\u0127\3\32\6\32\u012b\n\32\r\32\16\32\u012c")
        buf.write("\3\33\3\33\5\33\u0131\n\33\3\34\3\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0146\n\37\3 \3 \3 \5 \u014b\n \3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u015a")
        buf.write("\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\5&\u0172\n&\3\'\3\'\3\'\3\'\3\'\3\'\5")
        buf.write("\'\u017a\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3/\3/\3/\3/\3/\5/\u01a6\n/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u01ad\n\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\7\61\u01b5\n\61\f\61\16\61\u01b8\13\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\7\62\u01c0\n\62\f\62\16\62\u01c3")
        buf.write("\13\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u01cb\n\63\f")
        buf.write("\63\16\63\u01ce\13\63\3\64\3\64\3\64\3\64\3\64\3\64\7")
        buf.write("\64\u01d6\n\64\f\64\16\64\u01d9\13\64\3\65\3\65\3\65\5")
        buf.write("\65\u01de\n\65\3\66\3\66\3\66\5\66\u01e3\n\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u01eb\n\67\38\38\38\38\38\3")
        buf.write("8\38\38\38\78\u01f6\n8\f8\168\u01f9\138\39\39\39\59\u01fe")
        buf.write("\n9\39\39\3:\3:\3:\3:\5:\u0206\n:\3:\3:\5:\u020a\n:\3")
        buf.write(";\3;\3;\3;\3;\3;\3;\3;\5;\u0214\n;\3<\3<\3<\7<\u0219\n")
        buf.write("<\f<\16<\u021c\13<\3=\3=\3=\3=\3=\5=\u0223\n=\3>\3>\3")
        buf.write(">\3>\7>\u0229\n>\f>\16>\u022c\13>\3>\3>\3>\2\7`bdfn?\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\t\3\2\3\7\3\2")
        buf.write("\f\r\3\2!$\3\2\37 \3\2%&\3\2\31\32\3\2\33\36\2\u0238\2")
        buf.write("\177\3\2\2\2\4\u0085\3\2\2\2\6\u008b\3\2\2\2\b\u0093\3")
        buf.write("\2\2\2\n\u00a2\3\2\2\2\f\u00a4\3\2\2\2\16\u00a8\3\2\2")
        buf.write("\2\20\u00ad\3\2\2\2\22\u00be\3\2\2\2\24\u00c0\3\2\2\2")
        buf.write("\26\u00c8\3\2\2\2\30\u00cd\3\2\2\2\32\u00d5\3\2\2\2\34")
        buf.write("\u00db\3\2\2\2\36\u00e6\3\2\2\2 \u00ee\3\2\2\2\"\u00f1")
        buf.write("\3\2\2\2$\u00f9\3\2\2\2&\u0104\3\2\2\2(\u0108\3\2\2\2")
        buf.write("*\u010e\3\2\2\2,\u0119\3\2\2\2.\u011b\3\2\2\2\60\u0125")
        buf.write("\3\2\2\2\62\u012a\3\2\2\2\64\u0130\3\2\2\2\66\u0132\3")
        buf.write("\2\2\28\u0136\3\2\2\2:\u013b\3\2\2\2<\u0145\3\2\2\2>\u014a")
        buf.write("\3\2\2\2@\u014c\3\2\2\2B\u0159\3\2\2\2D\u015b\3\2\2\2")
        buf.write("F\u0160\3\2\2\2H\u0167\3\2\2\2J\u0171\3\2\2\2L\u0179\3")
        buf.write("\2\2\2N\u017b\3\2\2\2P\u0185\3\2\2\2R\u018f\3\2\2\2T\u0192")
        buf.write("\3\2\2\2V\u0195\3\2\2\2X\u0199\3\2\2\2Z\u019e\3\2\2\2")
        buf.write("\\\u01a5\3\2\2\2^\u01ac\3\2\2\2`\u01ae\3\2\2\2b\u01b9")
        buf.write("\3\2\2\2d\u01c4\3\2\2\2f\u01cf\3\2\2\2h\u01dd\3\2\2\2")
        buf.write("j\u01e2\3\2\2\2l\u01ea\3\2\2\2n\u01ec\3\2\2\2p\u01fa\3")
        buf.write("\2\2\2r\u0209\3\2\2\2t\u0213\3\2\2\2v\u0215\3\2\2\2x\u0222")
        buf.write("\3\2\2\2z\u0224\3\2\2\2|~\5\6\4\2}|\3\2\2\2~\u0081\3\2")
        buf.write("\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2")
        buf.write("\2\u0081\177\3\2\2\2\u0082\u0083\7\2\2\3\u0083\3\3\2\2")
        buf.write("\2\u0084\u0086\5Z.\2\u0085\u0084\3\2\2\2\u0086\u0087\3")
        buf.write("\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u008a\7\2\2\3\u008a\5\3\2\2\2\u008b\u008c")
        buf.write("\7\21\2\2\u008c\u008f\7;\2\2\u008d\u008e\7\22\2\2\u008e")
        buf.write("\u0090\7;\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0092\5\b\5\2\u0092\7\3\2\2")
        buf.write("\2\u0093\u0097\7/\2\2\u0094\u0096\5\n\6\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u009a\u009b\7\60\2\2\u009b\t\3\2\2\2\u009c\u00a3\5$\23")
        buf.write("\2\u009d\u00a3\5\f\7\2\u009e\u00a3\5\20\t\2\u009f\u00a3")
        buf.write("\5\16\b\2\u00a0\u00a3\5\22\n\2\u00a1\u00a3\5\34\17\2\u00a2")
        buf.write("\u009c\3\2\2\2\u00a2\u009d\3\2\2\2\u00a2\u009e\3\2\2\2")
        buf.write("\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3")
        buf.write("\2\2\2\u00a3\13\3\2\2\2\u00a4\u00a5\5&\24\2\u00a5\u00a6")
        buf.write("\5\24\13\2\u00a6\u00a7\7\61\2\2\u00a7\r\3\2\2\2\u00a8")
        buf.write("\u00a9\7\23\2\2\u00a9\u00aa\5&\24\2\u00aa\u00ab\5\30\r")
        buf.write("\2\u00ab\u00ac\7\61\2\2\u00ac\17\3\2\2\2\u00ad\u00ae\7")
        buf.write("\24\2\2\u00ae\u00af\5&\24\2\u00af\u00b0\5\24\13\2\u00b0")
        buf.write("\u00b1\7\61\2\2\u00b1\21\3\2\2\2\u00b2\u00b3\7\24\2\2")
        buf.write("\u00b3\u00b4\7\23\2\2\u00b4\u00b5\5&\24\2\u00b5\u00b6")
        buf.write("\5\30\r\2\u00b6\u00b7\7\61\2\2\u00b7\u00bf\3\2\2\2\u00b8")
        buf.write("\u00b9\7\23\2\2\u00b9\u00ba\7\24\2\2\u00ba\u00bb\5&\24")
        buf.write("\2\u00bb\u00bc\5\30\r\2\u00bc\u00bd\7\61\2\2\u00bd\u00bf")
        buf.write("\3\2\2\2\u00be\u00b2\3\2\2\2\u00be\u00b8\3\2\2\2\u00bf")
        buf.write("\23\3\2\2\2\u00c0\u00c5\5\26\f\2\u00c1\u00c2\7\64\2\2")
        buf.write("\u00c2\u00c4\5\26\f\2\u00c3\u00c1\3\2\2\2\u00c4\u00c7")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\25\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00cb\7;\2\2\u00c9")
        buf.write("\u00ca\7*\2\2\u00ca\u00cc\5Z.\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\27\3\2\2\2\u00cd\u00d2\5\32\16\2")
        buf.write("\u00ce\u00cf\7\64\2\2\u00cf\u00d1\5\32\16\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\31\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d8\7;\2\2\u00d6\u00d7\7*\2\2\u00d7\u00d9\5Z.\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\33\3\2\2\2\u00da")
        buf.write("\u00dc\7\24\2\2\u00db\u00da\3\2\2\2\u00db\u00dc\3\2\2")
        buf.write("\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\5&\24\2\u00de\u00df")
        buf.write("\7;\2\2\u00df\u00e1\7+\2\2\u00e0\u00e2\5\36\20\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e4\7,\2\2\u00e4\u00e5\5.\30\2\u00e5\35\3\2\2")
        buf.write("\2\u00e6\u00eb\5 \21\2\u00e7\u00e8\7\61\2\2\u00e8\u00ea")
        buf.write("\5 \21\2\u00e9\u00e7\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\37\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ee\u00ef\5&\24\2\u00ef\u00f0\5\"\22")
        buf.write("\2\u00f0!\3\2\2\2\u00f1\u00f6\7;\2\2\u00f2\u00f3\7\64")
        buf.write("\2\2\u00f3\u00f5\7;\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f8")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("#\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\7;\2\2\u00fa")
        buf.write("\u00fc\7+\2\2\u00fb\u00fd\5\36\20\2\u00fc\u00fb\3\2\2")
        buf.write("\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff")
        buf.write("\7,\2\2\u00ff\u0100\5.\30\2\u0100%\3\2\2\2\u0101\u0105")
        buf.write("\5*\26\2\u0102\u0105\5(\25\2\u0103\u0105\7;\2\2\u0104")
        buf.write("\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2")
        buf.write("\u0105\'\3\2\2\2\u0106\u0109\5*\26\2\u0107\u0109\7;\2")
        buf.write("\2\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u010b\7-\2\2\u010b\u010c\7\65\2\2\u010c")
        buf.write("\u010d\7.\2\2\u010d)\3\2\2\2\u010e\u010f\t\2\2\2\u010f")
        buf.write("+\3\2\2\2\u0110\u011a\5.\30\2\u0111\u011a\5R*\2\u0112")
        buf.write("\u011a\5T+\2\u0113\u011a\5V,\2\u0114\u011a\5X-\2\u0115")
        buf.write("\u011a\5:\36\2\u0116\u011a\5D#\2\u0117\u011a\5F$\2\u0118")
        buf.write("\u011a\5N(\2\u0119\u0110\3\2\2\2\u0119\u0111\3\2\2\2\u0119")
        buf.write("\u0112\3\2\2\2\u0119\u0113\3\2\2\2\u0119\u0114\3\2\2\2")
        buf.write("\u0119\u0115\3\2\2\2\u0119\u0116\3\2\2\2\u0119\u0117\3")
        buf.write("\2\2\2\u0119\u0118\3\2\2\2\u011a-\3\2\2\2\u011b\u011d")
        buf.write("\7/\2\2\u011c\u011e\5\60\31\2\u011d\u011c\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u0121\5\62\32")
        buf.write("\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0123\7\60\2\2\u0123/\3\2\2\2\u0124\u0126")
        buf.write("\5\64\33\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\61\3\2\2\2\u0129")
        buf.write("\u012b\5,\27\2\u012a\u0129\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\63\3\2")
        buf.write("\2\2\u012e\u0131\5\66\34\2\u012f\u0131\58\35\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u012f\3\2\2\2\u0131\65\3\2\2\2\u0132\u0133")
        buf.write("\5&\24\2\u0133\u0134\5\24\13\2\u0134\u0135\7\61\2\2\u0135")
        buf.write("\67\3\2\2\2\u0136\u0137\7\23\2\2\u0137\u0138\5&\24\2\u0138")
        buf.write("\u0139\5\30\r\2\u0139\u013a\7\61\2\2\u013a9\3\2\2\2\u013b")
        buf.write("\u013c\5<\37\2\u013c\u013d\7)\2\2\u013d\u013e\5Z.\2\u013e")
        buf.write("\u013f\7\61\2\2\u013f;\3\2\2\2\u0140\u0141\7+\2\2\u0141")
        buf.write("\u0142\5<\37\2\u0142\u0143\7,\2\2\u0143\u0146\3\2\2\2")
        buf.write("\u0144\u0146\5> \2\u0145\u0140\3\2\2\2\u0145\u0144\3\2")
        buf.write("\2\2\u0146=\3\2\2\2\u0147\u014b\7;\2\2\u0148\u014b\5B")
        buf.write("\"\2\u0149\u014b\5@!\2\u014a\u0147\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014a\u0149\3\2\2\2\u014b?\3\2\2\2\u014c\u014d")
        buf.write("\5n8\2\u014d\u014e\7-\2\2\u014e\u014f\5Z.\2\u014f\u0150")
        buf.write("\7.\2\2\u0150A\3\2\2\2\u0151\u0152\5r:\2\u0152\u0153\7")
        buf.write("\63\2\2\u0153\u0154\7;\2\2\u0154\u015a\3\2\2\2\u0155\u0156")
        buf.write("\5r:\2\u0156\u0157\7\63\2\2\u0157\u0158\5p9\2\u0158\u015a")
        buf.write("\3\2\2\2\u0159\u0151\3\2\2\2\u0159\u0155\3\2\2\2\u015a")
        buf.write("C\3\2\2\2\u015b\u015c\7\b\2\2\u015c\u015d\5Z.\2\u015d")
        buf.write("\u015e\7\n\2\2\u015e\u015f\5,\27\2\u015fE\3\2\2\2\u0160")
        buf.write("\u0161\7\b\2\2\u0161\u0162\5Z.\2\u0162\u0163\7\n\2\2\u0163")
        buf.write("\u0164\5J&\2\u0164\u0165\7\t\2\2\u0165\u0166\5,\27\2\u0166")
        buf.write("G\3\2\2\2\u0167\u0168\7\b\2\2\u0168\u0169\5Z.\2\u0169")
        buf.write("\u016a\7\n\2\2\u016a\u016b\5J&\2\u016b\u016c\7\t\2\2\u016c")
        buf.write("\u016d\5J&\2\u016dI\3\2\2\2\u016e\u0172\5L\'\2\u016f\u0172")
        buf.write("\5H%\2\u0170\u0172\5P)\2\u0171\u016e\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0170\3\2\2\2\u0172K\3\2\2\2\u0173\u017a")
        buf.write("\5.\30\2\u0174\u017a\5R*\2\u0175\u017a\5T+\2\u0176\u017a")
        buf.write("\5V,\2\u0177\u017a\5X-\2\u0178\u017a\5:\36\2\u0179\u0173")
        buf.write("\3\2\2\2\u0179\u0174\3\2\2\2\u0179\u0175\3\2\2\2\u0179")
        buf.write("\u0176\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2")
        buf.write("\u017aM\3\2\2\2\u017b\u017c\7\13\2\2\u017c\u017d\7;\2")
        buf.write("\2\u017d\u017e\7)\2\2\u017e\u017f\5Z.\2\u017f\u0180\3")
        buf.write("\2\2\2\u0180\u0181\t\3\2\2\u0181\u0182\5Z.\2\u0182\u0183")
        buf.write("\7\16\2\2\u0183\u0184\5,\27\2\u0184O\3\2\2\2\u0185\u0186")
        buf.write("\7\13\2\2\u0186\u0187\7;\2\2\u0187\u0188\7)\2\2\u0188")
        buf.write("\u0189\5Z.\2\u0189\u018a\3\2\2\2\u018a\u018b\t\3\2\2\u018b")
        buf.write("\u018c\5Z.\2\u018c\u018d\7\16\2\2\u018d\u018e\5J&\2\u018e")
        buf.write("Q\3\2\2\2\u018f\u0190\7\17\2\2\u0190\u0191\7\61\2\2\u0191")
        buf.write("S\3\2\2\2\u0192\u0193\7\20\2\2\u0193\u0194\7\61\2\2\u0194")
        buf.write("U\3\2\2\2\u0195\u0196\7\26\2\2\u0196\u0197\5Z.\2\u0197")
        buf.write("\u0198\7\61\2\2\u0198W\3\2\2\2\u0199\u019a\5Z.\2\u019a")
        buf.write("\u019b\7\63\2\2\u019b\u019c\5p9\2\u019c\u019d\7\61\2\2")
        buf.write("\u019dY\3\2\2\2\u019e\u019f\5\\/\2\u019f[\3\2\2\2\u01a0")
        buf.write("\u01a1\5^\60\2\u01a1\u01a2\t\4\2\2\u01a2\u01a3\5^\60\2")
        buf.write("\u01a3\u01a6\3\2\2\2\u01a4\u01a6\5^\60\2\u01a5\u01a0\3")
        buf.write("\2\2\2\u01a5\u01a4\3\2\2\2\u01a6]\3\2\2\2\u01a7\u01a8")
        buf.write("\5`\61\2\u01a8\u01a9\t\5\2\2\u01a9\u01aa\5`\61\2\u01aa")
        buf.write("\u01ad\3\2\2\2\u01ab\u01ad\5`\61\2\u01ac\u01a7\3\2\2\2")
        buf.write("\u01ac\u01ab\3\2\2\2\u01ad_\3\2\2\2\u01ae\u01af\b\61\1")
        buf.write("\2\u01af\u01b0\5b\62\2\u01b0\u01b6\3\2\2\2\u01b1\u01b2")
        buf.write("\f\4\2\2\u01b2\u01b3\t\6\2\2\u01b3\u01b5\5b\62\2\u01b4")
        buf.write("\u01b1\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7a\3\2\2\2\u01b8\u01b6\3\2\2")
        buf.write("\2\u01b9\u01ba\b\62\1\2\u01ba\u01bb\5d\63\2\u01bb\u01c1")
        buf.write("\3\2\2\2\u01bc\u01bd\f\4\2\2\u01bd\u01be\t\7\2\2\u01be")
        buf.write("\u01c0\5d\63\2\u01bf\u01bc\3\2\2\2\u01c0\u01c3\3\2\2\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2c\3\2\2")
        buf.write("\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\b\63\1\2\u01c5\u01c6")
        buf.write("\5f\64\2\u01c6\u01cc\3\2\2\2\u01c7\u01c8\f\4\2\2\u01c8")
        buf.write("\u01c9\t\b\2\2\u01c9\u01cb\5f\64\2\u01ca\u01c7\3\2\2\2")
        buf.write("\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cde\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0")
        buf.write("\b\64\1\2\u01d0\u01d1\5h\65\2\u01d1\u01d7\3\2\2\2\u01d2")
        buf.write("\u01d3\f\4\2\2\u01d3\u01d4\7(\2\2\u01d4\u01d6\5h\65\2")
        buf.write("\u01d5\u01d2\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3")
        buf.write("\2\2\2\u01d7\u01d8\3\2\2\2\u01d8g\3\2\2\2\u01d9\u01d7")
        buf.write("\3\2\2\2\u01da\u01db\7\'\2\2\u01db\u01de\5h\65\2\u01dc")
        buf.write("\u01de\5j\66\2\u01dd\u01da\3\2\2\2\u01dd\u01dc\3\2\2\2")
        buf.write("\u01dei\3\2\2\2\u01df\u01e0\t\7\2\2\u01e0\u01e3\5j\66")
        buf.write("\2\u01e1\u01e3\5l\67\2\u01e2\u01df\3\2\2\2\u01e2\u01e1")
        buf.write("\3\2\2\2\u01e3k\3\2\2\2\u01e4\u01e5\5n8\2\u01e5\u01e6")
        buf.write("\7-\2\2\u01e6\u01e7\5Z.\2\u01e7\u01e8\7.\2\2\u01e8\u01eb")
        buf.write("\3\2\2\2\u01e9\u01eb\5n8\2\u01ea\u01e4\3\2\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01ebm\3\2\2\2\u01ec\u01ed\b8\1\2\u01ed\u01ee")
        buf.write("\5r:\2\u01ee\u01f7\3\2\2\2\u01ef\u01f0\f\5\2\2\u01f0\u01f1")
        buf.write("\7\63\2\2\u01f1\u01f6\5p9\2\u01f2\u01f3\f\4\2\2\u01f3")
        buf.write("\u01f4\7\63\2\2\u01f4\u01f6\7;\2\2\u01f5\u01ef\3\2\2\2")
        buf.write("\u01f5\u01f2\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f7\u01f8\3\2\2\2\u01f8o\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01fa\u01fb\7;\2\2\u01fb\u01fd\7+\2\2\u01fc\u01fe")
        buf.write("\5v<\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff")
        buf.write("\3\2\2\2\u01ff\u0200\7,\2\2\u0200q\3\2\2\2\u0201\u0202")
        buf.write("\7\27\2\2\u0202\u0203\7;\2\2\u0203\u0205\7+\2\2\u0204")
        buf.write("\u0206\5v<\2\u0205\u0204\3\2\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write("\u0207\3\2\2\2\u0207\u020a\7,\2\2\u0208\u020a\5t;\2\u0209")
        buf.write("\u0201\3\2\2\2\u0209\u0208\3\2\2\2\u020as\3\2\2\2\u020b")
        buf.write("\u0214\5x=\2\u020c\u0214\7;\2\2\u020d\u0214\7\25\2\2\u020e")
        buf.write("\u020f\7+\2\2\u020f\u0210\5Z.\2\u0210\u0211\7,\2\2\u0211")
        buf.write("\u0214\3\2\2\2\u0212\u0214\7\30\2\2\u0213\u020b\3\2\2")
        buf.write("\2\u0213\u020c\3\2\2\2\u0213\u020d\3\2\2\2\u0213\u020e")
        buf.write("\3\2\2\2\u0213\u0212\3\2\2\2\u0214u\3\2\2\2\u0215\u021a")
        buf.write("\5Z.\2\u0216\u0217\7\64\2\2\u0217\u0219\5Z.\2\u0218\u0216")
        buf.write("\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021bw\3\2\2\2\u021c\u021a\3\2\2\2\u021d")
        buf.write("\u0223\7\65\2\2\u021e\u0223\7\66\2\2\u021f\u0223\7\67")
        buf.write("\2\2\u0220\u0223\78\2\2\u0221\u0223\5z>\2\u0222\u021d")
        buf.write("\3\2\2\2\u0222\u021e\3\2\2\2\u0222\u021f\3\2\2\2\u0222")
        buf.write("\u0220\3\2\2\2\u0222\u0221\3\2\2\2\u0223y\3\2\2\2\u0224")
        buf.write("\u0225\7/\2\2\u0225\u022a\5x=\2\u0226\u0227\7\64\2\2\u0227")
        buf.write("\u0229\5x=\2\u0228\u0226\3\2\2\2\u0229\u022c\3\2\2\2\u022a")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022d\3\2\2\2")
        buf.write("\u022c\u022a\3\2\2\2\u022d\u022e\7\60\2\2\u022e{\3\2\2")
        buf.write("\2\60\177\u0087\u008f\u0097\u00a2\u00be\u00c5\u00cb\u00d2")
        buf.write("\u00d8\u00db\u00e1\u00eb\u00f6\u00fc\u0104\u0108\u0119")
        buf.write("\u011d\u0120\u0127\u012c\u0130\u0145\u014a\u0159\u0171")
        buf.write("\u0179\u01a5\u01ac\u01b6\u01c1\u01cc\u01d7\u01dd\u01e2")
        buf.write("\u01ea\u01f5\u01f7\u01fd\u0205\u0209\u0213\u021a\u0222")
        buf.write("\u022a")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'int'", "'float'", "'string'", 
                     "'void'", "'if'", "'else'", "'then'", "'for'", "'to'", 
                     "'downto'", "'do'", "'break'", "'continue'", "'class'", 
                     "'extends'", "'final'", "'static'", "'this'", "'return'", 
                     "'new'", "'nil'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", 
                     "'||'", "'&&'", "'!'", "'^'", "':='", "'='", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "';'", "':'", "'.'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "BOOL", "INT", "FLOAT", "STRING", "VOID", 
                      "IF", "ELSE", "THEN", "FOR", "TO", "DOWNTO", "DO", 
                      "BREAK", "CONTINUE", "CLASS", "EXTENDS", "FINAL", 
                      "STATIC", "THIS", "RETURN", "NEW", "NIL", "ADD_OP", 
                      "SUB_OP", "MUL_OP", "FLOAT_DIV_OP", "INT_DIV_OP", 
                      "MOD_OP", "NEQ_OP", "EQ_OP", "LT_OP", "GT_OP", "LEQ_OP", 
                      "GEQ_OP", "OR_OP", "AND_OP", "NOT_OP", "CONCAT_OP", 
                      "ASSIGN_OP", "INIT_OP", "LP", "RP", "LSB", "RSB", 
                      "LCB", "RCB", "SEMI", "COLON", "DOT", "COMMA", "INTEGER_LITERAL", 
                      "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ID", "WS", "COMMENT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_test_expr = 1
    RULE_class_decl = 2
    RULE_class_body = 3
    RULE_class_body_decl = 4
    RULE_field_decl = 5
    RULE_const_field_decl = 6
    RULE_static_field_decl = 7
    RULE_static_constant_decl = 8
    RULE_var_decl_list = 9
    RULE_var_decl_unit = 10
    RULE_const_decl_list = 11
    RULE_const_decl_unit = 12
    RULE_method_decl = 13
    RULE_param_list = 14
    RULE_params = 15
    RULE_id_list = 16
    RULE_constructor_decl = 17
    RULE_bkooltype = 18
    RULE_array_type = 19
    RULE_primitive_type = 20
    RULE_stmt = 21
    RULE_block_stmt = 22
    RULE_local_decl_region = 23
    RULE_stmts = 24
    RULE_local_decl = 25
    RULE_local_var_decl = 26
    RULE_local_const_decl = 27
    RULE_assign_stmt = 28
    RULE_lhs = 29
    RULE_lhs_base = 30
    RULE_lhs_index_expr = 31
    RULE_lhs_member_access_expr = 32
    RULE_if_then_stmt = 33
    RULE_if_then_else_stmt = 34
    RULE_if_then_else_stmt_no_short_if = 35
    RULE_stmt_no_short_if = 36
    RULE_stmt_no_trailing_substmt = 37
    RULE_for_stmt = 38
    RULE_for_stmt_no_short_if = 39
    RULE_break_stmt = 40
    RULE_continue_stmt = 41
    RULE_return_stmt = 42
    RULE_method_invoke_stmt = 43
    RULE_expr = 44
    RULE_relational_expr = 45
    RULE_equality_expr = 46
    RULE_logical_expr = 47
    RULE_additive_expr = 48
    RULE_multiply_expr = 49
    RULE_concat_expr = 50
    RULE_negate_expr = 51
    RULE_unary_arithmetic_expr = 52
    RULE_index_expr = 53
    RULE_member_access_expr = 54
    RULE_method_call = 55
    RULE_new_expr = 56
    RULE_primary_expr = 57
    RULE_expr_list = 58
    RULE_literal = 59
    RULE_array_literal = 60

    ruleNames =  [ "program", "test_expr", "class_decl", "class_body", "class_body_decl", 
                   "field_decl", "const_field_decl", "static_field_decl", 
                   "static_constant_decl", "var_decl_list", "var_decl_unit", 
                   "const_decl_list", "const_decl_unit", "method_decl", 
                   "param_list", "params", "id_list", "constructor_decl", 
                   "bkooltype", "array_type", "primitive_type", "stmt", 
                   "block_stmt", "local_decl_region", "stmts", "local_decl", 
                   "local_var_decl", "local_const_decl", "assign_stmt", 
                   "lhs", "lhs_base", "lhs_index_expr", "lhs_member_access_expr", 
                   "if_then_stmt", "if_then_else_stmt", "if_then_else_stmt_no_short_if", 
                   "stmt_no_short_if", "stmt_no_trailing_substmt", "for_stmt", 
                   "for_stmt_no_short_if", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invoke_stmt", "expr", "relational_expr", 
                   "equality_expr", "logical_expr", "additive_expr", "multiply_expr", 
                   "concat_expr", "negate_expr", "unary_arithmetic_expr", 
                   "index_expr", "member_access_expr", "method_call", "new_expr", 
                   "primary_expr", "expr_list", "literal", "array_literal" ]

    EOF = Token.EOF
    BOOL=1
    INT=2
    FLOAT=3
    STRING=4
    VOID=5
    IF=6
    ELSE=7
    THEN=8
    FOR=9
    TO=10
    DOWNTO=11
    DO=12
    BREAK=13
    CONTINUE=14
    CLASS=15
    EXTENDS=16
    FINAL=17
    STATIC=18
    THIS=19
    RETURN=20
    NEW=21
    NIL=22
    ADD_OP=23
    SUB_OP=24
    MUL_OP=25
    FLOAT_DIV_OP=26
    INT_DIV_OP=27
    MOD_OP=28
    NEQ_OP=29
    EQ_OP=30
    LT_OP=31
    GT_OP=32
    LEQ_OP=33
    GEQ_OP=34
    OR_OP=35
    AND_OP=36
    NOT_OP=37
    CONCAT_OP=38
    ASSIGN_OP=39
    INIT_OP=40
    LP=41
    RP=42
    LSB=43
    RSB=44
    LCB=45
    RCB=46
    SEMI=47
    COLON=48
    DOT=49
    COMMA=50
    INTEGER_LITERAL=51
    FLOAT_LITERAL=52
    BOOLEAN_LITERAL=53
    STRING_LITERAL=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56
    ID=57
    WS=58
    COMMENT=59
    BLOCK_COMMENT=60
    LINE_COMMENT=61
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




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 122
                self.class_decl()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Test_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_test_expr




    def test_expr(self):

        localctx = BKOOLParser.Test_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_test_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.expr()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0)):
                    break

            self.state = 135
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

        def class_body(self):
            return self.getTypedRuleContext(BKOOLParser.Class_bodyContext,0)


        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BKOOLParser.CLASS)
            self.state = 138
            self.match(BKOOLParser.ID)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 139
                self.match(BKOOLParser.EXTENDS)
                self.state = 140
                self.match(BKOOLParser.ID)


            self.state = 143
            self.class_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def class_body_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_body_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_body_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_body




    def class_body(self):

        localctx = BKOOLParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKOOLParser.LCB)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 146
                self.class_body_decl()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_body_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Constructor_declContext,0)


        def field_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Field_declContext,0)


        def static_field_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Static_field_declContext,0)


        def const_field_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Const_field_declContext,0)


        def static_constant_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Static_constant_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_body_decl




    def class_body_decl(self):

        localctx = BKOOLParser.Class_body_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_body_decl)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.constructor_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.field_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.static_field_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.const_field_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.static_constant_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_field_decl




    def field_decl(self):

        localctx = BKOOLParser.Field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.bkooltype()
            self.state = 163
            self.var_decl_list()
            self.state = 164
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def const_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_const_field_decl




    def const_field_decl(self):

        localctx = BKOOLParser.Const_field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BKOOLParser.FINAL)
            self.state = 167
            self.bkooltype()
            self.state = 168
            self.const_decl_list()
            self.state = 169
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_static_field_decl




    def static_field_decl(self):

        localctx = BKOOLParser.Static_field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_static_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(BKOOLParser.STATIC)
            self.state = 172
            self.bkooltype()
            self.state = 173
            self.var_decl_list()
            self.state = 174
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_constant_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def const_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_static_constant_decl




    def static_constant_decl(self):

        localctx = BKOOLParser.Static_constant_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_static_constant_decl)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(BKOOLParser.STATIC)
                self.state = 177
                self.match(BKOOLParser.FINAL)
                self.state = 178
                self.bkooltype()
                self.state = 179
                self.const_decl_list()
                self.state = 180
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(BKOOLParser.FINAL)
                self.state = 183
                self.match(BKOOLParser.STATIC)
                self.state = 184
                self.bkooltype()
                self.state = 185
                self.const_decl_list()
                self.state = 186
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


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_decl_unitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_decl_unitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_list




    def var_decl_list(self):

        localctx = BKOOLParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.var_decl_unit()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 191
                self.match(BKOOLParser.COMMA)
                self.state = 192
                self.var_decl_unit()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT_OP(self):
            return self.getToken(BKOOLParser.INIT_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_unit




    def var_decl_unit(self):

        localctx = BKOOLParser.Var_decl_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_decl_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(BKOOLParser.ID)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INIT_OP:
                self.state = 199
                self.match(BKOOLParser.INIT_OP)
                self.state = 200
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_decl_unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Const_decl_unitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Const_decl_unitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_const_decl_list




    def const_decl_list(self):

        localctx = BKOOLParser.Const_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_const_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.const_decl_unit()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 204
                self.match(BKOOLParser.COMMA)
                self.state = 205
                self.const_decl_unit()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decl_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INIT_OP(self):
            return self.getToken(BKOOLParser.INIT_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_const_decl_unit




    def const_decl_unit(self):

        localctx = BKOOLParser.Const_decl_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_const_decl_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(BKOOLParser.ID)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INIT_OP:
                self.state = 212
                self.match(BKOOLParser.INIT_OP)
                self.state = 213
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

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 216
                self.match(BKOOLParser.STATIC)


            self.state = 219
            self.bkooltype()
            self.state = 220
            self.match(BKOOLParser.ID)
            self.state = 221
            self.match(BKOOLParser.LP)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 222
                self.param_list()


            self.state = 225
            self.match(BKOOLParser.RP)
            self.state = 226
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

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamsContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.params()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMI:
                self.state = 229
                self.match(BKOOLParser.SEMI)
                self.state = 230
                self.params()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def id_list(self):
            return self.getTypedRuleContext(BKOOLParser.Id_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.bkooltype()
            self.state = 237
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_id_list




    def id_list(self):

        localctx = BKOOLParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BKOOLParser.ID)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 240
                self.match(BKOOLParser.COMMA)
                self.state = 241
                self.match(BKOOLParser.ID)
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor_decl




    def constructor_decl(self):

        localctx = BKOOLParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constructor_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BKOOLParser.ID)
            self.state = 248
            self.match(BKOOLParser.LP)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 249
                self.param_list()


            self.state = 252
            self.match(BKOOLParser.RP)
            self.state = 253
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BkooltypeContext(ParserRuleContext):
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
            return BKOOLParser.RULE_bkooltype




    def bkooltype(self):

        localctx = BKOOLParser.BkooltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_bkooltype)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(BKOOLParser.ID)
                pass


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

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOL, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.VOID]:
                self.state = 260
                self.primitive_type()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 261
                self.match(BKOOLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 264
            self.match(BKOOLParser.LSB)
            self.state = 265
            self.match(BKOOLParser.INTEGER_LITERAL)
            self.state = 266
            self.match(BKOOLParser.RSB)
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

        def BOOL(self):
            return self.getToken(BKOOLParser.BOOL, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOL) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def method_invoke_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoke_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def if_then_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_stmtContext,0)


        def if_then_else_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_else_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 274
                self.method_invoke_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 275
                self.assign_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 276
                self.if_then_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 277
                self.if_then_else_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 278
                self.for_stmt()
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

        def local_decl_region(self):
            return self.getTypedRuleContext(BKOOLParser.Local_decl_regionContext,0)


        def stmts(self):
            return self.getTypedRuleContext(BKOOLParser.StmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKOOLParser.LCB)
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 282
                self.local_decl_region()


            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 285
                self.stmts()


            self.state = 288
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_decl_regionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Local_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Local_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_local_decl_region




    def local_decl_region(self):

        localctx = BKOOLParser.Local_decl_regionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_local_decl_region)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 290
                    self.local_decl()

                else:
                    raise NoViableAltException(self)
                self.state = 293 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmts




    def stmts(self):

        localctx = BKOOLParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 295
                self.stmt()
                self.state = 298 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Local_var_declContext,0)


        def local_const_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Local_const_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_local_decl




    def local_decl(self):

        localctx = BKOOLParser.Local_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_local_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOL, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.state = 300
                self.local_var_decl()
                pass
            elif token in [BKOOLParser.FINAL]:
                self.state = 301
                self.local_const_decl()
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


    class Local_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_local_var_decl




    def local_var_decl(self):

        localctx = BKOOLParser.Local_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_local_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.bkooltype()
            self.state = 305
            self.var_decl_list()
            self.state = 306
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def bkooltype(self):
            return self.getTypedRuleContext(BKOOLParser.BkooltypeContext,0)


        def const_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Const_decl_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_local_const_decl




    def local_const_decl(self):

        localctx = BKOOLParser.Local_const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_local_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(BKOOLParser.FINAL)
            self.state = 309
            self.bkooltype()
            self.state = 310
            self.const_decl_list()
            self.state = 311
            self.match(BKOOLParser.SEMI)
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


        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.lhs()
            self.state = 314
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 315
            self.expr()
            self.state = 316
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

        def lhs_base(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_baseContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lhs)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(BKOOLParser.LP)
                self.state = 319
                self.lhs()
                self.state = 320
                self.match(BKOOLParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.lhs_base()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_baseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def lhs_member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_member_access_exprContext,0)


        def lhs_index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Lhs_index_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_base




    def lhs_base(self):

        localctx = BKOOLParser.Lhs_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs_base)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.lhs_member_access_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.lhs_index_expr()
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

        def member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_exprContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_index_expr




    def lhs_index_expr(self):

        localctx = BKOOLParser.Lhs_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.member_access_expr(0)

            self.state = 331
            self.match(BKOOLParser.LSB)
            self.state = 332
            self.expr()
            self.state = 333
            self.match(BKOOLParser.RSB)
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

        def new_expr(self):
            return self.getTypedRuleContext(BKOOLParser.New_exprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs_member_access_expr




    def lhs_member_access_expr(self):

        localctx = BKOOLParser.Lhs_member_access_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lhs_member_access_expr)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.new_expr()
                self.state = 336
                localctx.bop = self.match(BKOOLParser.DOT)

                self.state = 337
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.new_expr()
                self.state = 340
                localctx.bop = self.match(BKOOLParser.DOT)

                self.state = 341
                self.method_call()
                pass


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




    def if_then_stmt(self):

        localctx = BKOOLParser.If_then_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_then_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BKOOLParser.IF)
            self.state = 346
            self.expr()
            self.state = 347
            self.match(BKOOLParser.THEN)
            self.state = 348
            self.stmt()
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

        def stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_no_short_ifContext,0)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_then_else_stmt




    def if_then_else_stmt(self):

        localctx = BKOOLParser.If_then_else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_then_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(BKOOLParser.IF)
            self.state = 351
            self.expr()
            self.state = 352
            self.match(BKOOLParser.THEN)
            self.state = 353
            self.stmt_no_short_if()
            self.state = 354
            self.match(BKOOLParser.ELSE)
            self.state = 355
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_else_stmt_no_short_ifContext(ParserRuleContext):
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

        def stmt_no_short_if(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Stmt_no_short_ifContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Stmt_no_short_ifContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_then_else_stmt_no_short_if




    def if_then_else_stmt_no_short_if(self):

        localctx = BKOOLParser.If_then_else_stmt_no_short_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_then_else_stmt_no_short_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(BKOOLParser.IF)
            self.state = 358
            self.expr()
            self.state = 359
            self.match(BKOOLParser.THEN)
            self.state = 360
            self.stmt_no_short_if()
            self.state = 361
            self.match(BKOOLParser.ELSE)
            self.state = 362
            self.stmt_no_short_if()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_no_short_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_no_trailing_substmt(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_no_trailing_substmtContext,0)


        def if_then_else_stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.If_then_else_stmt_no_short_ifContext,0)


        def for_stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmt_no_short_ifContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_no_short_if




    def stmt_no_short_if(self):

        localctx = BKOOLParser.Stmt_no_short_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt_no_short_if)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.RETURN, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.NOT_OP, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.stmt_no_trailing_substmt()
                pass
            elif token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.if_then_else_stmt_no_short_if()
                pass
            elif token in [BKOOLParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 366
                self.for_stmt_no_short_if()
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


    class Stmt_no_trailing_substmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def method_invoke_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoke_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_no_trailing_substmt




    def stmt_no_trailing_substmt(self):

        localctx = BKOOLParser.Stmt_no_trailing_substmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt_no_trailing_substmt)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 373
                self.method_invoke_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 374
                self.assign_stmt()
                pass


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

        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(BKOOLParser.FOR)

            self.state = 378
            self.match(BKOOLParser.ID)
            self.state = 379
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 380
            self.expr()
            self.state = 382
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 383
            self.expr()
            self.state = 384
            self.match(BKOOLParser.DO)
            self.state = 385
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmt_no_short_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt_no_short_if(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_no_short_ifContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt_no_short_if




    def for_stmt_no_short_if(self):

        localctx = BKOOLParser.For_stmt_no_short_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_for_stmt_no_short_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(BKOOLParser.FOR)

            self.state = 388
            self.match(BKOOLParser.ID)
            self.state = 389
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 390
            self.expr()
            self.state = 392
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 393
            self.expr()
            self.state = 394
            self.match(BKOOLParser.DO)
            self.state = 395
            self.stmt_no_short_if()
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
        self.enterRule(localctx, 80, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(BKOOLParser.BREAK)
            self.state = 398
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
        self.enterRule(localctx, 82, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(BKOOLParser.CONTINUE)
            self.state = 401
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
        self.enterRule(localctx, 84, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(BKOOLParser.RETURN)
            self.state = 404
            self.expr()
            self.state = 405
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoke_stmtContext(ParserRuleContext):
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
            return BKOOLParser.RULE_method_invoke_stmt




    def method_invoke_stmt(self):

        localctx = BKOOLParser.Method_invoke_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_method_invoke_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr()
            self.state = 408
            self.match(BKOOLParser.DOT)
            self.state = 409
            self.method_call()
            self.state = 410
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

        def relational_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Relational_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.relational_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Equality_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Equality_exprContext,i)


        def LT_OP(self):
            return self.getToken(BKOOLParser.LT_OP, 0)

        def GT_OP(self):
            return self.getToken(BKOOLParser.GT_OP, 0)

        def LEQ_OP(self):
            return self.getToken(BKOOLParser.LEQ_OP, 0)

        def GEQ_OP(self):
            return self.getToken(BKOOLParser.GEQ_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_relational_expr




    def relational_expr(self):

        localctx = BKOOLParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.equality_expr()
                self.state = 415
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT_OP) | (1 << BKOOLParser.GT_OP) | (1 << BKOOLParser.LEQ_OP) | (1 << BKOOLParser.GEQ_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 416
                self.equality_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.equality_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Logical_exprContext,i)


        def EQ_OP(self):
            return self.getToken(BKOOLParser.EQ_OP, 0)

        def NEQ_OP(self):
            return self.getToken(BKOOLParser.NEQ_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_equality_expr




    def equality_expr(self):

        localctx = BKOOLParser.Equality_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_equality_expr)
        self._la = 0 # Token type
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.logical_expr(0)
                self.state = 422
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ_OP or _la==BKOOLParser.EQ_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 423
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.logical_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Additive_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Logical_exprContext,0)


        def AND_OP(self):
            return self.getToken(BKOOLParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(BKOOLParser.OR_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_logical_expr



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.additive_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 432
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR_OP or _la==BKOOLParser.AND_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 433
                    self.additive_expr(0) 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Additive_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiply_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiply_exprContext,0)


        def additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Additive_exprContext,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_additive_expr



    def additive_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Additive_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_additive_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.multiply_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Additive_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expr)
                    self.state = 442
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 443
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 444
                    self.multiply_expr(0) 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiply_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Concat_exprContext,0)


        def multiply_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiply_exprContext,0)


        def MUL_OP(self):
            return self.getToken(BKOOLParser.MUL_OP, 0)

        def FLOAT_DIV_OP(self):
            return self.getToken(BKOOLParser.FLOAT_DIV_OP, 0)

        def INT_DIV_OP(self):
            return self.getToken(BKOOLParser.INT_DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(BKOOLParser.MOD_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_multiply_expr



    def multiply_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Multiply_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_multiply_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.concat_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Multiply_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiply_expr)
                    self.state = 453
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 454
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL_OP) | (1 << BKOOLParser.FLOAT_DIV_OP) | (1 << BKOOLParser.INT_DIV_OP) | (1 << BKOOLParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 455
                    self.concat_expr(0) 
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Concat_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negate_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Negate_exprContext,0)


        def concat_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Concat_exprContext,0)


        def CONCAT_OP(self):
            return self.getToken(BKOOLParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_concat_expr



    def concat_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Concat_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_concat_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.negate_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 469
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Concat_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_concat_expr)
                    self.state = 464
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 465
                    self.match(BKOOLParser.CONCAT_OP)
                    self.state = 466
                    self.negate_expr() 
                self.state = 471
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negate_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negate_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Negate_exprContext,0)


        def NOT_OP(self):
            return self.getToken(BKOOLParser.NOT_OP, 0)

        def unary_arithmetic_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Unary_arithmetic_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_negate_expr




    def negate_expr(self):

        localctx = BKOOLParser.Negate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_negate_expr)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(BKOOLParser.NOT_OP)
                self.state = 473
                self.negate_expr()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.unary_arithmetic_expr()
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


    class Unary_arithmetic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_arithmetic_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Unary_arithmetic_exprContext,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_unary_arithmetic_expr




    def unary_arithmetic_expr(self):

        localctx = BKOOLParser.Unary_arithmetic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_unary_arithmetic_expr)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD_OP, BKOOLParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 478
                self.unary_arithmetic_expr()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.index_expr()
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


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_exprContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_index_expr




    def index_expr(self):

        localctx = BKOOLParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index_expr)
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.member_access_expr(0)

                self.state = 483
                self.match(BKOOLParser.LSB)
                self.state = 484
                self.expr()
                self.state = 485
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.member_access_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def new_expr(self):
            return self.getTypedRuleContext(BKOOLParser.New_exprContext,0)


        def member_access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_exprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def method_call(self):
            return self.getTypedRuleContext(BKOOLParser.Method_callContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access_expr



    def member_access_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Member_access_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_member_access_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.new_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 501
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 499
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Member_access_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expr)
                        self.state = 493
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 494
                        localctx.bop = self.match(BKOOLParser.DOT)

                        self.state = 495
                        self.method_call()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Member_access_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expr)
                        self.state = 496
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 497
                        localctx.bop = self.match(BKOOLParser.DOT)

                        self.state = 498
                        self.match(BKOOLParser.ID)
                        pass

             
                self.state = 503
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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




    def method_call(self):

        localctx = BKOOLParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(BKOOLParser.ID)
            self.state = 505
            self.match(BKOOLParser.LP)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 506
                self.expr_list()


            self.state = 509
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_exprContext(ParserRuleContext):
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


        def primary_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Primary_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_new_expr




    def new_expr(self):

        localctx = BKOOLParser.New_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_new_expr)
        self._la = 0 # Token type
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(BKOOLParser.NEW)
                self.state = 512
                self.match(BKOOLParser.ID)
                self.state = 513
                self.match(BKOOLParser.LP)
                self.state = 515
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.ADD_OP) | (1 << BKOOLParser.SUB_OP) | (1 << BKOOLParser.NOT_OP) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.BOOLEAN_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 514
                    self.expr_list()


                self.state = 517
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NIL, BKOOLParser.LP, BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.primary_expr()
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


    class Primary_exprContext(ParserRuleContext):
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
            return BKOOLParser.RULE_primary_expr




    def primary_expr(self):

        localctx = BKOOLParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_primary_expr)
        try:
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LCB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.BOOLEAN_LITERAL, BKOOLParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.literal()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.match(BKOOLParser.LP)
                self.state = 525
                self.expr()
                self.state = 526
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 528
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_list




    def expr_list(self):

        localctx = BKOOLParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.expr()
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 532
                self.match(BKOOLParser.COMMA)
                self.state = 533
                self.expr()
                self.state = 538
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BKOOLParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BKOOLParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BKOOLParser.STRING_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(BKOOLParser.Array_literalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_literal)
        try:
            self.state = 544
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.match(BKOOLParser.INTEGER_LITERAL)
                pass
            elif token in [BKOOLParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.match(BKOOLParser.FLOAT_LITERAL)
                pass
            elif token in [BKOOLParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self.match(BKOOLParser.BOOLEAN_LITERAL)
                pass
            elif token in [BKOOLParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 542
                self.match(BKOOLParser.STRING_LITERAL)
                pass
            elif token in [BKOOLParser.LCB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 543
                self.array_literal()
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_literal




    def array_literal(self):

        localctx = BKOOLParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(BKOOLParser.LCB)

            self.state = 547
            self.literal()
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 548
                self.match(BKOOLParser.COMMA)
                self.state = 549
                self.literal()
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 555
            self.match(BKOOLParser.RCB)
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
        self._predicates[47] = self.logical_expr_sempred
        self._predicates[48] = self.additive_expr_sempred
        self._predicates[49] = self.multiply_expr_sempred
        self._predicates[50] = self.concat_expr_sempred
        self._predicates[54] = self.member_access_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def additive_expr_sempred(self, localctx:Additive_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiply_expr_sempred(self, localctx:Multiply_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def concat_expr_sempred(self, localctx:Concat_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def member_access_expr_sempred(self, localctx:Member_access_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




