from antlr4 import *
from gen.ttLexer import ttLexer
from gen.ttParser import ttParser
from unidecode import unidecode

def main():
    with open("inputs/input_financeiro1.txt", 'r', encoding='utf-8') as f:
        dados = f.read()
    print(dados)
    dados = unidecode(dados)
    print(dados)
    dados = InputStream(dados)
    #dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = ttLexer(dados)
    for token in lexer.getAllTokens():
        print("Token:", token.text, ", Classe:", lexer.symbolicNames[token.type])
    lexer.reset()
    stream = CommonTokenStream(lexer)

    parser = ttParser(stream)
    tree = parser.prog()
    print(tree.toStringTree())

if __name__ == '__main__':
    main()