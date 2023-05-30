// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class tt4Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VALOR_MONETARIO=1, SIMBOLO_MOEDA=2, VALOR=3, DIGITO=4, SIMBOLO_QUANTIDADE=5, 
		MOEDA=6, PALAVRA=7, LETRA=8, WS=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VALOR_MONETARIO", "SIMBOLO_MOEDA", "VALOR", "DIGITO", "SIMBOLO_QUANTIDADE", 
			"MOEDA", "PALAVRA", "LETRA", "WS"
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


	public tt4Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "tt4.g4"; }

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

	public static final String _serializedATN =
		"\u0004\u0000\tr\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0003\u0001\u0018\b\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0005\u0002\u001e\b\u0002\n\u0002\f\u0002!\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0004\u0002*\b\u0002\u000b\u0002\f\u0002+\u0005\u0002.\b\u0002\n\u0002"+
		"\f\u00021\t\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004N\b"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005a\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005f\b\u0005"+
		"\u0001\u0006\u0004\u0006i\b\u0006\u000b\u0006\f\u0006j\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0000\u0000\t\u0001\u0001\u0003"+
		"\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011"+
		"\t\u0001\u0000\u0007\u0002\u0000RRrr\u0001\u000019\u0001\u000009\u0002"+
		"\u0000kkmm\u0003\u0000oo\u00b3\u00b3\u00c3\u00c3\u0013\u0000AZaz\u00a0"+
		"\u00a3\u00a7\u00a7\u00a9\u00aa\u00ad\u00ad\u00b3\u00b5\u00ba\u00ba\u00bc"+
		"\u00bc\u00c3\u00c3\u0153\u0153\u0160\u0161\u0192\u0192\u201a\u201a\u201c"+
		"\u201d\u2021\u2022\u2030\u2030\u20ac\u20ac\u8000\ufffd\u8000\ufffd\u0003"+
		"\u0000\t\n\f\r  \u007f\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0001\u0013\u0001\u0000"+
		"\u0000\u0000\u0003\u0017\u0001\u0000\u0000\u0000\u0005\u001b\u0001\u0000"+
		"\u0000\u0000\u00072\u0001\u0000\u0000\u0000\tM\u0001\u0000\u0000\u0000"+
		"\u000be\u0001\u0000\u0000\u0000\rh\u0001\u0000\u0000\u0000\u000fl\u0001"+
		"\u0000\u0000\u0000\u0011n\u0001\u0000\u0000\u0000\u0013\u0014\u0003\u0005"+
		"\u0002\u0000\u0014\u0015\u0003\r\u0006\u0000\u0015\u0002\u0001\u0000\u0000"+
		"\u0000\u0016\u0018\u0007\u0000\u0000\u0000\u0017\u0016\u0001\u0000\u0000"+
		"\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u0019\u0001\u0000\u0000"+
		"\u0000\u0019\u001a\u0005$\u0000\u0000\u001a\u0004\u0001\u0000\u0000\u0000"+
		"\u001b\u001f\u0007\u0001\u0000\u0000\u001c\u001e\u0003\u0007\u0003\u0000"+
		"\u001d\u001c\u0001\u0000\u0000\u0000\u001e!\u0001\u0000\u0000\u0000\u001f"+
		"\u001d\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 /\u0001"+
		"\u0000\u0000\u0000!\u001f\u0001\u0000\u0000\u0000\"#\u0005.\u0000\u0000"+
		"#$\u0003\u0007\u0003\u0000$%\u0003\u0007\u0003\u0000%&\u0003\u0007\u0003"+
		"\u0000&.\u0001\u0000\u0000\u0000\')\u0005,\u0000\u0000(*\u0003\u0007\u0003"+
		"\u0000)(\u0001\u0000\u0000\u0000*+\u0001\u0000\u0000\u0000+)\u0001\u0000"+
		"\u0000\u0000+,\u0001\u0000\u0000\u0000,.\u0001\u0000\u0000\u0000-\"\u0001"+
		"\u0000\u0000\u0000-\'\u0001\u0000\u0000\u0000.1\u0001\u0000\u0000\u0000"+
		"/-\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000\u00000\u0006\u0001\u0000"+
		"\u0000\u00001/\u0001\u0000\u0000\u000023\u0007\u0002\u0000\u00003\b\u0001"+
		"\u0000\u0000\u000045\u0005[\u0000\u000056\u0005b\u0000\u000067\u0005m"+
		"\u0000\u000078\u0005]\u0000\u000089\u0005i\u0000\u00009:\u0005l\u0000"+
		"\u0000:;\u0005h\u0000\u0000;<\u0005a\u0000\u0000<N\u0005o\u0000\u0000"+
		"=>\u0005[\u0000\u0000>?\u0005b\u0000\u0000?@\u0005m\u0000\u0000@A\u0005"+
		"]\u0000\u0000AB\u0005i\u0000\u0000BC\u0005l\u0000\u0000CD\u0005h\u0000"+
		"\u0000DE\u0005o\u0000\u0000EF\u0005e\u0000\u0000FN\u0005s\u0000\u0000"+
		"GH\u0005m\u0000\u0000HI\u0005i\u0000\u0000IN\u0005l\u0000\u0000JN\u0007"+
		"\u0003\u0000\u0000KL\u0005b\u0000\u0000LN\u0005i\u0000\u0000M4\u0001\u0000"+
		"\u0000\u0000M=\u0001\u0000\u0000\u0000MG\u0001\u0000\u0000\u0000MJ\u0001"+
		"\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000N\n\u0001\u0000\u0000\u0000"+
		"OP\u0005r\u0000\u0000PQ\u0005e\u0000\u0000QR\u0005a\u0000\u0000Rf\u0005"+
		"l\u0000\u0000ST\u0005r\u0000\u0000TU\u0005e\u0000\u0000UV\u0005a\u0000"+
		"\u0000VW\u0005i\u0000\u0000Wf\u0005s\u0000\u0000XY\u0005d\u0000\u0000"+
		"YZ\u0007\u0004\u0000\u0000Z[\u0005l\u0000\u0000[\\\u0005a\u0000\u0000"+
		"\\]\u0005r\u0000\u0000]`\u0001\u0000\u0000\u0000^_\u0005e\u0000\u0000"+
		"_a\u0005s\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000"+
		"af\u0001\u0000\u0000\u0000bc\u0005d\u0000\u0000cd\u0005o\u0000\u0000d"+
		"f\u0005l\u0000\u0000eO\u0001\u0000\u0000\u0000eS\u0001\u0000\u0000\u0000"+
		"eX\u0001\u0000\u0000\u0000eb\u0001\u0000\u0000\u0000f\f\u0001\u0000\u0000"+
		"\u0000gi\u0003\u000f\u0007\u0000hg\u0001\u0000\u0000\u0000ij\u0001\u0000"+
		"\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000k\u000e"+
		"\u0001\u0000\u0000\u0000lm\u0007\u0005\u0000\u0000m\u0010\u0001\u0000"+
		"\u0000\u0000no\u0007\u0006\u0000\u0000op\u0001\u0000\u0000\u0000pq\u0006"+
		"\b\u0000\u0000q\u0012\u0001\u0000\u0000\u0000\n\u0000\u0017\u001f+-/M"+
		"`ej\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}