// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link tt4Parser}.
 */
public interface tt4Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link tt4Parser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(tt4Parser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link tt4Parser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(tt4Parser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link tt4Parser#monetario}.
	 * @param ctx the parse tree
	 */
	void enterMonetario(tt4Parser.MonetarioContext ctx);
	/**
	 * Exit a parse tree produced by {@link tt4Parser#monetario}.
	 * @param ctx the parse tree
	 */
	void exitMonetario(tt4Parser.MonetarioContext ctx);
	/**
	 * Enter a parse tree produced by {@link tt4Parser#palavra}.
	 * @param ctx the parse tree
	 */
	void enterPalavra(tt4Parser.PalavraContext ctx);
	/**
	 * Exit a parse tree produced by {@link tt4Parser#palavra}.
	 * @param ctx the parse tree
	 */
	void exitPalavra(tt4Parser.PalavraContext ctx);
}