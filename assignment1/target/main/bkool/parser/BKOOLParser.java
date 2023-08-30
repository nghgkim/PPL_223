// Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKOOLParser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_class_decl = 1, RULE_class_mem = 2, RULE_class_mem_list = 3, 
		RULE_class_mem_decl = 4, RULE_attr_decl = 5, RULE_const_attr_decl = 6, 
		RULE_static_attr_decl = 7, RULE_static_const_attr_decl = 8, RULE_attr_decl_list = 9, 
		RULE_attr_decl_unit = 10, RULE_method_decl = 11, RULE_param_list = 12, 
		RULE_param_decl = 13, RULE_param = 14, RULE_idlist = 15, RULE_constructor_decl = 16, 
		RULE_class_type = 17, RULE_decl_type = 18, RULE_primitive_type = 19, RULE_array_type = 20, 
		RULE_stmt = 21, RULE_block_stmt = 22, RULE_local_var_decls = 23, RULE_local_var_decl = 24, 
		RULE_var_decl = 25, RULE_const_decl = 26, RULE_decl_list = 27, RULE_decl_unit = 28, 
		RULE_stmts = 29, RULE_assign_stmt = 30, RULE_lhs = 31, RULE_lhs_unit = 32, 
		RULE_lhs_member_access_expr = 33, RULE_lhs_index_expr = 34, RULE_if_stmt = 35, 
		RULE_if_then_else_stmt = 36, RULE_if_then_stmt = 37, RULE_for_stmt = 38, 
		RULE_break_stmt = 39, RULE_continue_stmt = 40, RULE_return_stmt = 41, 
		RULE_method_invocation_stmt = 42, RULE_expr = 43, RULE_expr1 = 44, RULE_expr2 = 45, 
		RULE_expr3 = 46, RULE_expr4 = 47, RULE_expr5 = 48, RULE_expr6 = 49, RULE_expr7 = 50, 
		RULE_expr8 = 51, RULE_expr9 = 52, RULE_expr10 = 53, RULE_expr11 = 54, 
		RULE_expr12 = 55, RULE_method_call = 56, RULE_expr_list = 57, RULE_literal = 58, 
		RULE_arrlit = 59, RULE_literal_list = 60;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class_decl", "class_mem", "class_mem_list", "class_mem_decl", 
			"attr_decl", "const_attr_decl", "static_attr_decl", "static_const_attr_decl", 
			"attr_decl_list", "attr_decl_unit", "method_decl", "param_list", "param_decl", 
			"param", "idlist", "constructor_decl", "class_type", "decl_type", "primitive_type", 
			"array_type", "stmt", "block_stmt", "local_var_decls", "local_var_decl", 
			"var_decl", "const_decl", "decl_list", "decl_unit", "stmts", "assign_stmt", 
			"lhs", "lhs_unit", "lhs_member_access_expr", "lhs_index_expr", "if_stmt", 
			"if_then_else_stmt", "if_then_stmt", "for_stmt", "break_stmt", "continue_stmt", 
			"return_stmt", "method_invocation_stmt", "expr", "expr1", "expr2", "expr3", 
			"expr4", "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
			"expr12", "method_call", "expr_list", "literal", "arrlit", "literal_list"
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

	@Override
	public String getGrammarFileName() { return "BKOOL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKOOLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BKOOLParser.EOF, 0); }
		public List<Class_declContext> class_decl() {
			return getRuleContexts(Class_declContext.class);
		}
		public Class_declContext class_decl(int i) {
			return getRuleContext(Class_declContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(122);
				class_decl();
				}
				}
				setState(125); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			setState(127);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_declContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(BKOOLParser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(BKOOLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BKOOLParser.ID, i);
		}
		public Class_memContext class_mem() {
			return getRuleContext(Class_memContext.class,0);
		}
		public TerminalNode EXTENDS() { return getToken(BKOOLParser.EXTENDS, 0); }
		public Class_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitClass_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Class_declContext class_decl() throws RecognitionException {
		Class_declContext _localctx = new Class_declContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(CLASS);
			setState(130);
			match(ID);
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EXTENDS) {
				{
				setState(131);
				match(EXTENDS);
				setState(132);
				match(ID);
				}
			}

			setState(135);
			class_mem();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_memContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(BKOOLParser.LCB, 0); }
		public Class_mem_listContext class_mem_list() {
			return getRuleContext(Class_mem_listContext.class,0);
		}
		public TerminalNode RCB() { return getToken(BKOOLParser.RCB, 0); }
		public Class_memContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_mem; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitClass_mem(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Class_memContext class_mem() throws RecognitionException {
		Class_memContext _localctx = new Class_memContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_class_mem);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(LCB);
			setState(138);
			class_mem_list();
			setState(139);
			match(RCB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_mem_listContext extends ParserRuleContext {
		public Class_mem_declContext class_mem_decl() {
			return getRuleContext(Class_mem_declContext.class,0);
		}
		public Class_mem_listContext class_mem_list() {
			return getRuleContext(Class_mem_listContext.class,0);
		}
		public Class_mem_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_mem_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitClass_mem_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Class_mem_listContext class_mem_list() throws RecognitionException {
		Class_mem_listContext _localctx = new Class_mem_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_class_mem_list);
		try {
			setState(145);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case INT:
			case FLOAT:
			case STRING:
			case VOID:
			case FINAL:
			case STATIC:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(141);
				class_mem_decl();
				setState(142);
				class_mem_list();
				}
				}
				break;
			case RCB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_mem_declContext extends ParserRuleContext {
		public Method_declContext method_decl() {
			return getRuleContext(Method_declContext.class,0);
		}
		public Const_attr_declContext const_attr_decl() {
			return getRuleContext(Const_attr_declContext.class,0);
		}
		public Static_attr_declContext static_attr_decl() {
			return getRuleContext(Static_attr_declContext.class,0);
		}
		public Static_const_attr_declContext static_const_attr_decl() {
			return getRuleContext(Static_const_attr_declContext.class,0);
		}
		public Attr_declContext attr_decl() {
			return getRuleContext(Attr_declContext.class,0);
		}
		public Constructor_declContext constructor_decl() {
			return getRuleContext(Constructor_declContext.class,0);
		}
		public Class_mem_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_mem_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitClass_mem_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Class_mem_declContext class_mem_decl() throws RecognitionException {
		Class_mem_declContext _localctx = new Class_mem_declContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_class_mem_decl);
		try {
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				method_decl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				const_attr_decl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(149);
				static_attr_decl();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(150);
				static_const_attr_decl();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(151);
				attr_decl();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(152);
				constructor_decl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attr_declContext extends ParserRuleContext {
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public Attr_decl_listContext attr_decl_list() {
			return getRuleContext(Attr_decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Attr_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitAttr_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Attr_declContext attr_decl() throws RecognitionException {
		Attr_declContext _localctx = new Attr_declContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attr_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			decl_type();
			setState(156);
			attr_decl_list();
			setState(157);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Const_attr_declContext extends ParserRuleContext {
		public TerminalNode FINAL() { return getToken(BKOOLParser.FINAL, 0); }
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public Attr_decl_listContext attr_decl_list() {
			return getRuleContext(Attr_decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Const_attr_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_const_attr_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitConst_attr_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Const_attr_declContext const_attr_decl() throws RecognitionException {
		Const_attr_declContext _localctx = new Const_attr_declContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_const_attr_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			match(FINAL);
			setState(160);
			decl_type();
			setState(161);
			attr_decl_list();
			setState(162);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Static_attr_declContext extends ParserRuleContext {
		public TerminalNode STATIC() { return getToken(BKOOLParser.STATIC, 0); }
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public Attr_decl_listContext attr_decl_list() {
			return getRuleContext(Attr_decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Static_attr_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_static_attr_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitStatic_attr_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Static_attr_declContext static_attr_decl() throws RecognitionException {
		Static_attr_declContext _localctx = new Static_attr_declContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_static_attr_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(STATIC);
			setState(165);
			decl_type();
			setState(166);
			attr_decl_list();
			setState(167);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Static_const_attr_declContext extends ParserRuleContext {
		public TerminalNode FINAL() { return getToken(BKOOLParser.FINAL, 0); }
		public TerminalNode STATIC() { return getToken(BKOOLParser.STATIC, 0); }
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public Attr_decl_listContext attr_decl_list() {
			return getRuleContext(Attr_decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Static_const_attr_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_static_const_attr_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitStatic_const_attr_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Static_const_attr_declContext static_const_attr_decl() throws RecognitionException {
		Static_const_attr_declContext _localctx = new Static_const_attr_declContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_static_const_attr_decl);
		try {
			setState(181);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FINAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(169);
				match(FINAL);
				setState(170);
				match(STATIC);
				setState(171);
				decl_type();
				setState(172);
				attr_decl_list();
				setState(173);
				match(SEMI);
				}
				break;
			case STATIC:
				enterOuterAlt(_localctx, 2);
				{
				setState(175);
				match(STATIC);
				setState(176);
				match(FINAL);
				setState(177);
				decl_type();
				setState(178);
				attr_decl_list();
				setState(179);
				match(SEMI);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attr_decl_listContext extends ParserRuleContext {
		public Attr_decl_unitContext attr_decl_unit() {
			return getRuleContext(Attr_decl_unitContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Attr_decl_listContext attr_decl_list() {
			return getRuleContext(Attr_decl_listContext.class,0);
		}
		public Attr_decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr_decl_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitAttr_decl_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Attr_decl_listContext attr_decl_list() throws RecognitionException {
		Attr_decl_listContext _localctx = new Attr_decl_listContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_attr_decl_list);
		try {
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				attr_decl_unit();
				setState(184);
				match(COMMA);
				setState(185);
				attr_decl_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				attr_decl_unit();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attr_decl_unitContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode INIT() { return getToken(BKOOLParser.INIT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Attr_decl_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr_decl_unit; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitAttr_decl_unit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Attr_decl_unitContext attr_decl_unit() throws RecognitionException {
		Attr_decl_unitContext _localctx = new Attr_decl_unitContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_attr_decl_unit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			match(ID);
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INIT) {
				{
				setState(191);
				match(INIT);
				setState(192);
				expr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declContext extends ParserRuleContext {
		public Class_typeContext class_type() {
			return getRuleContext(Class_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public TerminalNode STATIC() { return getToken(BKOOLParser.STATIC, 0); }
		public Method_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitMethod_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Method_declContext method_decl() throws RecognitionException {
		Method_declContext _localctx = new Method_declContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_method_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STATIC) {
				{
				setState(195);
				match(STATIC);
				}
			}

			setState(198);
			class_type();
			setState(199);
			match(ID);
			setState(200);
			match(LP);
			setState(201);
			param_list();
			setState(202);
			match(RP);
			setState(203);
			block_stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_listContext extends ParserRuleContext {
		public Param_declContext param_decl() {
			return getRuleContext(Param_declContext.class,0);
		}
		public Param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitParam_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Param_listContext param_list() throws RecognitionException {
		Param_listContext _localctx = new Param_listContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_param_list);
		try {
			setState(207);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case INT:
			case FLOAT:
			case STRING:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				param_decl();
				}
				break;
			case RP:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_declContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Param_declContext param_decl() {
			return getRuleContext(Param_declContext.class,0);
		}
		public Param_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitParam_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Param_declContext param_decl() throws RecognitionException {
		Param_declContext _localctx = new Param_declContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_param_decl);
		try {
			setState(214);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				param();
				setState(210);
				match(SEMI);
				setState(211);
				param_decl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(213);
				param();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitParam(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			decl_type();
			setState(217);
			idlist();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdlistContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public IdlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idlist; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitIdlist(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdlistContext idlist() throws RecognitionException {
		IdlistContext _localctx = new IdlistContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_idlist);
		try {
			setState(223);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(219);
				match(ID);
				setState(220);
				match(COMMA);
				setState(221);
				idlist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(222);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Constructor_declContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public Constructor_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructor_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitConstructor_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Constructor_declContext constructor_decl() throws RecognitionException {
		Constructor_declContext _localctx = new Constructor_declContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_constructor_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(ID);
			setState(226);
			match(LP);
			setState(227);
			param_list();
			setState(228);
			match(RP);
			setState(229);
			block_stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_typeContext extends ParserRuleContext {
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public TerminalNode VOID() { return getToken(BKOOLParser.VOID, 0); }
		public Class_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_type; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitClass_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Class_typeContext class_type() throws RecognitionException {
		Class_typeContext _localctx = new Class_typeContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_class_type);
		try {
			setState(233);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case INT:
			case FLOAT:
			case STRING:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(231);
				decl_type();
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(232);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Decl_typeContext extends ParserRuleContext {
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public Decl_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl_type; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitDecl_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Decl_typeContext decl_type() throws RecognitionException {
		Decl_typeContext _localctx = new Decl_typeContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_decl_type);
		try {
			setState(238);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(235);
				primitive_type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				array_type();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(237);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primitive_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BKOOLParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(BKOOLParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(BKOOLParser.STRING, 0); }
		public TerminalNode BOOLEAN() { return getToken(BKOOLParser.BOOLEAN, 0); }
		public Primitive_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_type; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitPrimitive_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Primitive_typeContext primitive_type() throws RecognitionException {
		Primitive_typeContext _localctx = new Primitive_typeContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOLEAN) | (1L << INT) | (1L << FLOAT) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_typeContext extends ParserRuleContext {
		public TerminalNode LSB() { return getToken(BKOOLParser.LSB, 0); }
		public TerminalNode INTLIT() { return getToken(BKOOLParser.INTLIT, 0); }
		public TerminalNode RSB() { return getToken(BKOOLParser.RSB, 0); }
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitArray_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_array_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case INT:
			case FLOAT:
			case STRING:
				{
				setState(242);
				primitive_type();
				}
				break;
			case ID:
				{
				setState(243);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(246);
			match(LSB);
			setState(247);
			match(INTLIT);
			setState(248);
			match(RSB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public Break_stmtContext break_stmt() {
			return getRuleContext(Break_stmtContext.class,0);
		}
		public Continue_stmtContext continue_stmt() {
			return getRuleContext(Continue_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public Method_invocation_stmtContext method_invocation_stmt() {
			return getRuleContext(Method_invocation_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_stmt);
		try {
			setState(258);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(250);
				block_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(251);
				assign_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(252);
				if_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(253);
				for_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(254);
				break_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(255);
				continue_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(256);
				return_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(257);
				method_invocation_stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_stmtContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(BKOOLParser.LCB, 0); }
		public TerminalNode RCB() { return getToken(BKOOLParser.RCB, 0); }
		public Local_var_declsContext local_var_decls() {
			return getRuleContext(Local_var_declsContext.class,0);
		}
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
		}
		public Block_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitBlock_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Block_stmtContext block_stmt() throws RecognitionException {
		Block_stmtContext _localctx = new Block_stmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_block_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(LCB);
			setState(262);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(261);
				local_var_decls();
				}
				break;
			}
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << FOR) | (1L << BREAK) | (1L << CONTINUE) | (1L << THIS) | (1L << NIL) | (1L << NEW) | (1L << RETURN) | (1L << ADD) | (1L << SUB) | (1L << NOT) | (1L << LCB) | (1L << LP) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << BOOLLIT) | (1L << STRINGLIT) | (1L << ID))) != 0)) {
				{
				setState(264);
				stmts();
				}
			}

			setState(267);
			match(RCB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Local_var_declsContext extends ParserRuleContext {
		public Local_var_declContext local_var_decl() {
			return getRuleContext(Local_var_declContext.class,0);
		}
		public Local_var_declsContext local_var_decls() {
			return getRuleContext(Local_var_declsContext.class,0);
		}
		public Local_var_declsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_local_var_decls; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLocal_var_decls(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Local_var_declsContext local_var_decls() throws RecognitionException {
		Local_var_declsContext _localctx = new Local_var_declsContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_local_var_decls);
		try {
			setState(273);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				local_var_decl();
				setState(270);
				local_var_decls();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(272);
				local_var_decl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Local_var_declContext extends ParserRuleContext {
		public Var_declContext var_decl() {
			return getRuleContext(Var_declContext.class,0);
		}
		public Const_declContext const_decl() {
			return getRuleContext(Const_declContext.class,0);
		}
		public Local_var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_local_var_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLocal_var_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Local_var_declContext local_var_decl() throws RecognitionException {
		Local_var_declContext _localctx = new Local_var_declContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_local_var_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLEAN:
			case INT:
			case FLOAT:
			case STRING:
			case ID:
				{
				setState(275);
				var_decl();
				}
				break;
			case FINAL:
				{
				setState(276);
				const_decl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declContext extends ParserRuleContext {
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public Decl_listContext decl_list() {
			return getRuleContext(Decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitVar_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_var_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			decl_type();
			setState(280);
			decl_list();
			setState(281);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Const_declContext extends ParserRuleContext {
		public TerminalNode FINAL() { return getToken(BKOOLParser.FINAL, 0); }
		public Decl_typeContext decl_type() {
			return getRuleContext(Decl_typeContext.class,0);
		}
		public Decl_listContext decl_list() {
			return getRuleContext(Decl_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Const_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_const_decl; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitConst_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Const_declContext const_decl() throws RecognitionException {
		Const_declContext _localctx = new Const_declContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_const_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(FINAL);
			setState(284);
			decl_type();
			setState(285);
			decl_list();
			setState(286);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Decl_listContext extends ParserRuleContext {
		public Decl_unitContext decl_unit() {
			return getRuleContext(Decl_unitContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Decl_listContext decl_list() {
			return getRuleContext(Decl_listContext.class,0);
		}
		public Decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitDecl_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Decl_listContext decl_list() throws RecognitionException {
		Decl_listContext _localctx = new Decl_listContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_decl_list);
		try {
			setState(293);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(288);
				decl_unit();
				setState(289);
				match(COMMA);
				setState(290);
				decl_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(292);
				decl_unit();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Decl_unitContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode INIT() { return getToken(BKOOLParser.INIT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Decl_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl_unit; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitDecl_unit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Decl_unitContext decl_unit() throws RecognitionException {
		Decl_unitContext _localctx = new Decl_unitContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_decl_unit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			match(ID);
			setState(298);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INIT) {
				{
				setState(296);
				match(INIT);
				setState(297);
				expr();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtsContext extends ParserRuleContext {
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
		}
		public StmtsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmts; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitStmts(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StmtsContext stmts() throws RecognitionException {
		StmtsContext _localctx = new StmtsContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_stmts);
		try {
			setState(304);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				stmt();
				setState(301);
				stmts();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(303);
				stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmtContext extends ParserRuleContext {
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKOOLParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitAssign_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			lhs();
			setState(307);
			match(ASSIGN);
			setState(308);
			expr();
			setState(309);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LhsContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public Lhs_unitContext lhs_unit() {
			return getRuleContext(Lhs_unitContext.class,0);
		}
		public LhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLhs(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LhsContext lhs() throws RecognitionException {
		LhsContext _localctx = new LhsContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_lhs);
		try {
			setState(316);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(311);
				match(LP);
				setState(312);
				lhs();
				setState(313);
				match(RP);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(315);
				lhs_unit();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Lhs_unitContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public Lhs_index_exprContext lhs_index_expr() {
			return getRuleContext(Lhs_index_exprContext.class,0);
		}
		public Lhs_member_access_exprContext lhs_member_access_expr() {
			return getRuleContext(Lhs_member_access_exprContext.class,0);
		}
		public Lhs_unitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs_unit; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLhs_unit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Lhs_unitContext lhs_unit() throws RecognitionException {
		Lhs_unitContext _localctx = new Lhs_unitContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_lhs_unit);
		try {
			setState(321);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(318);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(319);
				lhs_index_expr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(320);
				lhs_member_access_expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Lhs_member_access_exprContext extends ParserRuleContext {
		public Token bop;
		public Expr11Context expr11() {
			return getRuleContext(Expr11Context.class,0);
		}
		public TerminalNode DOT() { return getToken(BKOOLParser.DOT, 0); }
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public Lhs_member_access_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs_member_access_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLhs_member_access_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Lhs_member_access_exprContext lhs_member_access_expr() throws RecognitionException {
		Lhs_member_access_exprContext _localctx = new Lhs_member_access_exprContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_lhs_member_access_expr);
		try {
			setState(331);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(323);
				expr11();
				setState(324);
				((Lhs_member_access_exprContext)_localctx).bop = match(DOT);
				{
				setState(325);
				method_call();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(327);
				expr11();
				setState(328);
				((Lhs_member_access_exprContext)_localctx).bop = match(DOT);
				{
				setState(329);
				match(ID);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Lhs_index_exprContext extends ParserRuleContext {
		public Expr10Context expr10() {
			return getRuleContext(Expr10Context.class,0);
		}
		public TerminalNode LSB() { return getToken(BKOOLParser.LSB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RSB() { return getToken(BKOOLParser.RSB, 0); }
		public Lhs_index_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs_index_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLhs_index_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Lhs_index_exprContext lhs_index_expr() throws RecognitionException {
		Lhs_index_exprContext _localctx = new Lhs_index_exprContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_lhs_index_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			expr10(0);
			{
			setState(334);
			match(LSB);
			setState(335);
			expr();
			setState(336);
			match(RSB);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmtContext extends ParserRuleContext {
		public If_then_stmtContext if_then_stmt() {
			return getRuleContext(If_then_stmtContext.class,0);
		}
		public If_then_else_stmtContext if_then_else_stmt() {
			return getRuleContext(If_then_else_stmtContext.class,0);
		}
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitIf_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_if_stmt);
		try {
			setState(340);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(338);
				if_then_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(339);
				if_then_else_stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_then_else_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKOOLParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode THEN() { return getToken(BKOOLParser.THEN, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(BKOOLParser.ELSE, 0); }
		public If_then_else_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_then_else_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitIf_then_else_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final If_then_else_stmtContext if_then_else_stmt() throws RecognitionException {
		If_then_else_stmtContext _localctx = new If_then_else_stmtContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_if_then_else_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(342);
			match(IF);
			setState(343);
			expr();
			setState(344);
			match(THEN);
			setState(345);
			stmt();
			setState(346);
			match(ELSE);
			setState(347);
			stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_then_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKOOLParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode THEN() { return getToken(BKOOLParser.THEN, 0); }
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public If_then_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_then_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitIf_then_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final If_then_stmtContext if_then_stmt() throws RecognitionException {
		If_then_stmtContext _localctx = new If_then_stmtContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_if_then_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			match(IF);
			setState(350);
			expr();
			setState(351);
			match(THEN);
			setState(352);
			stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKOOLParser.FOR, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DO() { return getToken(BKOOLParser.DO, 0); }
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public TerminalNode TO() { return getToken(BKOOLParser.TO, 0); }
		public TerminalNode DOWNTO() { return getToken(BKOOLParser.DOWNTO, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKOOLParser.ASSIGN, 0); }
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitFor_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_for_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			match(FOR);
			{
			setState(355);
			match(ID);
			setState(356);
			match(ASSIGN);
			setState(357);
			expr();
			}
			setState(359);
			_la = _input.LA(1);
			if ( !(_la==TO || _la==DOWNTO) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(360);
			expr();
			setState(361);
			match(DO);
			setState(362);
			stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_stmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(BKOOLParser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Break_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitBreak_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			match(BREAK);
			setState(365);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_stmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BKOOLParser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Continue_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitContinue_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Continue_stmtContext continue_stmt() throws RecognitionException {
		Continue_stmtContext _localctx = new Continue_stmtContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(367);
			match(CONTINUE);
			setState(368);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_stmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKOOLParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitReturn_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_return_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
			match(RETURN);
			setState(371);
			expr();
			setState(372);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_invocation_stmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode DOT() { return getToken(BKOOLParser.DOT, 0); }
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Method_invocation_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_invocation_stmt; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitMethod_invocation_stmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Method_invocation_stmtContext method_invocation_stmt() throws RecognitionException {
		Method_invocation_stmtContext _localctx = new Method_invocation_stmtContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_method_invocation_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			expr();
			setState(375);
			match(DOT);
			setState(376);
			method_call();
			setState(377);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public Expr1Context expr1() {
			return getRuleContext(Expr1Context.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(379);
			expr1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr1Context extends ParserRuleContext {
		public List<Expr2Context> expr2() {
			return getRuleContexts(Expr2Context.class);
		}
		public Expr2Context expr2(int i) {
			return getRuleContext(Expr2Context.class,i);
		}
		public TerminalNode LT() { return getToken(BKOOLParser.LT, 0); }
		public TerminalNode GT() { return getToken(BKOOLParser.GT, 0); }
		public TerminalNode LTE() { return getToken(BKOOLParser.LTE, 0); }
		public TerminalNode GTE() { return getToken(BKOOLParser.GTE, 0); }
		public Expr1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr1; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr1(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr1Context expr1() throws RecognitionException {
		Expr1Context _localctx = new Expr1Context(_ctx, getState());
		enterRule(_localctx, 88, RULE_expr1);
		int _la;
		try {
			setState(386);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(381);
				expr2();
				setState(382);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LT) | (1L << GT) | (1L << LTE) | (1L << GTE))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(383);
				expr2();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(385);
				expr2();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr2Context extends ParserRuleContext {
		public List<Expr3Context> expr3() {
			return getRuleContexts(Expr3Context.class);
		}
		public Expr3Context expr3(int i) {
			return getRuleContext(Expr3Context.class,i);
		}
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public TerminalNode NE() { return getToken(BKOOLParser.NE, 0); }
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr2(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr2Context expr2() throws RecognitionException {
		Expr2Context _localctx = new Expr2Context(_ctx, getState());
		enterRule(_localctx, 90, RULE_expr2);
		int _la;
		try {
			setState(393);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(388);
				expr3(0);
				setState(389);
				_la = _input.LA(1);
				if ( !(_la==NE || _la==EQUAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(390);
				expr3(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(392);
				expr3(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr3Context extends ParserRuleContext {
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public TerminalNode AND() { return getToken(BKOOLParser.AND, 0); }
		public TerminalNode OR() { return getToken(BKOOLParser.OR, 0); }
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr3(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr3Context expr3() throws RecognitionException {
		return expr3(0);
	}

	private Expr3Context expr3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr3Context _localctx = new Expr3Context(_ctx, _parentState);
		Expr3Context _prevctx = _localctx;
		int _startState = 92;
		enterRecursionRule(_localctx, 92, RULE_expr3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(396);
			expr4(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(403);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr3);
					setState(398);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(399);
					_la = _input.LA(1);
					if ( !(_la==OR || _la==AND) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(400);
					expr4(0);
					}
					} 
				}
				setState(405);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr4Context extends ParserRuleContext {
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public TerminalNode ADD() { return getToken(BKOOLParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(BKOOLParser.SUB, 0); }
		public Expr4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr4; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr4(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr4Context expr4() throws RecognitionException {
		return expr4(0);
	}

	private Expr4Context expr4(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr4Context _localctx = new Expr4Context(_ctx, _parentState);
		Expr4Context _prevctx = _localctx;
		int _startState = 94;
		enterRecursionRule(_localctx, 94, RULE_expr4, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(407);
			expr5(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(414);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr4Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr4);
					setState(409);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(410);
					_la = _input.LA(1);
					if ( !(_la==ADD || _la==SUB) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(411);
					expr5(0);
					}
					} 
				}
				setState(416);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr5Context extends ParserRuleContext {
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public TerminalNode MUL() { return getToken(BKOOLParser.MUL, 0); }
		public TerminalNode FLOAT_DIV() { return getToken(BKOOLParser.FLOAT_DIV, 0); }
		public TerminalNode INT_DIV() { return getToken(BKOOLParser.INT_DIV, 0); }
		public TerminalNode MOD() { return getToken(BKOOLParser.MOD, 0); }
		public Expr5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr5; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr5(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr5Context expr5() throws RecognitionException {
		return expr5(0);
	}

	private Expr5Context expr5(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr5Context _localctx = new Expr5Context(_ctx, _parentState);
		Expr5Context _prevctx = _localctx;
		int _startState = 96;
		enterRecursionRule(_localctx, 96, RULE_expr5, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(418);
			expr6(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(425);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr5Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr5);
					setState(420);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(421);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << FLOAT_DIV) | (1L << INT_DIV) | (1L << MOD))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(422);
					expr6(0);
					}
					} 
				}
				setState(427);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr6Context extends ParserRuleContext {
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public TerminalNode CONCATENATION() { return getToken(BKOOLParser.CONCATENATION, 0); }
		public Expr6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr6; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr6(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr6Context expr6() throws RecognitionException {
		return expr6(0);
	}

	private Expr6Context expr6(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr6Context _localctx = new Expr6Context(_ctx, _parentState);
		Expr6Context _prevctx = _localctx;
		int _startState = 98;
		enterRecursionRule(_localctx, 98, RULE_expr6, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(429);
			expr7();
			}
			_ctx.stop = _input.LT(-1);
			setState(436);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr6Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr6);
					setState(431);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(432);
					match(CONCATENATION);
					}
					setState(433);
					expr7();
					}
					} 
				}
				setState(438);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr7Context extends ParserRuleContext {
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public TerminalNode NOT() { return getToken(BKOOLParser.NOT, 0); }
		public Expr8Context expr8() {
			return getRuleContext(Expr8Context.class,0);
		}
		public Expr7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr7; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr7(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr7Context expr7() throws RecognitionException {
		Expr7Context _localctx = new Expr7Context(_ctx, getState());
		enterRule(_localctx, 100, RULE_expr7);
		try {
			setState(442);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(439);
				match(NOT);
				}
				setState(440);
				expr7();
				}
				break;
			case THIS:
			case NIL:
			case NEW:
			case ADD:
			case SUB:
			case LCB:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(441);
				expr8();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr8Context extends ParserRuleContext {
		public Expr8Context expr8() {
			return getRuleContext(Expr8Context.class,0);
		}
		public TerminalNode ADD() { return getToken(BKOOLParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(BKOOLParser.SUB, 0); }
		public Expr9Context expr9() {
			return getRuleContext(Expr9Context.class,0);
		}
		public Expr8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr8; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr8(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr8Context expr8() throws RecognitionException {
		Expr8Context _localctx = new Expr8Context(_ctx, getState());
		enterRule(_localctx, 102, RULE_expr8);
		int _la;
		try {
			setState(447);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD:
			case SUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(444);
				_la = _input.LA(1);
				if ( !(_la==ADD || _la==SUB) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(445);
				expr8();
				}
				break;
			case THIS:
			case NIL:
			case NEW:
			case LCB:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(446);
				expr9();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr9Context extends ParserRuleContext {
		public Expr10Context expr10() {
			return getRuleContext(Expr10Context.class,0);
		}
		public TerminalNode LSB() { return getToken(BKOOLParser.LSB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RSB() { return getToken(BKOOLParser.RSB, 0); }
		public Expr9Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr9; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr9(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr9Context expr9() throws RecognitionException {
		Expr9Context _localctx = new Expr9Context(_ctx, getState());
		enterRule(_localctx, 104, RULE_expr9);
		try {
			setState(455);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(449);
				expr10(0);
				setState(450);
				match(LSB);
				setState(451);
				expr();
				setState(452);
				match(RSB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(454);
				expr10(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr10Context extends ParserRuleContext {
		public Token bop;
		public Expr11Context expr11() {
			return getRuleContext(Expr11Context.class,0);
		}
		public Expr10Context expr10() {
			return getRuleContext(Expr10Context.class,0);
		}
		public Method_callContext method_call() {
			return getRuleContext(Method_callContext.class,0);
		}
		public TerminalNode DOT() { return getToken(BKOOLParser.DOT, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public Expr10Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr10; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr10(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr10Context expr10() throws RecognitionException {
		return expr10(0);
	}

	private Expr10Context expr10(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr10Context _localctx = new Expr10Context(_ctx, _parentState);
		Expr10Context _prevctx = _localctx;
		int _startState = 106;
		enterRecursionRule(_localctx, 106, RULE_expr10, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(458);
			expr11();
			}
			_ctx.stop = _input.LT(-1);
			setState(468);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(466);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
					case 1:
						{
						_localctx = new Expr10Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr10);
						setState(460);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(461);
						((Expr10Context)_localctx).bop = match(DOT);
						setState(462);
						method_call();
						}
						break;
					case 2:
						{
						_localctx = new Expr10Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr10);
						setState(463);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(464);
						((Expr10Context)_localctx).bop = match(DOT);
						setState(465);
						match(ID);
						}
						break;
					}
					} 
				}
				setState(470);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr11Context extends ParserRuleContext {
		public TerminalNode NEW() { return getToken(BKOOLParser.NEW, 0); }
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Expr12Context expr12() {
			return getRuleContext(Expr12Context.class,0);
		}
		public Expr11Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr11; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr11(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr11Context expr11() throws RecognitionException {
		Expr11Context _localctx = new Expr11Context(_ctx, getState());
		enterRule(_localctx, 108, RULE_expr11);
		int _la;
		try {
			setState(479);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NEW:
				enterOuterAlt(_localctx, 1);
				{
				setState(471);
				match(NEW);
				setState(472);
				match(ID);
				setState(473);
				match(LP);
				setState(475);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << THIS) | (1L << NIL) | (1L << NEW) | (1L << ADD) | (1L << SUB) | (1L << NOT) | (1L << LCB) | (1L << LP) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << BOOLLIT) | (1L << STRINGLIT) | (1L << ID))) != 0)) {
					{
					setState(474);
					expr_list();
					}
				}

				setState(477);
				match(RP);
				}
				break;
			case THIS:
			case NIL:
			case LCB:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(478);
				expr12();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr12Context extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode THIS() { return getToken(BKOOLParser.THIS, 0); }
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public TerminalNode NIL() { return getToken(BKOOLParser.NIL, 0); }
		public Expr12Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr12; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr12(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr12Context expr12() throws RecognitionException {
		Expr12Context _localctx = new Expr12Context(_ctx, getState());
		enterRule(_localctx, 110, RULE_expr12);
		try {
			setState(489);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LCB:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(481);
				literal();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(482);
				match(ID);
				}
				break;
			case THIS:
				enterOuterAlt(_localctx, 3);
				{
				setState(483);
				match(THIS);
				}
				break;
			case LP:
				enterOuterAlt(_localctx, 4);
				{
				setState(484);
				match(LP);
				setState(485);
				expr();
				setState(486);
				match(RP);
				}
				break;
			case NIL:
				enterOuterAlt(_localctx, 5);
				{
				setState(488);
				match(NIL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKOOLParser.ID, 0); }
		public TerminalNode LP() { return getToken(BKOOLParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKOOLParser.RP, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Method_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_call; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitMethod_call(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Method_callContext method_call() throws RecognitionException {
		Method_callContext _localctx = new Method_callContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_method_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(491);
			match(ID);
			setState(492);
			match(LP);
			setState(494);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << THIS) | (1L << NIL) | (1L << NEW) | (1L << ADD) | (1L << SUB) | (1L << NOT) | (1L << LCB) | (1L << LP) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << BOOLLIT) | (1L << STRINGLIT) | (1L << ID))) != 0)) {
				{
				setState(493);
				expr_list();
				}
			}

			setState(496);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr_listContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Expr_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitExpr_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expr_listContext expr_list() throws RecognitionException {
		Expr_listContext _localctx = new Expr_listContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_expr_list);
		try {
			setState(503);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(498);
				expr();
				setState(499);
				match(COMMA);
				setState(500);
				expr_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(502);
				expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(BKOOLParser.INTLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(BKOOLParser.FLOATLIT, 0); }
		public TerminalNode STRINGLIT() { return getToken(BKOOLParser.STRINGLIT, 0); }
		public TerminalNode BOOLLIT() { return getToken(BKOOLParser.BOOLLIT, 0); }
		public ArrlitContext arrlit() {
			return getRuleContext(ArrlitContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLiteral(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_literal);
		try {
			setState(510);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTLIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(505);
				match(INTLIT);
				}
				break;
			case FLOATLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(506);
				match(FLOATLIT);
				}
				break;
			case STRINGLIT:
				enterOuterAlt(_localctx, 3);
				{
				setState(507);
				match(STRINGLIT);
				}
				break;
			case BOOLLIT:
				enterOuterAlt(_localctx, 4);
				{
				setState(508);
				match(BOOLLIT);
				}
				break;
			case LCB:
				enterOuterAlt(_localctx, 5);
				{
				setState(509);
				arrlit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrlitContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(BKOOLParser.LCB, 0); }
		public Literal_listContext literal_list() {
			return getRuleContext(Literal_listContext.class,0);
		}
		public TerminalNode RCB() { return getToken(BKOOLParser.RCB, 0); }
		public ArrlitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrlit; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitArrlit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArrlitContext arrlit() throws RecognitionException {
		ArrlitContext _localctx = new ArrlitContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_arrlit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(512);
			match(LCB);
			setState(513);
			literal_list();
			setState(514);
			match(RCB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Literal_listContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Literal_listContext literal_list() {
			return getRuleContext(Literal_listContext.class,0);
		}
		public Literal_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKOOLVisitor ) return ((BKOOLVisitor<? extends T>)visitor).visitLiteral_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Literal_listContext literal_list() throws RecognitionException {
		Literal_listContext _localctx = new Literal_listContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_literal_list);
		try {
			setState(521);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(516);
				literal();
				setState(517);
				match(COMMA);
				setState(518);
				literal_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(520);
				literal();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 46:
			return expr3_sempred((Expr3Context)_localctx, predIndex);
		case 47:
			return expr4_sempred((Expr4Context)_localctx, predIndex);
		case 48:
			return expr5_sempred((Expr5Context)_localctx, predIndex);
		case 49:
			return expr6_sempred((Expr6Context)_localctx, predIndex);
		case 53:
			return expr10_sempred((Expr10Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr3_sempred(Expr3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr4_sempred(Expr4Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr5_sempred(Expr5Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr6_sempred(Expr6Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr10_sempred(Expr10Context _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 3);
		case 5:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@\u020e\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\3\2\6\2~\n\2\r\2\16\2\177\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0088\n\3"+
		"\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u0094\n\5\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\5\6\u009c\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t"+
		"\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b8\n\n"+
		"\3\13\3\13\3\13\3\13\3\13\5\13\u00bf\n\13\3\f\3\f\3\f\5\f\u00c4\n\f\3"+
		"\r\5\r\u00c7\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00d2\n\16"+
		"\3\17\3\17\3\17\3\17\3\17\5\17\u00d9\n\17\3\20\3\20\3\20\3\21\3\21\3\21"+
		"\3\21\5\21\u00e2\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u00ec"+
		"\n\23\3\24\3\24\3\24\5\24\u00f1\n\24\3\25\3\25\3\26\3\26\5\26\u00f7\n"+
		"\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0105"+
		"\n\27\3\30\3\30\5\30\u0109\n\30\3\30\5\30\u010c\n\30\3\30\3\30\3\31\3"+
		"\31\3\31\3\31\5\31\u0114\n\31\3\32\3\32\5\32\u0118\n\32\3\33\3\33\3\33"+
		"\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\5\35\u0128\n\35"+
		"\3\36\3\36\3\36\5\36\u012d\n\36\3\37\3\37\3\37\3\37\5\37\u0133\n\37\3"+
		" \3 \3 \3 \3 \3!\3!\3!\3!\3!\5!\u013f\n!\3\"\3\"\3\"\5\"\u0144\n\"\3#"+
		"\3#\3#\3#\3#\3#\3#\3#\5#\u014e\n#\3$\3$\3$\3$\3$\3%\3%\5%\u0157\n%\3&"+
		"\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3"+
		")\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\5.\u0185"+
		"\n.\3/\3/\3/\3/\3/\5/\u018c\n/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u0194"+
		"\n\60\f\60\16\60\u0197\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u019f"+
		"\n\61\f\61\16\61\u01a2\13\61\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u01aa"+
		"\n\62\f\62\16\62\u01ad\13\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u01b5"+
		"\n\63\f\63\16\63\u01b8\13\63\3\64\3\64\3\64\5\64\u01bd\n\64\3\65\3\65"+
		"\3\65\5\65\u01c2\n\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01ca\n\66\3"+
		"\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u01d5\n\67\f\67\16\67"+
		"\u01d8\13\67\38\38\38\38\58\u01de\n8\38\38\58\u01e2\n8\39\39\39\39\39"+
		"\39\39\39\59\u01ec\n9\3:\3:\3:\5:\u01f1\n:\3:\3:\3;\3;\3;\3;\3;\5;\u01fa"+
		"\n;\3<\3<\3<\3<\3<\5<\u0201\n<\3=\3=\3=\3=\3>\3>\3>\3>\3>\5>\u020c\n>"+
		"\3>\2\7^`bdl?\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64"+
		"\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\t\3\2\6\t\3\2\17\20\3\2$\'\3"+
		"\2\"#\3\2()\3\2\34\35\3\2\36!\2\u020e\2}\3\2\2\2\4\u0083\3\2\2\2\6\u008b"+
		"\3\2\2\2\b\u0093\3\2\2\2\n\u009b\3\2\2\2\f\u009d\3\2\2\2\16\u00a1\3\2"+
		"\2\2\20\u00a6\3\2\2\2\22\u00b7\3\2\2\2\24\u00be\3\2\2\2\26\u00c0\3\2\2"+
		"\2\30\u00c6\3\2\2\2\32\u00d1\3\2\2\2\34\u00d8\3\2\2\2\36\u00da\3\2\2\2"+
		" \u00e1\3\2\2\2\"\u00e3\3\2\2\2$\u00eb\3\2\2\2&\u00f0\3\2\2\2(\u00f2\3"+
		"\2\2\2*\u00f6\3\2\2\2,\u0104\3\2\2\2.\u0106\3\2\2\2\60\u0113\3\2\2\2\62"+
		"\u0117\3\2\2\2\64\u0119\3\2\2\2\66\u011d\3\2\2\28\u0127\3\2\2\2:\u0129"+
		"\3\2\2\2<\u0132\3\2\2\2>\u0134\3\2\2\2@\u013e\3\2\2\2B\u0143\3\2\2\2D"+
		"\u014d\3\2\2\2F\u014f\3\2\2\2H\u0156\3\2\2\2J\u0158\3\2\2\2L\u015f\3\2"+
		"\2\2N\u0164\3\2\2\2P\u016e\3\2\2\2R\u0171\3\2\2\2T\u0174\3\2\2\2V\u0178"+
		"\3\2\2\2X\u017d\3\2\2\2Z\u0184\3\2\2\2\\\u018b\3\2\2\2^\u018d\3\2\2\2"+
		"`\u0198\3\2\2\2b\u01a3\3\2\2\2d\u01ae\3\2\2\2f\u01bc\3\2\2\2h\u01c1\3"+
		"\2\2\2j\u01c9\3\2\2\2l\u01cb\3\2\2\2n\u01e1\3\2\2\2p\u01eb\3\2\2\2r\u01ed"+
		"\3\2\2\2t\u01f9\3\2\2\2v\u0200\3\2\2\2x\u0202\3\2\2\2z\u020b\3\2\2\2|"+
		"~\5\4\3\2}|\3\2\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080"+
		"\u0081\3\2\2\2\u0081\u0082\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\7\24\2"+
		"\2\u0084\u0087\7>\2\2\u0085\u0086\7\25\2\2\u0086\u0088\7>\2\2\u0087\u0085"+
		"\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\5\6\4\2\u008a"+
		"\5\3\2\2\2\u008b\u008c\7\60\2\2\u008c\u008d\5\b\5\2\u008d\u008e\7\61\2"+
		"\2\u008e\7\3\2\2\2\u008f\u0090\5\n\6\2\u0090\u0091\5\b\5\2\u0091\u0094"+
		"\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u008f\3\2\2\2\u0093\u0092\3\2\2\2\u0094"+
		"\t\3\2\2\2\u0095\u009c\5\30\r\2\u0096\u009c\5\16\b\2\u0097\u009c\5\20"+
		"\t\2\u0098\u009c\5\22\n\2\u0099\u009c\5\f\7\2\u009a\u009c\5\"\22\2\u009b"+
		"\u0095\3\2\2\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2\u009b\u0098\3\2"+
		"\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\13\3\2\2\2\u009d\u009e"+
		"\5&\24\2\u009e\u009f\5\24\13\2\u009f\u00a0\7\64\2\2\u00a0\r\3\2\2\2\u00a1"+
		"\u00a2\7\27\2\2\u00a2\u00a3\5&\24\2\u00a3\u00a4\5\24\13\2\u00a4\u00a5"+
		"\7\64\2\2\u00a5\17\3\2\2\2\u00a6\u00a7\7\30\2\2\u00a7\u00a8\5&\24\2\u00a8"+
		"\u00a9\5\24\13\2\u00a9\u00aa\7\64\2\2\u00aa\21\3\2\2\2\u00ab\u00ac\7\27"+
		"\2\2\u00ac\u00ad\7\30\2\2\u00ad\u00ae\5&\24\2\u00ae\u00af\5\24\13\2\u00af"+
		"\u00b0\7\64\2\2\u00b0\u00b8\3\2\2\2\u00b1\u00b2\7\30\2\2\u00b2\u00b3\7"+
		"\27\2\2\u00b3\u00b4\5&\24\2\u00b4\u00b5\5\24\13\2\u00b5\u00b6\7\64\2\2"+
		"\u00b6\u00b8\3\2\2\2\u00b7\u00ab\3\2\2\2\u00b7\u00b1\3\2\2\2\u00b8\23"+
		"\3\2\2\2\u00b9\u00ba\5\26\f\2\u00ba\u00bb\7\67\2\2\u00bb\u00bc\5\24\13"+
		"\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf\5\26\f\2\u00be\u00b9\3\2\2\2\u00be"+
		"\u00bd\3\2\2\2\u00bf\25\3\2\2\2\u00c0\u00c3\7>\2\2\u00c1\u00c2\7-\2\2"+
		"\u00c2\u00c4\5X-\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\27\3"+
		"\2\2\2\u00c5\u00c7\7\30\2\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7"+
		"\u00c8\3\2\2\2\u00c8\u00c9\5$\23\2\u00c9\u00ca\7>\2\2\u00ca\u00cb\7\62"+
		"\2\2\u00cb\u00cc\5\32\16\2\u00cc\u00cd\7\63\2\2\u00cd\u00ce\5.\30\2\u00ce"+
		"\31\3\2\2\2\u00cf\u00d2\5\34\17\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2"+
		"\2\2\u00d1\u00d0\3\2\2\2\u00d2\33\3\2\2\2\u00d3\u00d4\5\36\20\2\u00d4"+
		"\u00d5\7\64\2\2\u00d5\u00d6\5\34\17\2\u00d6\u00d9\3\2\2\2\u00d7\u00d9"+
		"\5\36\20\2\u00d8\u00d3\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\35\3\2\2\2\u00da"+
		"\u00db\5&\24\2\u00db\u00dc\5 \21\2\u00dc\37\3\2\2\2\u00dd\u00de\7>\2\2"+
		"\u00de\u00df\7\67\2\2\u00df\u00e2\5 \21\2\u00e0\u00e2\7>\2\2\u00e1\u00dd"+
		"\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2!\3\2\2\2\u00e3\u00e4\7>\2\2\u00e4\u00e5"+
		"\7\62\2\2\u00e5\u00e6\5\32\16\2\u00e6\u00e7\7\63\2\2\u00e7\u00e8\5.\30"+
		"\2\u00e8#\3\2\2\2\u00e9\u00ec\5&\24\2\u00ea\u00ec\7\n\2\2\u00eb\u00e9"+
		"\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec%\3\2\2\2\u00ed\u00f1\5(\25\2\u00ee"+
		"\u00f1\5*\26\2\u00ef\u00f1\7>\2\2\u00f0\u00ed\3\2\2\2\u00f0\u00ee\3\2"+
		"\2\2\u00f0\u00ef\3\2\2\2\u00f1\'\3\2\2\2\u00f2\u00f3\t\2\2\2\u00f3)\3"+
		"\2\2\2\u00f4\u00f7\5(\25\2\u00f5\u00f7\7>\2\2\u00f6\u00f4\3\2\2\2\u00f6"+
		"\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7.\2\2\u00f9\u00fa\78\2"+
		"\2\u00fa\u00fb\7/\2\2\u00fb+\3\2\2\2\u00fc\u0105\5.\30\2\u00fd\u0105\5"+
		"> \2\u00fe\u0105\5H%\2\u00ff\u0105\5N(\2\u0100\u0105\5P)\2\u0101\u0105"+
		"\5R*\2\u0102\u0105\5T+\2\u0103\u0105\5V,\2\u0104\u00fc\3\2\2\2\u0104\u00fd"+
		"\3\2\2\2\u0104\u00fe\3\2\2\2\u0104\u00ff\3\2\2\2\u0104\u0100\3\2\2\2\u0104"+
		"\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105-\3\2\2\2"+
		"\u0106\u0108\7\60\2\2\u0107\u0109\5\60\31\2\u0108\u0107\3\2\2\2\u0108"+
		"\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u010c\5<\37\2\u010b\u010a\3\2"+
		"\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\7\61\2\2\u010e"+
		"/\3\2\2\2\u010f\u0110\5\62\32\2\u0110\u0111\5\60\31\2\u0111\u0114\3\2"+
		"\2\2\u0112\u0114\5\62\32\2\u0113\u010f\3\2\2\2\u0113\u0112\3\2\2\2\u0114"+
		"\61\3\2\2\2\u0115\u0118\5\64\33\2\u0116\u0118\5\66\34\2\u0117\u0115\3"+
		"\2\2\2\u0117\u0116\3\2\2\2\u0118\63\3\2\2\2\u0119\u011a\5&\24\2\u011a"+
		"\u011b\58\35\2\u011b\u011c\7\64\2\2\u011c\65\3\2\2\2\u011d\u011e\7\27"+
		"\2\2\u011e\u011f\5&\24\2\u011f\u0120\58\35\2\u0120\u0121\7\64\2\2\u0121"+
		"\67\3\2\2\2\u0122\u0123\5:\36\2\u0123\u0124\7\67\2\2\u0124\u0125\58\35"+
		"\2\u0125\u0128\3\2\2\2\u0126\u0128\5:\36\2\u0127\u0122\3\2\2\2\u0127\u0126"+
		"\3\2\2\2\u01289\3\2\2\2\u0129\u012c\7>\2\2\u012a\u012b\7-\2\2\u012b\u012d"+
		"\5X-\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d;\3\2\2\2\u012e\u012f"+
		"\5,\27\2\u012f\u0130\5<\37\2\u0130\u0133\3\2\2\2\u0131\u0133\5,\27\2\u0132"+
		"\u012e\3\2\2\2\u0132\u0131\3\2\2\2\u0133=\3\2\2\2\u0134\u0135\5@!\2\u0135"+
		"\u0136\7,\2\2\u0136\u0137\5X-\2\u0137\u0138\7\64\2\2\u0138?\3\2\2\2\u0139"+
		"\u013a\7\62\2\2\u013a\u013b\5@!\2\u013b\u013c\7\63\2\2\u013c\u013f\3\2"+
		"\2\2\u013d\u013f\5B\"\2\u013e\u0139\3\2\2\2\u013e\u013d\3\2\2\2\u013f"+
		"A\3\2\2\2\u0140\u0144\7>\2\2\u0141\u0144\5F$\2\u0142\u0144\5D#\2\u0143"+
		"\u0140\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144C\3\2\2\2"+
		"\u0145\u0146\5n8\2\u0146\u0147\7\66\2\2\u0147\u0148\5r:\2\u0148\u014e"+
		"\3\2\2\2\u0149\u014a\5n8\2\u014a\u014b\7\66\2\2\u014b\u014c\7>\2\2\u014c"+
		"\u014e\3\2\2\2\u014d\u0145\3\2\2\2\u014d\u0149\3\2\2\2\u014eE\3\2\2\2"+
		"\u014f\u0150\5l\67\2\u0150\u0151\7.\2\2\u0151\u0152\5X-\2\u0152\u0153"+
		"\7/\2\2\u0153G\3\2\2\2\u0154\u0157\5L\'\2\u0155\u0157\5J&\2\u0156\u0154"+
		"\3\2\2\2\u0156\u0155\3\2\2\2\u0157I\3\2\2\2\u0158\u0159\7\13\2\2\u0159"+
		"\u015a\5X-\2\u015a\u015b\7\f\2\2\u015b\u015c\5,\27\2\u015c\u015d\7\r\2"+
		"\2\u015d\u015e\5,\27\2\u015eK\3\2\2\2\u015f\u0160\7\13\2\2\u0160\u0161"+
		"\5X-\2\u0161\u0162\7\f\2\2\u0162\u0163\5,\27\2\u0163M\3\2\2\2\u0164\u0165"+
		"\7\16\2\2\u0165\u0166\7>\2\2\u0166\u0167\7,\2\2\u0167\u0168\5X-\2\u0168"+
		"\u0169\3\2\2\2\u0169\u016a\t\3\2\2\u016a\u016b\5X-\2\u016b\u016c\7\21"+
		"\2\2\u016c\u016d\5,\27\2\u016dO\3\2\2\2\u016e\u016f\7\22\2\2\u016f\u0170"+
		"\7\64\2\2\u0170Q\3\2\2\2\u0171\u0172\7\23\2\2\u0172\u0173\7\64\2\2\u0173"+
		"S\3\2\2\2\u0174\u0175\7\33\2\2\u0175\u0176\5X-\2\u0176\u0177\7\64\2\2"+
		"\u0177U\3\2\2\2\u0178\u0179\5X-\2\u0179\u017a\7\66\2\2\u017a\u017b\5r"+
		":\2\u017b\u017c\7\64\2\2\u017cW\3\2\2\2\u017d\u017e\5Z.\2\u017eY\3\2\2"+
		"\2\u017f\u0180\5\\/\2\u0180\u0181\t\4\2\2\u0181\u0182\5\\/\2\u0182\u0185"+
		"\3\2\2\2\u0183\u0185\5\\/\2\u0184\u017f\3\2\2\2\u0184\u0183\3\2\2\2\u0185"+
		"[\3\2\2\2\u0186\u0187\5^\60\2\u0187\u0188\t\5\2\2\u0188\u0189\5^\60\2"+
		"\u0189\u018c\3\2\2\2\u018a\u018c\5^\60\2\u018b\u0186\3\2\2\2\u018b\u018a"+
		"\3\2\2\2\u018c]\3\2\2\2\u018d\u018e\b\60\1\2\u018e\u018f\5`\61\2\u018f"+
		"\u0195\3\2\2\2\u0190\u0191\f\4\2\2\u0191\u0192\t\6\2\2\u0192\u0194\5`"+
		"\61\2\u0193\u0190\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195"+
		"\u0196\3\2\2\2\u0196_\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\b\61\1\2"+
		"\u0199\u019a\5b\62\2\u019a\u01a0\3\2\2\2\u019b\u019c\f\4\2\2\u019c\u019d"+
		"\t\7\2\2\u019d\u019f\5b\62\2\u019e\u019b\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0"+
		"\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1a\3\2\2\2\u01a2\u01a0\3\2\2\2"+
		"\u01a3\u01a4\b\62\1\2\u01a4\u01a5\5d\63\2\u01a5\u01ab\3\2\2\2\u01a6\u01a7"+
		"\f\4\2\2\u01a7\u01a8\t\b\2\2\u01a8\u01aa\5d\63\2\u01a9\u01a6\3\2\2\2\u01aa"+
		"\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01acc\3\2\2\2"+
		"\u01ad\u01ab\3\2\2\2\u01ae\u01af\b\63\1\2\u01af\u01b0\5f\64\2\u01b0\u01b6"+
		"\3\2\2\2\u01b1\u01b2\f\4\2\2\u01b2\u01b3\7+\2\2\u01b3\u01b5\5f\64\2\u01b4"+
		"\u01b1\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2"+
		"\2\2\u01b7e\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7*\2\2\u01ba\u01bd"+
		"\5f\64\2\u01bb\u01bd\5h\65\2\u01bc\u01b9\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd"+
		"g\3\2\2\2\u01be\u01bf\t\7\2\2\u01bf\u01c2\5h\65\2\u01c0\u01c2\5j\66\2"+
		"\u01c1\u01be\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2i\3\2\2\2\u01c3\u01c4\5"+
		"l\67\2\u01c4\u01c5\7.\2\2\u01c5\u01c6\5X-\2\u01c6\u01c7\7/\2\2\u01c7\u01ca"+
		"\3\2\2\2\u01c8\u01ca\5l\67\2\u01c9\u01c3\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca"+
		"k\3\2\2\2\u01cb\u01cc\b\67\1\2\u01cc\u01cd\5n8\2\u01cd\u01d6\3\2\2\2\u01ce"+
		"\u01cf\f\5\2\2\u01cf\u01d0\7\66\2\2\u01d0\u01d5\5r:\2\u01d1\u01d2\f\4"+
		"\2\2\u01d2\u01d3\7\66\2\2\u01d3\u01d5\7>\2\2\u01d4\u01ce\3\2\2\2\u01d4"+
		"\u01d1\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2"+
		"\2\2\u01d7m\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01da\7\32\2\2\u01da\u01db"+
		"\7>\2\2\u01db\u01dd\7\62\2\2\u01dc\u01de\5t;\2\u01dd\u01dc\3\2\2\2\u01dd"+
		"\u01de\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e2\7\63\2\2\u01e0\u01e2\5"+
		"p9\2\u01e1\u01d9\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2o\3\2\2\2\u01e3\u01ec"+
		"\5v<\2\u01e4\u01ec\7>\2\2\u01e5\u01ec\7\26\2\2\u01e6\u01e7\7\62\2\2\u01e7"+
		"\u01e8\5X-\2\u01e8\u01e9\7\63\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01ec\7\31"+
		"\2\2\u01eb\u01e3\3\2\2\2\u01eb\u01e4\3\2\2\2\u01eb\u01e5\3\2\2\2\u01eb"+
		"\u01e6\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ecq\3\2\2\2\u01ed\u01ee\7>\2\2\u01ee"+
		"\u01f0\7\62\2\2\u01ef\u01f1\5t;\2\u01f0\u01ef\3\2\2\2\u01f0\u01f1\3\2"+
		"\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\7\63\2\2\u01f3s\3\2\2\2\u01f4\u01f5"+
		"\5X-\2\u01f5\u01f6\7\67\2\2\u01f6\u01f7\5t;\2\u01f7\u01fa\3\2\2\2\u01f8"+
		"\u01fa\5X-\2\u01f9\u01f4\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fau\3\2\2\2\u01fb"+
		"\u0201\78\2\2\u01fc\u0201\79\2\2\u01fd\u0201\7;\2\2\u01fe\u0201\7:\2\2"+
		"\u01ff\u0201\5x=\2\u0200\u01fb\3\2\2\2\u0200\u01fc\3\2\2\2\u0200\u01fd"+
		"\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2\u0201w\3\2\2\2\u0202"+
		"\u0203\7\60\2\2\u0203\u0204\5z>\2\u0204\u0205\7\61\2\2\u0205y\3\2\2\2"+
		"\u0206\u0207\5v<\2\u0207\u0208\7\67\2\2\u0208\u0209\5z>\2\u0209\u020c"+
		"\3\2\2\2\u020a\u020c\5v<\2\u020b\u0206\3\2\2\2\u020b\u020a\3\2\2\2\u020c"+
		"{\3\2\2\2.\177\u0087\u0093\u009b\u00b7\u00be\u00c3\u00c6\u00d1\u00d8\u00e1"+
		"\u00eb\u00f0\u00f6\u0104\u0108\u010b\u0113\u0117\u0127\u012c\u0132\u013e"+
		"\u0143\u014d\u0156\u0184\u018b\u0195\u01a0\u01ab\u01b6\u01bc\u01c1\u01c9"+
		"\u01d4\u01d6\u01dd\u01e1\u01eb\u01f0\u01f9\u0200\u020b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}