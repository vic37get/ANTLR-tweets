from antlr4 import *
from gen.ttLexer import ttLexer
from gen.ttParser import ttParser

def main():
    dados = FileStream("inputs/input1.txt", encoding="utf-8")
    #dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = ttLexer(dados)
    for tok in lexer.getAllTokens():
        print(tok.text, tok.type)
    lexer.reset()
    stream = CommonTokenStream(lexer)

    for token in stream.tokens:
        token_type = token.type
        token_name = lexer.symbolicNames[token_type]
        print("Token:", token.text, ", Classe:", token_name)

    parser = ttParser(stream)
    tree = parser.prog()
    print(tree.toStringTree())

if __name__ == '__main__':
    main()