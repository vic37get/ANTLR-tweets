// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class tt4Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VALOR_MONETARIO=1, SIMBOLO_MOEDA=2, VALOR=3, DIGITO=4, SIMBOLO_QUANTIDADE=5, 
		MOEDA=6, PALAVRA=7, LETRA=8, WS=9;
	public static final int
		RULE_prog = 0, RULE_monetario = 1, RULE_palavra = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "monetario", "palavra"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VALOR_MONETARIO", "SIMBOLO_MOEDA", "VALOR", "DIGITO", "SIMBOLO_QUANTIDADE", 
			"MOEDA", "PALAVRA", "LETRA", "WS"
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
	public String getGrammarFileName() { return "java-escape"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public tt4Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<PalavraContext> palavra() {
			return getRuleContexts(PalavraContext.class);
		}
		public PalavraContext palavra(int i) {
			return getRuleContext(PalavraContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tt4Listener ) ((tt4Listener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tt4Listener ) ((tt4Listener)listener).exitProg(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof tt4Visitor ) return ((tt4Visitor<? extends T>)visitor).visitProg(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PALAVRA) {
				{
				{
				setState(6);
				palavra();
				}
				}
				setState(11);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class MonetarioContext extends ParserRuleContext {
		public TerminalNode VALOR_MONETARIO() { return getToken(tt4Parser.VALOR_MONETARIO, 0); }
		public MonetarioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_monetario; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tt4Listener ) ((tt4Listener)listener).enterMonetario(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tt4Listener ) ((tt4Listener)listener).exitMonetario(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof tt4Visitor ) return ((tt4Visitor<? extends T>)visitor).visitMonetario(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MonetarioContext monetario() throws RecognitionException {
		MonetarioContext _localctx = new MonetarioContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_monetario);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(12);
			match(VALOR_MONETARIO);
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

	@SuppressWarnings("CheckReturnValue")
	public static class PalavraContext extends ParserRuleContext {
		public TerminalNode PALAVRA() { return getToken(tt4Parser.PALAVRA, 0); }
		public PalavraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_palavra; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof tt4Listener ) ((tt4Listener)listener).enterPalavra(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof tt4Listener ) ((tt4Listener)listener).exitPalavra(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof tt4Visitor ) return ((tt4Visitor<? extends T>)visitor).visitPalavra(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PalavraContext palavra() throws RecognitionException {
		PalavraContext _localctx = new PalavraContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_palavra);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(14);
			match(PALAVRA);
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

	public static final String _serializedATN =
		"\u0004\u0001\t\u0011\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0005\u0000\b\b\u0000\n\u0000\f\u0000\u000b"+
		"\t\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0000"+
		"\u0000\u0003\u0000\u0002\u0004\u0000\u0000\u000e\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0002\f\u0001\u0000\u0000\u0000\u0004\u000e\u0001\u0000\u0000\u0000"+
		"\u0006\b\u0003\u0004\u0002\u0000\u0007\u0006\u0001\u0000\u0000\u0000\b"+
		"\u000b\u0001\u0000\u0000\u0000\t\u0007\u0001\u0000\u0000\u0000\t\n\u0001"+
		"\u0000\u0000\u0000\n\u0001\u0001\u0000\u0000\u0000\u000b\t\u0001\u0000"+
		"\u0000\u0000\f\r\u0005\u0001\u0000\u0000\r\u0003\u0001\u0000\u0000\u0000"+
		"\u000e\u000f\u0005\u0007\u0000\u0000\u000f\u0005\u0001\u0000\u0000\u0000"+
		"\u0001\t";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}