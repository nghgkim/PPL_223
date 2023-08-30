// Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2

from lexererr import *

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKOOLLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMENT=1, BLOCK_CMT=2, LINE_CMT=3, BOOLEAN=4, INT=5, FLOAT=6, STRING=7, 
		VOID=8, IF=9, THEN=10, ELSE=11, FOR=12, TO=13, DOWNTO=14, DO=15, BREAK=16, 
		CONTINUE=17, CLASS=18, EXTENDS=19, THIS=20, FINAL=21, STATIC=22, NIL=23, 
		NEW=24, RETURN=25, ADD=26, SUB=27, MUL=28, FLOAT_DIV=29, INT_DIV=30, MOD=31, 
		NE=32, EQUAL=33, LT=34, GT=35, LTE=36, GTE=37, OR=38, AND=39, NOT=40, 
		CONCATENATION=41, ASSIGN=42, INIT=43, LSB=44, RSB=45, LCB=46, RCB=47, 
		LP=48, RP=49, SEMI=50, COLON=51, DOT=52, COMMA=53, INTLIT=54, FLOATLIT=55, 
		BOOLLIT=56, STRINGLIT=57, UNCLOSE_STRING=58, ILLEGAL_ESCAPE=59, ID=60, 
		WS=61, ERROR_CHAR=62;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"COMMENT", "BLOCK_CMT", "LINE_CMT", "BOOLEAN", "INT", "FLOAT", "STRING", 
			"VOID", "IF", "THEN", "ELSE", "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", 
			"CLASS", "EXTENDS", "THIS", "FINAL", "STATIC", "TRUE", "FALSE", "NIL", 
			"NEW", "RETURN", "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", 
			"NE", "EQUAL", "LT", "GT", "LTE", "GTE", "OR", "AND", "NOT", "CONCATENATION", 
			"ASSIGN", "INIT", "LSB", "RSB", "LCB", "RCB", "LP", "RP", "SEMI", "COLON", 
			"DOT", "COMMA", "INTLIT", "FLOATLIT", "DIGIT", "DigitSequence", "Exponent", 
			"SIGN", "DecimalPart", "ExponentPart", "BOOLLIT", "STRINGLIT", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "CHAR", "ESCAPE_SEQUENCE", "ESC_ILLEGAL", "ID", "WS", 
			"ERROR_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'boolean'", "'int'", "'float'", "'string'", 
			"'void'", "'if'", "'then'", "'else'", "'for'", "'to'", "'downto'", "'do'", 
			"'break'", "'continue'", "'class'", "'extends'", "'this'", "'final'", 
			"'static'", "'nil'", "'new'", "'return'", "'+'", "'-'", "'*'", "'/'", 
			"'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", 
			"'&&'", "'!'", "'^'", "':='", "'='", "'['", "']'", "'{'", "'}'", "'('", 
			"')'", "';'", "':'", "'.'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMENT", "BLOCK_CMT", "LINE_CMT", "BOOLEAN", "INT", "FLOAT", 
			"STRING", "VOID", "IF", "THEN", "ELSE", "FOR", "TO", "DOWNTO", "DO", 
			"BREAK", "CONTINUE", "CLASS", "EXTENDS", "THIS", "FINAL", "STATIC", "NIL", 
			"NEW", "RETURN", "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", 
			"NE", "EQUAL", "LT", "GT", "LTE", "GTE", "OR", "AND", "NOT", "CONCATENATION", 
			"ASSIGN", "INIT", "LSB", "RSB", "LCB", "RCB", "LP", "RP", "SEMI", "COLON", 
			"DOT", "COMMA", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "ID", "WS", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public BKOOLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKOOL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 65:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 66:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 72:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:

			    raise UncloseString(self.text[:])

			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:

			    raise IllegalEscape(self.text[:])

			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			raise ErrorToken(self.text)
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@\u01e2\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\3\2\3\2\5\2\u0098\n\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00a0\n\3"+
		"\f\3\16\3\u00a3\13\3\3\3\3\3\3\3\5\3\u00a8\n\3\3\4\3\4\7\4\u00ac\n\4\f"+
		"\4\16\4\u00af\13\4\3\4\5\4\u00b2\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f"+
		"\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34"+
		"\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!"+
		"\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3"+
		")\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3"+
		"\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3"+
		":\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0184\n:\3;\3;\3<\6<\u0189\n<\r<\16<\u018a"+
		"\3=\3=\3>\3>\3?\3?\5?\u0193\n?\3@\3@\3@\3@\3A\3A\5A\u019b\nA\3B\3B\7B"+
		"\u019f\nB\fB\16B\u01a2\13B\3B\3B\3C\3C\7C\u01a8\nC\fC\16C\u01ab\13C\3"+
		"C\3C\3D\3D\7D\u01b1\nD\fD\16D\u01b4\13D\3D\3D\3D\3E\3E\5E\u01bb\nE\3F"+
		"\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u01cb\nF\3G\3G\3G\5G\u01d0"+
		"\nG\3H\3H\7H\u01d4\nH\fH\16H\u01d7\13H\3I\6I\u01da\nI\rI\16I\u01db\3I"+
		"\3I\3J\3J\3J\3\u00a1\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f"+
		"\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\2\61\2\63"+
		"\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60"+
		"c\61e\62g\63i\64k\65m\66o\67q8s9u\2w\2y\2{\2}\2\177\2\u0081:\u0083;\u0085"+
		"<\u0087=\u0089\2\u008b\2\u008d\2\u008f>\u0091?\u0093@\3\2\13\3\2\f\f\3"+
		"\2\62;\4\2GGgg\4\2--//\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\5\2C\\aac|"+
		"\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u01ed\2\3\3\2\2\2\2\5\3\2\2\2\2\7"+
		"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2"+
		"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2"+
		"\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2"+
		"\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2"+
		"\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2"+
		"E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3"+
		"\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2"+
		"\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2"+
		"k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2\u0081\3\2\2\2"+
		"\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008f\3\2\2\2\2\u0091"+
		"\3\2\2\2\2\u0093\3\2\2\2\3\u0097\3\2\2\2\5\u009b\3\2\2\2\7\u00a9\3\2\2"+
		"\2\t\u00b3\3\2\2\2\13\u00bb\3\2\2\2\r\u00bf\3\2\2\2\17\u00c5\3\2\2\2\21"+
		"\u00cc\3\2\2\2\23\u00d1\3\2\2\2\25\u00d4\3\2\2\2\27\u00d9\3\2\2\2\31\u00de"+
		"\3\2\2\2\33\u00e2\3\2\2\2\35\u00e5\3\2\2\2\37\u00ec\3\2\2\2!\u00ef\3\2"+
		"\2\2#\u00f5\3\2\2\2%\u00fe\3\2\2\2\'\u0104\3\2\2\2)\u010c\3\2\2\2+\u0111"+
		"\3\2\2\2-\u0117\3\2\2\2/\u011e\3\2\2\2\61\u0123\3\2\2\2\63\u0129\3\2\2"+
		"\2\65\u012d\3\2\2\2\67\u0131\3\2\2\29\u0138\3\2\2\2;\u013a\3\2\2\2=\u013c"+
		"\3\2\2\2?\u013e\3\2\2\2A\u0140\3\2\2\2C\u0142\3\2\2\2E\u0144\3\2\2\2G"+
		"\u0147\3\2\2\2I\u014a\3\2\2\2K\u014c\3\2\2\2M\u014e\3\2\2\2O\u0151\3\2"+
		"\2\2Q\u0154\3\2\2\2S\u0157\3\2\2\2U\u015a\3\2\2\2W\u015c\3\2\2\2Y\u015e"+
		"\3\2\2\2[\u0161\3\2\2\2]\u0163\3\2\2\2_\u0165\3\2\2\2a\u0167\3\2\2\2c"+
		"\u0169\3\2\2\2e\u016b\3\2\2\2g\u016d\3\2\2\2i\u016f\3\2\2\2k\u0171\3\2"+
		"\2\2m\u0173\3\2\2\2o\u0175\3\2\2\2q\u0177\3\2\2\2s\u0183\3\2\2\2u\u0185"+
		"\3\2\2\2w\u0188\3\2\2\2y\u018c\3\2\2\2{\u018e\3\2\2\2}\u0190\3\2\2\2\177"+
		"\u0194\3\2\2\2\u0081\u019a\3\2\2\2\u0083\u019c\3\2\2\2\u0085\u01a5\3\2"+
		"\2\2\u0087\u01ae\3\2\2\2\u0089\u01ba\3\2\2\2\u008b\u01ca\3\2\2\2\u008d"+
		"\u01cf\3\2\2\2\u008f\u01d1\3\2\2\2\u0091\u01d9\3\2\2\2\u0093\u01df\3\2"+
		"\2\2\u0095\u0098\5\5\3\2\u0096\u0098\5\7\4\2\u0097\u0095\3\2\2\2\u0097"+
		"\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b\2\2\2\u009a\4\3\2\2\2"+
		"\u009b\u009c\7\61\2\2\u009c\u009d\7,\2\2\u009d\u00a1\3\2\2\2\u009e\u00a0"+
		"\13\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u00a2\3\2\2\2"+
		"\u00a1\u009f\3\2\2\2\u00a2\u00a7\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5"+
		"\7,\2\2\u00a5\u00a8\7\61\2\2\u00a6\u00a8\7\2\2\3\u00a7\u00a4\3\2\2\2\u00a7"+
		"\u00a6\3\2\2\2\u00a8\6\3\2\2\2\u00a9\u00ad\7%\2\2\u00aa\u00ac\n\2\2\2"+
		"\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae"+
		"\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b2\7\2\2\3\u00b1"+
		"\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\b\3\2\2\2\u00b3\u00b4\7d\2\2"+
		"\u00b4\u00b5\7q\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8"+
		"\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7p\2\2\u00ba\n\3\2\2\2\u00bb\u00bc"+
		"\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\f\3\2\2\2\u00bf\u00c0"+
		"\7h\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7c\2\2\u00c3"+
		"\u00c4\7v\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7"+
		"\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7i\2\2"+
		"\u00cb\20\3\2\2\2\u00cc\u00cd\7x\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7"+
		"k\2\2\u00cf\u00d0\7f\2\2\u00d0\22\3\2\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3"+
		"\7h\2\2\u00d3\24\3\2\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7j\2\2\u00d6\u00d7"+
		"\7g\2\2\u00d7\u00d8\7p\2\2\u00d8\26\3\2\2\2\u00d9\u00da\7g\2\2\u00da\u00db"+
		"\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7g\2\2\u00dd\30\3\2\2\2\u00de\u00df"+
		"\7h\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7t\2\2\u00e1\32\3\2\2\2\u00e2\u00e3"+
		"\7v\2\2\u00e3\u00e4\7q\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7"+
		"\7q\2\2\u00e7\u00e8\7y\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea"+
		"\u00eb\7q\2\2\u00eb\36\3\2\2\2\u00ec\u00ed\7f\2\2\u00ed\u00ee\7q\2\2\u00ee"+
		" \3\2\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7g\2\2\u00f2"+
		"\u00f3\7c\2\2\u00f3\u00f4\7m\2\2\u00f4\"\3\2\2\2\u00f5\u00f6\7e\2\2\u00f6"+
		"\u00f7\7q\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7k\2\2"+
		"\u00fa\u00fb\7p\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7g\2\2\u00fd$\3\2\2"+
		"\2\u00fe\u00ff\7e\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7c\2\2\u0101\u0102"+
		"\7u\2\2\u0102\u0103\7u\2\2\u0103&\3\2\2\2\u0104\u0105\7g\2\2\u0105\u0106"+
		"\7z\2\2\u0106\u0107\7v\2\2\u0107\u0108\7g\2\2\u0108\u0109\7p\2\2\u0109"+
		"\u010a\7f\2\2\u010a\u010b\7u\2\2\u010b(\3\2\2\2\u010c\u010d\7v\2\2\u010d"+
		"\u010e\7j\2\2\u010e\u010f\7k\2\2\u010f\u0110\7u\2\2\u0110*\3\2\2\2\u0111"+
		"\u0112\7h\2\2\u0112\u0113\7k\2\2\u0113\u0114\7p\2\2\u0114\u0115\7c\2\2"+
		"\u0115\u0116\7n\2\2\u0116,\3\2\2\2\u0117\u0118\7u\2\2\u0118\u0119\7v\2"+
		"\2\u0119\u011a\7c\2\2\u011a\u011b\7v\2\2\u011b\u011c\7k\2\2\u011c\u011d"+
		"\7e\2\2\u011d.\3\2\2\2\u011e\u011f\7v\2\2\u011f\u0120\7t\2\2\u0120\u0121"+
		"\7w\2\2\u0121\u0122\7g\2\2\u0122\60\3\2\2\2\u0123\u0124\7h\2\2\u0124\u0125"+
		"\7c\2\2\u0125\u0126\7n\2\2\u0126\u0127\7u\2\2\u0127\u0128\7g\2\2\u0128"+
		"\62\3\2\2\2\u0129\u012a\7p\2\2\u012a\u012b\7k\2\2\u012b\u012c\7n\2\2\u012c"+
		"\64\3\2\2\2\u012d\u012e\7p\2\2\u012e\u012f\7g\2\2\u012f\u0130\7y\2\2\u0130"+
		"\66\3\2\2\2\u0131\u0132\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7v\2\2\u0134"+
		"\u0135\7w\2\2\u0135\u0136\7t\2\2\u0136\u0137\7p\2\2\u01378\3\2\2\2\u0138"+
		"\u0139\7-\2\2\u0139:\3\2\2\2\u013a\u013b\7/\2\2\u013b<\3\2\2\2\u013c\u013d"+
		"\7,\2\2\u013d>\3\2\2\2\u013e\u013f\7\61\2\2\u013f@\3\2\2\2\u0140\u0141"+
		"\7^\2\2\u0141B\3\2\2\2\u0142\u0143\7\'\2\2\u0143D\3\2\2\2\u0144\u0145"+
		"\7#\2\2\u0145\u0146\7?\2\2\u0146F\3\2\2\2\u0147\u0148\7?\2\2\u0148\u0149"+
		"\7?\2\2\u0149H\3\2\2\2\u014a\u014b\7>\2\2\u014bJ\3\2\2\2\u014c\u014d\7"+
		"@\2\2\u014dL\3\2\2\2\u014e\u014f\7>\2\2\u014f\u0150\7?\2\2\u0150N\3\2"+
		"\2\2\u0151\u0152\7@\2\2\u0152\u0153\7?\2\2\u0153P\3\2\2\2\u0154\u0155"+
		"\7~\2\2\u0155\u0156\7~\2\2\u0156R\3\2\2\2\u0157\u0158\7(\2\2\u0158\u0159"+
		"\7(\2\2\u0159T\3\2\2\2\u015a\u015b\7#\2\2\u015bV\3\2\2\2\u015c\u015d\7"+
		"`\2\2\u015dX\3\2\2\2\u015e\u015f\7<\2\2\u015f\u0160\7?\2\2\u0160Z\3\2"+
		"\2\2\u0161\u0162\7?\2\2\u0162\\\3\2\2\2\u0163\u0164\7]\2\2\u0164^\3\2"+
		"\2\2\u0165\u0166\7_\2\2\u0166`\3\2\2\2\u0167\u0168\7}\2\2\u0168b\3\2\2"+
		"\2\u0169\u016a\7\177\2\2\u016ad\3\2\2\2\u016b\u016c\7*\2\2\u016cf\3\2"+
		"\2\2\u016d\u016e\7+\2\2\u016eh\3\2\2\2\u016f\u0170\7=\2\2\u0170j\3\2\2"+
		"\2\u0171\u0172\7<\2\2\u0172l\3\2\2\2\u0173\u0174\7\60\2\2\u0174n\3\2\2"+
		"\2\u0175\u0176\7.\2\2\u0176p\3\2\2\2\u0177\u0178\5w<\2\u0178r\3\2\2\2"+
		"\u0179\u017a\5w<\2\u017a\u017b\5}?\2\u017b\u017c\5\177@\2\u017c\u0184"+
		"\3\2\2\2\u017d\u017e\5w<\2\u017e\u017f\5}?\2\u017f\u0184\3\2\2\2\u0180"+
		"\u0181\5w<\2\u0181\u0182\5\177@\2\u0182\u0184\3\2\2\2\u0183\u0179\3\2"+
		"\2\2\u0183\u017d\3\2\2\2\u0183\u0180\3\2\2\2\u0184t\3\2\2\2\u0185\u0186"+
		"\t\3\2\2\u0186v\3\2\2\2\u0187\u0189\5u;\2\u0188\u0187\3\2\2\2\u0189\u018a"+
		"\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018bx\3\2\2\2\u018c"+
		"\u018d\t\4\2\2\u018dz\3\2\2\2\u018e\u018f\t\5\2\2\u018f|\3\2\2\2\u0190"+
		"\u0192\5m\67\2\u0191\u0193\5w<\2\u0192\u0191\3\2\2\2\u0192\u0193\3\2\2"+
		"\2\u0193~\3\2\2\2\u0194\u0195\5y=\2\u0195\u0196\5{>\2\u0196\u0197\5w<"+
		"\2\u0197\u0080\3\2\2\2\u0198\u019b\5/\30\2\u0199\u019b\5\61\31\2\u019a"+
		"\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019b\u0082\3\2\2\2\u019c\u01a0\7$"+
		"\2\2\u019d\u019f\5\u0089E\2\u019e\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0"+
		"\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2\u01a0\3\2"+
		"\2\2\u01a3\u01a4\7$\2\2\u01a4\u0084\3\2\2\2\u01a5\u01a9\7$\2\2\u01a6\u01a8"+
		"\5\u0089E\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2"+
		"\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad"+
		"\bC\3\2\u01ad\u0086\3\2\2\2\u01ae\u01b2\7$\2\2\u01af\u01b1\5\u0089E\2"+
		"\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3"+
		"\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\5\u008dG"+
		"\2\u01b6\u01b7\bD\4\2\u01b7\u0088\3\2\2\2\u01b8\u01bb\n\6\2\2\u01b9\u01bb"+
		"\5\u008bF\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u008a\3\2\2"+
		"\2\u01bc\u01bd\7^\2\2\u01bd\u01cb\7d\2\2\u01be\u01bf\7^\2\2\u01bf\u01cb"+
		"\7h\2\2\u01c0\u01c1\7^\2\2\u01c1\u01cb\7t\2\2\u01c2\u01c3\7^\2\2\u01c3"+
		"\u01cb\7p\2\2\u01c4\u01c5\7^\2\2\u01c5\u01cb\7v\2\2\u01c6\u01c7\7^\2\2"+
		"\u01c7\u01cb\7$\2\2\u01c8\u01c9\7^\2\2\u01c9\u01cb\7^\2\2\u01ca\u01bc"+
		"\3\2\2\2\u01ca\u01be\3\2\2\2\u01ca\u01c0\3\2\2\2\u01ca\u01c2\3\2\2\2\u01ca"+
		"\u01c4\3\2\2\2\u01ca\u01c6\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u008c\3\2"+
		"\2\2\u01cc\u01cd\7^\2\2\u01cd\u01d0\n\7\2\2\u01ce\u01d0\7^\2\2\u01cf\u01cc"+
		"\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0\u008e\3\2\2\2\u01d1\u01d5\t\b\2\2\u01d2"+
		"\u01d4\t\t\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2"+
		"\2\2\u01d5\u01d6\3\2\2\2\u01d6\u0090\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8"+
		"\u01da\t\n\2\2\u01d9\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01d9\3\2"+
		"\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\bI\2\2\u01de"+
		"\u0092\3\2\2\2\u01df\u01e0\13\2\2\2\u01e0\u01e1\bJ\5\2\u01e1\u0094\3\2"+
		"\2\2\24\2\u0097\u00a1\u00a7\u00ad\u00b1\u0183\u018a\u0192\u019a\u01a0"+
		"\u01a9\u01b2\u01ba\u01ca\u01cf\u01d5\u01db\6\b\2\2\3C\2\3D\3\3J\4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}