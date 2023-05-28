from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from antlr4 import *
from gen.ttLexer import ttLexer
from unidecode import unidecode


def home(request):
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
    print(dict_tokens)

    for k, v in dict_tokens.items():
        dict_tokens[k] = list(set(v))
    lexer.reset()

    context = {
        'dict_tokens': dict_tokens,
        'tweet': dados,
    }
    template = loader.get_template('antlrtt_app/home.html')
    return HttpResponse(template.render(context, request))