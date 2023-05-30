// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link tt4Parser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface tt4Visitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link tt4Parser#prog}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProg(tt4Parser.ProgContext ctx);
	/**
	 * Visit a parse tree produced by {@link tt4Parser#monetario}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMonetario(tt4Parser.MonetarioContext ctx);
	/**
	 * Visit a parse tree produced by {@link tt4Parser#palavra}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPalavra(tt4Parser.PalavraContext ctx);
}