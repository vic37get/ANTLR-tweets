from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from antlr4 import *
from gen.ttLexer import ttLexer
from unidecode import unidecode
import json


def home(request):
    dados = ''
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        dados = uploaded_file.read().decode('utf-8')

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
            dict_tokens[k] = str((set(v))).replace('{', '').replace('}', '').replace("'", '')
        lexer.reset()
        
        with open('db/entrada.json', 'w') as json_file:
            json.dump(dict_tokens, json_file)

        context = {
            'dict_tokens': dict_tokens,
            'tweet': dados,
        }
        
        template = loader.get_template('antlrtt_app/home.html')
        return HttpResponse(template.render(context, request))

    return render(request, 'antlrtt_app/home.html')

def download_json(request):
    with open('db/entrada.json', 'r') as json_file:
        dict_tokens = json.load(json_file)
    
    dict_tokens = {
        'dict_tokens': dict_tokens,
    }

    json_data = json.dumps(dict_tokens, indent=4)

    response = HttpResponse(json_data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="tokens.json"'
    
    return response