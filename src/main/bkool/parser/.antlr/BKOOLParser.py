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
        buf.write("\u016e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\3\2\3\3\3\3\3\3\3\3\5\3U\n\3\3\3\3\3\7\3")
        buf.write("Y\n\3\f\3\16\3\\\13\3\3\3\3\3\3\4\3\4\5\4b\n\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5j\n\5\3\5\3\5\3\6\3\6\5\6p\n\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\5\n\177")
        buf.write("\n\n\3\n\3\n\3\n\3\n\3\n\5\n\u0086\n\n\5\n\u0088\n\n\3")
        buf.write("\13\5\13\u008b\n\13\3\13\3\13\5\13\u008f\n\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u009b\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\5\f\u00a2\n\f\3\r\3\r\3\16\3\16")
        buf.write("\3\16\5\16\u00a9\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00bb\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00c2\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\7\25\u00ca\n\25\f\25\16\25")
        buf.write("\u00cd\13\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00d5")
        buf.write("\n\26\f\26\16\26\u00d8\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\7\27\u00e0\n\27\f\27\16\27\u00e3\13\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\7\30\u00eb\n\30\f\30\16\30\u00ee")
        buf.write("\13\30\3\31\3\31\3\31\5\31\u00f3\n\31\3\32\3\32\3\32\5")
        buf.write("\32\u00f8\n\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0100")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0108\n\34\3")
        buf.write("\34\5\34\u010b\n\34\3\34\3\34\3\34\3\34\3\34\5\34\u0112")
        buf.write("\n\34\3\34\5\34\u0115\n\34\7\34\u0117\n\34\f\34\16\34")
        buf.write("\u011a\13\34\3\35\3\35\3\35\3\35\5\35\u0120\n\35\3\35")
        buf.write("\3\35\5\35\u0124\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u012e\n\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0137\n\37\3 \3 \5 \u013b\n \3!\3!\5!\u013f")
        buf.write("\n!\3!\3!\3\"\5\"\u0144\n\"\3\"\7\"\u0147\n\"\f\"\16\"")
        buf.write("\u014a\13\"\3\"\7\"\u014d\n\"\f\"\16\"\u0150\13\"\3#\3")
        buf.write("#\5#\u0154\n#\3#\3#\3#\3#\3$\3$\3$\3$\3$\5$\u015f\n$\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\5&\u016a\n&\3\'\3\'\3\'\2\7")
        buf.write("(*,.\66(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJL\2\t\6\2\5\5\f\f\16\16\20\20")
        buf.write("\3\2%(\3\2#$\3\2)*\3\2\35\36\3\2\37\"\3\28;\2\u0178\2")
        buf.write("N\3\2\2\2\4P\3\2\2\2\6a\3\2\2\2\bi\3\2\2\2\no\3\2\2\2")
        buf.write("\fs\3\2\2\2\16v\3\2\2\2\20y\3\2\2\2\22\u0087\3\2\2\2\24")
        buf.write("\u009a\3\2\2\2\26\u00a1\3\2\2\2\30\u00a3\3\2\2\2\32\u00a8")
        buf.write("\3\2\2\2\34\u00aa\3\2\2\2\36\u00ac\3\2\2\2 \u00ae\3\2")
        buf.write("\2\2\"\u00b3\3\2\2\2$\u00ba\3\2\2\2&\u00c1\3\2\2\2(\u00c3")
        buf.write("\3\2\2\2*\u00ce\3\2\2\2,\u00d9\3\2\2\2.\u00e4\3\2\2\2")
        buf.write("\60\u00f2\3\2\2\2\62\u00f7\3\2\2\2\64\u00ff\3\2\2\2\66")
        buf.write("\u0101\3\2\2\28\u011b\3\2\2\2:\u012d\3\2\2\2<\u0136\3")
        buf.write("\2\2\2>\u013a\3\2\2\2@\u013c\3\2\2\2B\u0148\3\2\2\2D\u0153")
        buf.write("\3\2\2\2F\u015e\3\2\2\2H\u0160\3\2\2\2J\u0169\3\2\2\2")
        buf.write("L\u016b\3\2\2\2NO\3\2\2\2O\3\3\2\2\2PQ\7\7\2\2QT\7<\2")
        buf.write("\2RS\7\13\2\2SU\7<\2\2TR\3\2\2\2TU\3\2\2\2UV\3\2\2\2V")
        buf.write("Z\7\60\2\2WY\5\6\4\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[")
        buf.write("\3\2\2\2[]\3\2\2\2\\Z\3\2\2\2]^\7\61\2\2^\5\3\2\2\2_b")
        buf.write("\5\b\5\2`b\5\24\13\2a_\3\2\2\2a`\3\2\2\2b\7\3\2\2\2cj")
        buf.write("\7\32\2\2dj\7\31\2\2ef\7\32\2\2fj\7\31\2\2gh\7\31\2\2")
        buf.write("hj\7\32\2\2ic\3\2\2\2id\3\2\2\2ie\3\2\2\2ig\3\2\2\2ij")
        buf.write("\3\2\2\2jk\3\2\2\2kl\5\n\6\2l\t\3\2\2\2mp\5\f\7\2np\5")
        buf.write("\16\b\2om\3\2\2\2on\3\2\2\2pq\3\2\2\2qr\7\64\2\2r\13\3")
        buf.write("\2\2\2st\5\32\16\2tu\5\20\t\2u\r\3\2\2\2vw\5\32\16\2w")
        buf.write("x\5\20\t\2x\17\3\2\2\2yz\5\22\n\2z\21\3\2\2\2{~\7<\2\2")
        buf.write("|}\7$\2\2}\177\5$\23\2~|\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0081\7\67\2\2\u0081\u0088\5\22\n\2\u0082")
        buf.write("\u0085\7<\2\2\u0083\u0084\7$\2\2\u0084\u0086\5$\23\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088\3\2\2\2")
        buf.write("\u0087{\3\2\2\2\u0087\u0082\3\2\2\2\u0088\23\3\2\2\2\u0089")
        buf.write("\u008b\7\32\2\2\u008a\u0089\3\2\2\2\u008a\u008b\3\2\2")
        buf.write("\2\u008b\u008e\3\2\2\2\u008c\u008f\5\32\16\2\u008d\u008f")
        buf.write("\5\36\20\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u0091\7<\2\2\u0091\u0092\7\62\2\2")
        buf.write("\u0092\u0093\5\26\f\2\u0093\u0094\7\63\2\2\u0094\u0095")
        buf.write("\5@!\2\u0095\u009b\3\2\2\2\u0096\u0097\7<\2\2\u0097\u0098")
        buf.write("\5\26\f\2\u0098\u0099\5@!\2\u0099\u009b\3\2\2\2\u009a")
        buf.write("\u008a\3\2\2\2\u009a\u0096\3\2\2\2\u009b\25\3\2\2\2\u009c")
        buf.write("\u009d\5\30\r\2\u009d\u009e\7\64\2\2\u009e\u009f\5\26")
        buf.write("\f\2\u009f\u00a2\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009c")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\27\3\2\2\2\u00a3\u00a4")
        buf.write("\5\22\n\2\u00a4\31\3\2\2\2\u00a5\u00a9\5\34\17\2\u00a6")
        buf.write("\u00a9\5 \21\2\u00a7\u00a9\5\"\22\2\u00a8\u00a5\3\2\2")
        buf.write("\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\33\3")
        buf.write("\2\2\2\u00aa\u00ab\t\2\2\2\u00ab\35\3\2\2\2\u00ac\u00ad")
        buf.write("\7\26\2\2\u00ad\37\3\2\2\2\u00ae\u00af\5\34\17\2\u00af")
        buf.write("\u00b0\7.\2\2\u00b0\u00b1\78\2\2\u00b1\u00b2\7/\2\2\u00b2")
        buf.write("!\3\2\2\2\u00b3\u00b4\7<\2\2\u00b4#\3\2\2\2\u00b5\u00b6")
        buf.write("\5&\24\2\u00b6\u00b7\t\3\2\2\u00b7\u00b8\5&\24\2\u00b8")
        buf.write("\u00bb\3\2\2\2\u00b9\u00bb\5&\24\2\u00ba\u00b5\3\2\2\2")
        buf.write("\u00ba\u00b9\3\2\2\2\u00bb%\3\2\2\2\u00bc\u00bd\5(\25")
        buf.write("\2\u00bd\u00be\t\4\2\2\u00be\u00bf\5(\25\2\u00bf\u00c2")
        buf.write("\3\2\2\2\u00c0\u00c2\5(\25\2\u00c1\u00bc\3\2\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\'\3\2\2\2\u00c3\u00c4\b\25\1\2\u00c4")
        buf.write("\u00c5\5*\26\2\u00c5\u00cb\3\2\2\2\u00c6\u00c7\f\4\2\2")
        buf.write("\u00c7\u00c8\t\5\2\2\u00c8\u00ca\5*\26\2\u00c9\u00c6\3")
        buf.write("\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc)\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00cf")
        buf.write("\b\26\1\2\u00cf\u00d0\5,\27\2\u00d0\u00d6\3\2\2\2\u00d1")
        buf.write("\u00d2\f\4\2\2\u00d2\u00d3\t\6\2\2\u00d3\u00d5\5,\27\2")
        buf.write("\u00d4\u00d1\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d6\u00d7\3\2\2\2\u00d7+\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d9\u00da\b\27\1\2\u00da\u00db\5.\30\2\u00db")
        buf.write("\u00e1\3\2\2\2\u00dc\u00dd\f\4\2\2\u00dd\u00de\t\7\2\2")
        buf.write("\u00de\u00e0\5.\30\2\u00df\u00dc\3\2\2\2\u00e0\u00e3\3")
        buf.write("\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2-")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\b\30\1\2\u00e5")
        buf.write("\u00e6\5\60\31\2\u00e6\u00ec\3\2\2\2\u00e7\u00e8\f\4\2")
        buf.write("\2\u00e8\u00e9\7,\2\2\u00e9\u00eb\5\60\31\2\u00ea\u00e7")
        buf.write("\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed/\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef")
        buf.write("\u00f0\7+\2\2\u00f0\u00f3\5\60\31\2\u00f1\u00f3\5\62\32")
        buf.write("\2\u00f2\u00ef\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\61\3")
        buf.write("\2\2\2\u00f4\u00f5\t\6\2\2\u00f5\u00f8\5\62\32\2\u00f6")
        buf.write("\u00f8\5\64\33\2\u00f7\u00f4\3\2\2\2\u00f7\u00f6\3\2\2")
        buf.write("\2\u00f8\63\3\2\2\2\u00f9\u00fa\5\66\34\2\u00fa\u00fb")
        buf.write("\7.\2\2\u00fb\u00fc\5$\23\2\u00fc\u00fd\7/\2\2\u00fd\u0100")
        buf.write("\3\2\2\2\u00fe\u0100\5\66\34\2\u00ff\u00f9\3\2\2\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u0100\65\3\2\2\2\u0101\u0102\b\34\1\2\u0102")
        buf.write("\u0103\7<\2\2\u0103\u0104\7\66\2\2\u0104\u010a\7<\2\2")
        buf.write("\u0105\u0107\7\62\2\2\u0106\u0108\5<\37\2\u0107\u0106")
        buf.write("\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\u010b\7\63\2\2\u010a\u0105\3\2\2\2\u010a\u010b\3\2\2")
        buf.write("\2\u010b\u0118\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e")
        buf.write("\7\66\2\2\u010e\u0114\7<\2\2\u010f\u0111\7\62\2\2\u0110")
        buf.write("\u0112\5<\37\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0113\3\2\2\2\u0113\u0115\7\63\2\2\u0114\u010f")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2\u0116")
        buf.write("\u010c\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\67\3\2\2\2\u011a\u0118\3\2")
        buf.write("\2\2\u011b\u011c\7\17\2\2\u011c\u011d\7<\2\2\u011d\u011f")
        buf.write("\7\62\2\2\u011e\u0120\5<\37\2\u011f\u011e\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\7\63\2")
        buf.write("\2\u0122\u0124\58\35\2\u0123\u0122\3\2\2\2\u0123\u0124")
        buf.write("\3\2\2\2\u01249\3\2\2\2\u0125\u0126\7\62\2\2\u0126\u0127")
        buf.write("\5$\23\2\u0127\u0128\7\63\2\2\u0128\u012e\3\2\2\2\u0129")
        buf.write("\u012e\7<\2\2\u012a\u012e\5F$\2\u012b\u012e\7\30\2\2\u012c")
        buf.write("\u012e\7\27\2\2\u012d\u0125\3\2\2\2\u012d\u0129\3\2\2")
        buf.write("\2\u012d\u012a\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e;\3\2\2\2\u012f\u0130\5$\23\2\u0130\u0131")
        buf.write("\7\67\2\2\u0131\u0132\5<\37\2\u0132\u0137\3\2\2\2\u0133")
        buf.write("\u0134\5$\23\2\u0134\u0135\7\67\2\2\u0135\u0137\3\2\2")
        buf.write("\2\u0136\u012f\3\2\2\2\u0136\u0133\3\2\2\2\u0137=\3\2")
        buf.write("\2\2\u0138\u013b\5@!\2\u0139\u013b\5D#\2\u013a\u0138\3")
        buf.write("\2\2\2\u013a\u0139\3\2\2\2\u013b?\3\2\2\2\u013c\u013e")
        buf.write("\7\60\2\2\u013d\u013f\5B\"\2\u013e\u013d\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\7\61\2")
        buf.write("\2\u0141A\3\2\2\2\u0142\u0144\7\31\2\2\u0143\u0142\3\2")
        buf.write("\2\2\u0143\u0144\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0147")
        buf.write("\5\n\6\2\u0146\u0143\3\2\2\2\u0147\u014a\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014e\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014b\u014d\5> \2\u014c\u014b\3\2")
        buf.write("\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014fC\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0154")
        buf.write("\7<\2\2\u0152\u0154\5\64\33\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\7-\2\2")
        buf.write("\u0156\u0157\5$\23\2\u0157\u0158\7\64\2\2\u0158E\3\2\2")
        buf.write("\2\u0159\u015f\78\2\2\u015a\u015f\79\2\2\u015b\u015f\7")
        buf.write(":\2\2\u015c\u015f\7;\2\2\u015d\u015f\5H%\2\u015e\u0159")
        buf.write("\3\2\2\2\u015e\u015a\3\2\2\2\u015e\u015b\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015fG\3\2\2\2\u0160")
        buf.write("\u0161\7\60\2\2\u0161\u0162\5J&\2\u0162\u0163\7\61\2\2")
        buf.write("\u0163I\3\2\2\2\u0164\u0165\5L\'\2\u0165\u0166\7\67\2")
        buf.write("\2\u0166\u0167\5J&\2\u0167\u016a\3\2\2\2\u0168\u016a\5")
        buf.write("L\'\2\u0169\u0164\3\2\2\2\u0169\u0168\3\2\2\2\u016aK\3")
        buf.write("\2\2\2\u016b\u016c\t\b\2\2\u016cM\3\2\2\2)TZaio~\u0085")
        buf.write("\u0087\u008a\u008e\u009a\u00a1\u00a8\u00ba\u00c1\u00cb")
        buf.write("\u00d6\u00e1\u00ec\u00f2\u00f7\u00ff\u0107\u010a\u0111")
        buf.write("\u0114\u0118\u011f\u0123\u012d\u0136\u013a\u013e\u0143")
        buf.write("\u0148\u014e\u0153\u015e\u0169")
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
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
    RULE_literal = 34
    RULE_arr_lit = 35
    RULE_arr_decl = 36
    RULE_arr_val = 37

    ruleNames =  [ "program", "class_decl", "member", "attribute_decl", 
                   "var_decl", "immutable_attribute", "mutable_attribute", 
                   "attribute", "idlist", "method_decl", "paralist", "para_decl", 
                   "data_type", "not_void_type", "void_type", "arr_type", 
                   "class_type", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "exprlist", "stmt", "block_stmt", "mem_stmt", 
                   "assignment_decl", "literal", "arr_lit", "arr_decl", 
                   "arr_val" ]

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
    WS=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

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
            self.state = 78
            self.match(BKOOLParser.CLASS)
            self.state = 79
            self.match(BKOOLParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 80
                self.match(BKOOLParser.EXTENDS)
                self.state = 81
                self.match(BKOOLParser.ID)


            self.state = 84
            self.match(BKOOLParser.LP)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 85
                self.member()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 97
                self.match(BKOOLParser.STATIC)

            elif la_ == 2:
                self.state = 98
                self.match(BKOOLParser.FINAL)

            elif la_ == 3:
                self.state = 99
                self.match(BKOOLParser.STATIC)
                self.state = 100
                self.match(BKOOLParser.FINAL)

            elif la_ == 4:
                self.state = 101
                self.match(BKOOLParser.FINAL)
                self.state = 102
                self.match(BKOOLParser.STATIC)


            self.state = 105
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
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 107
                self.immutable_attribute()
                pass

            elif la_ == 2:
                self.state = 108
                self.mutable_attribute()
                pass


            self.state = 111
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
            self.state = 113
            self.data_type()
            self.state = 114
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
            self.state = 116
            self.data_type()
            self.state = 117
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
            self.state = 119
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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(BKOOLParser.ID)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 122
                    self.match(BKOOLParser.EQUAL)
                    self.state = 123
                    self.expr()


                self.state = 126
                self.match(BKOOLParser.COMMA)
                self.state = 127
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(BKOOLParser.ID)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.EQUAL:
                    self.state = 129
                    self.match(BKOOLParser.EQUAL)
                    self.state = 130
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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 135
                    self.match(BKOOLParser.STATIC)


                self.state = 140
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                    self.state = 138
                    self.data_type()
                    pass
                elif token in [BKOOLParser.VOID]:
                    self.state = 139
                    self.void_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 142
                self.match(BKOOLParser.ID)
                self.state = 143
                self.match(BKOOLParser.LB)
                self.state = 144
                self.paralist()
                self.state = 145
                self.match(BKOOLParser.RB)
                self.state = 146
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(BKOOLParser.ID)
                self.state = 149
                self.paralist()
                self.state = 150
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
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.para_decl()
                self.state = 155
                self.match(BKOOLParser.SEMI)
                self.state = 156
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
            self.state = 161
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
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.not_void_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.arr_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
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
            self.state = 168
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
            self.state = 170
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
            self.state = 172
            self.not_void_type()
            self.state = 173
            self.match(BKOOLParser.LSB)
            self.state = 174
            self.match(BKOOLParser.INT_LIT)
            self.state = 175
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
            self.state = 177
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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.expr1()
                self.state = 180
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
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
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.expr2(0)
                self.state = 187
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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
            self.state = 194
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 198
                    self.expr3(0) 
                self.state = 203
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
            self.state = 205
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self.expr4(0) 
                self.state = 214
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
            self.state = 216
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INTEGER_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 220
                    self.expr5(0) 
                self.state = 225
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
            self.state = 227
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 229
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 230
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 231
                    self.expr6() 
                self.state = 236
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
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(BKOOLParser.NOT)
                self.state = 238
                self.expr6()
                pass
            elif token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
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
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.expr7()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.expr9(0)
                self.state = 248
                self.match(BKOOLParser.LSB)
                self.state = 249
                self.expr()
                self.state = 250
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
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
            self.state = 256
            self.match(BKOOLParser.ID)
            self.state = 257
            self.match(BKOOLParser.DOT)
            self.state = 258
            self.match(BKOOLParser.ID)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 259
                self.match(BKOOLParser.LB)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 260
                    self.exprlist()


                self.state = 263
                self.match(BKOOLParser.RB)


            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    self.match(BKOOLParser.DOT)
                    self.state = 268
                    self.match(BKOOLParser.ID)
                    self.state = 274
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        self.state = 269
                        self.match(BKOOLParser.LB)
                        self.state = 271
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 270
                            self.exprlist()


                        self.state = 273
                        self.match(BKOOLParser.RB)

             
                self.state = 280
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
            self.state = 281
            self.match(BKOOLParser.NEW)
            self.state = 282
            self.match(BKOOLParser.ID)
            self.state = 283
            self.match(BKOOLParser.LB)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 284
                self.exprlist()


            self.state = 287
            self.match(BKOOLParser.RB)
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 288
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
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(BKOOLParser.LB)
                self.state = 292
                self.expr()
                self.state = 293
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 298
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
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.expr()
                self.state = 302
                self.match(BKOOLParser.COMMA)
                self.state = 303
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.expr()
                self.state = 306
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.block_stmt()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.assignment_decl()
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
            self.state = 314
            self.match(BKOOLParser.LP)
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 315
                self.mem_stmt()


            self.state = 318
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
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BKOOLParser.FINAL:
                        self.state = 320
                        self.match(BKOOLParser.FINAL)


                    self.state = 323
                    self.var_decl() 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.LP or _la==BKOOLParser.ID:
                self.state = 329
                self.stmt()
                self.state = 334
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
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 335
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 336
                self.expr8()
                pass


            self.state = 339
            self.match(BKOOLParser.ASSIGN)
            self.state = 340
            self.expr()
            self.state = 341
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
        self.enterRule(localctx, 68, self.RULE_literal)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(BKOOLParser.BOOL_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 346
                self.match(BKOOLParser.STR_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 347
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
        self.enterRule(localctx, 70, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(BKOOLParser.LP)
            self.state = 351
            self.arr_decl()
            self.state = 352
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
        self.enterRule(localctx, 72, self.RULE_arr_decl)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.arr_val()
                self.state = 355
                self.match(BKOOLParser.COMMA)
                self.state = 356
                self.arr_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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
        self.enterRule(localctx, 74, self.RULE_arr_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
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
         




