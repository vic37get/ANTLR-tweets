from antlr4 import *
from gen.ttLexer import ttLexer
from gen.ttParser import ttParser
from unidecode import unidecode

def main():
    with open("inputs/input_financeiro1.txt", 'r', encoding='utf-8') as f:
        dados = f.read()
    dados = unidecode(dados)
    dados = InputStream(dados)
    lexer = ttLexer(dados)

    dict_tokens = {}

    for token in lexer.getAllTokens():
        if lexer.symbolicNames[token.type] in dict_tokens:
            dict_tokens[lexer.symbolicNames[token.type]].append(token.text)
        else:
            dict_tokens[lexer.symbolicNames[token.type]] = [token.text]

    for k, v in dict_tokens.items():
        dict_tokens[k] = list(set(v))
    lexer.reset()

if __name__ == '__main__':
    main()