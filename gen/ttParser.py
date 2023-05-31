# Generated from H:/Documentos/ANTLR-tweets\tt.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,4,0,48,8,0,11,0,12,0,49,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,3,2,59,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,10,1,10,3,10,79,8,10,1,11,1,11,1,11,1,11,1,11,
        3,11,86,8,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,0,0,16,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,7,1,0,1,2,1,0,7,8,1,
        0,9,10,1,0,17,18,2,0,24,24,28,28,1,0,29,30,2,0,31,31,33,34,103,0,
        47,1,0,0,0,2,51,1,0,0,0,4,58,1,0,0,0,6,60,1,0,0,0,8,62,1,0,0,0,10,
        64,1,0,0,0,12,66,1,0,0,0,14,68,1,0,0,0,16,70,1,0,0,0,18,72,1,0,0,
        0,20,78,1,0,0,0,22,85,1,0,0,0,24,87,1,0,0,0,26,89,1,0,0,0,28,91,
        1,0,0,0,30,93,1,0,0,0,32,48,3,4,2,0,33,48,3,8,4,0,34,48,3,18,9,0,
        35,48,3,24,12,0,36,48,3,30,15,0,37,48,5,38,0,0,38,48,3,22,11,0,39,
        48,3,28,14,0,40,48,5,37,0,0,41,48,3,2,1,0,42,48,3,10,5,0,43,48,3,
        16,8,0,44,48,3,12,6,0,45,48,3,14,7,0,46,48,3,26,13,0,47,32,1,0,0,
        0,47,33,1,0,0,0,47,34,1,0,0,0,47,35,1,0,0,0,47,36,1,0,0,0,47,37,
        1,0,0,0,47,38,1,0,0,0,47,39,1,0,0,0,47,40,1,0,0,0,47,41,1,0,0,0,
        47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,47,45,1,0,0,0,47,46,1,
        0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,0,51,
        52,7,0,0,0,52,3,1,0,0,0,53,59,5,3,0,0,54,59,3,6,3,0,55,59,5,4,0,
        0,56,59,5,5,0,0,57,59,5,6,0,0,58,53,1,0,0,0,58,54,1,0,0,0,58,55,
        1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,5,1,0,0,0,60,61,7,1,0,0,61,
        7,1,0,0,0,62,63,7,2,0,0,63,9,1,0,0,0,64,65,5,11,0,0,65,11,1,0,0,
        0,66,67,5,12,0,0,67,13,1,0,0,0,68,69,5,13,0,0,69,15,1,0,0,0,70,71,
        5,14,0,0,71,17,1,0,0,0,72,73,7,3,0,0,73,19,1,0,0,0,74,75,5,19,0,
        0,75,79,5,20,0,0,76,77,5,21,0,0,77,79,5,20,0,0,78,74,1,0,0,0,78,
        76,1,0,0,0,79,21,1,0,0,0,80,86,5,22,0,0,81,86,5,21,0,0,82,86,3,20,
        10,0,83,86,5,19,0,0,84,86,5,23,0,0,85,80,1,0,0,0,85,81,1,0,0,0,85,
        82,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,23,1,0,0,0,87,88,7,4,0,
        0,88,25,1,0,0,0,89,90,7,5,0,0,90,27,1,0,0,0,91,92,7,6,0,0,92,29,
        1,0,0,0,93,94,5,35,0,0,94,31,1,0,0,0,5,47,49,58,78,85
    ]

class ttParser ( Parser ):

    grammarFileName = "tt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'...'" ]

    symbolicNames = [ "<INVALID>", "DATA_COM_BARRA", "DIA_SEMANA", "TURNO", 
                      "DIA_TEMPO", "MEDIDA_TEMPO", "MES", "HORA_EXTENSO", 
                      "HORA_FORMATADA", "RENDA_FIXA", "RENDA_VARIAVEL", 
                      "INDICES", "BOLSA", "OPERACAO", "TENDENCIA", "ALTO", 
                      "BAIXO", "FII", "ACAO", "NUMERO", "SIMBOLO_QUANTIDADE", 
                      "FRACAO", "PORCENTAGEM", "ORDINAL", "VALOR_MONETARIO", 
                      "SIMBOLO_MOEDA", "DIGITO", "VALOR", "MOEDA", "DIVIDENDO", 
                      "JCP", "PONTUACAO", "RET", "OUTROS_CHARS", "EMOJI", 
                      "PALAVRA", "LETRA", "MENCOES", "HASHTAGS", "WS" ]

    RULE_prog = 0
    RULE_datas = 1
    RULE_tempo = 2
    RULE_horas = 3
    RULE_tipo_investimento = 4
    RULE_indices = 5
    RULE_bolsa = 6
    RULE_operacao = 7
    RULE_tendencia = 8
    RULE_ativo = 9
    RULE_quantidade = 10
    RULE_numeros = 11
    RULE_monetario = 12
    RULE_renda = 13
    RULE_char = 14
    RULE_palavra = 15

    ruleNames =  [ "prog", "datas", "tempo", "horas", "tipo_investimento", 
                   "indices", "bolsa", "operacao", "tendencia", "ativo", 
                   "quantidade", "numeros", "monetario", "renda", "char", 
                   "palavra" ]

    EOF = Token.EOF
    DATA_COM_BARRA=1
    DIA_SEMANA=2
    TURNO=3
    DIA_TEMPO=4
    MEDIDA_TEMPO=5
    MES=6
    HORA_EXTENSO=7
    HORA_FORMATADA=8
    RENDA_FIXA=9
    RENDA_VARIAVEL=10
    INDICES=11
    BOLSA=12
    OPERACAO=13
    TENDENCIA=14
    ALTO=15
    BAIXO=16
    FII=17
    ACAO=18
    NUMERO=19
    SIMBOLO_QUANTIDADE=20
    FRACAO=21
    PORCENTAGEM=22
    ORDINAL=23
    VALOR_MONETARIO=24
    SIMBOLO_MOEDA=25
    DIGITO=26
    VALOR=27
    MOEDA=28
    DIVIDENDO=29
    JCP=30
    PONTUACAO=31
    RET=32
    OUTROS_CHARS=33
    EMOJI=34
    PALAVRA=35
    LETRA=36
    MENCOES=37
    HASHTAGS=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tempo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.TempoContext)
            else:
                return self.getTypedRuleContext(ttParser.TempoContext,i)


        def tipo_investimento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.Tipo_investimentoContext)
            else:
                return self.getTypedRuleContext(ttParser.Tipo_investimentoContext,i)


        def ativo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.AtivoContext)
            else:
                return self.getTypedRuleContext(ttParser.AtivoContext,i)


        def monetario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.MonetarioContext)
            else:
                return self.getTypedRuleContext(ttParser.MonetarioContext,i)


        def palavra(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.PalavraContext)
            else:
                return self.getTypedRuleContext(ttParser.PalavraContext,i)


        def HASHTAGS(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.HASHTAGS)
            else:
                return self.getToken(ttParser.HASHTAGS, i)

        def numeros(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.NumerosContext)
            else:
                return self.getTypedRuleContext(ttParser.NumerosContext,i)


        def char(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.CharContext)
            else:
                return self.getTypedRuleContext(ttParser.CharContext,i)


        def MENCOES(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.MENCOES)
            else:
                return self.getToken(ttParser.MENCOES, i)

        def datas(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.DatasContext)
            else:
                return self.getTypedRuleContext(ttParser.DatasContext,i)


        def indices(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.IndicesContext)
            else:
                return self.getTypedRuleContext(ttParser.IndicesContext,i)


        def tendencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.TendenciaContext)
            else:
                return self.getTypedRuleContext(ttParser.TendenciaContext,i)


        def bolsa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.BolsaContext)
            else:
                return self.getTypedRuleContext(ttParser.BolsaContext,i)


        def operacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.OperacaoContext)
            else:
                return self.getTypedRuleContext(ttParser.OperacaoContext,i)


        def renda(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ttParser.RendaContext)
            else:
                return self.getTypedRuleContext(ttParser.RendaContext,i)


        def getRuleIndex(self):
            return ttParser.RULE_prog




    def prog(self):

        localctx = ttParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5, 6, 7, 8]:
                    self.state = 32
                    self.tempo()
                    pass
                elif token in [9, 10]:
                    self.state = 33
                    self.tipo_investimento()
                    pass
                elif token in [17, 18]:
                    self.state = 34
                    self.ativo()
                    pass
                elif token in [24, 28]:
                    self.state = 35
                    self.monetario()
                    pass
                elif token in [35]:
                    self.state = 36
                    self.palavra()
                    pass
                elif token in [38]:
                    self.state = 37
                    self.match(ttParser.HASHTAGS)
                    pass
                elif token in [19, 21, 22, 23]:
                    self.state = 38
                    self.numeros()
                    pass
                elif token in [31, 33, 34]:
                    self.state = 39
                    self.char()
                    pass
                elif token in [37]:
                    self.state = 40
                    self.match(ttParser.MENCOES)
                    pass
                elif token in [1, 2]:
                    self.state = 41
                    self.datas()
                    pass
                elif token in [11]:
                    self.state = 42
                    self.indices()
                    pass
                elif token in [14]:
                    self.state = 43
                    self.tendencia()
                    pass
                elif token in [12]:
                    self.state = 44
                    self.bolsa()
                    pass
                elif token in [13]:
                    self.state = 45
                    self.operacao()
                    pass
                elif token in [29, 30]:
                    self.state = 46
                    self.renda()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 476505341950) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_COM_BARRA(self):
            return self.getToken(ttParser.DATA_COM_BARRA, 0)

        def DIA_SEMANA(self):
            return self.getToken(ttParser.DIA_SEMANA, 0)

        def getRuleIndex(self):
            return ttParser.RULE_datas




    def datas(self):

        localctx = ttParser.DatasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_datas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TempoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TURNO(self):
            return self.getToken(ttParser.TURNO, 0)

        def horas(self):
            return self.getTypedRuleContext(ttParser.HorasContext,0)


        def DIA_TEMPO(self):
            return self.getToken(ttParser.DIA_TEMPO, 0)

        def MEDIDA_TEMPO(self):
            return self.getToken(ttParser.MEDIDA_TEMPO, 0)

        def MES(self):
            return self.getToken(ttParser.MES, 0)

        def getRuleIndex(self):
            return ttParser.RULE_tempo




    def tempo(self):

        localctx = ttParser.TempoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tempo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 53
                self.match(ttParser.TURNO)
                pass
            elif token in [7, 8]:
                self.state = 54
                self.horas()
                pass
            elif token in [4]:
                self.state = 55
                self.match(ttParser.DIA_TEMPO)
                pass
            elif token in [5]:
                self.state = 56
                self.match(ttParser.MEDIDA_TEMPO)
                pass
            elif token in [6]:
                self.state = 57
                self.match(ttParser.MES)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HorasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HORA_FORMATADA(self):
            return self.getToken(ttParser.HORA_FORMATADA, 0)

        def HORA_EXTENSO(self):
            return self.getToken(ttParser.HORA_EXTENSO, 0)

        def getRuleIndex(self):
            return ttParser.RULE_horas




    def horas(self):

        localctx = ttParser.HorasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_horas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_investimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RENDA_FIXA(self):
            return self.getToken(ttParser.RENDA_FIXA, 0)

        def RENDA_VARIAVEL(self):
            return self.getToken(ttParser.RENDA_VARIAVEL, 0)

        def getRuleIndex(self):
            return ttParser.RULE_tipo_investimento




    def tipo_investimento(self):

        localctx = ttParser.Tipo_investimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo_investimento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndicesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDICES(self):
            return self.getToken(ttParser.INDICES, 0)

        def getRuleIndex(self):
            return ttParser.RULE_indices




    def indices(self):

        localctx = ttParser.IndicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_indices)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ttParser.INDICES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BolsaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOLSA(self):
            return self.getToken(ttParser.BOLSA, 0)

        def getRuleIndex(self):
            return ttParser.RULE_bolsa




    def bolsa(self):

        localctx = ttParser.BolsaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bolsa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ttParser.BOLSA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERACAO(self):
            return self.getToken(ttParser.OPERACAO, 0)

        def getRuleIndex(self):
            return ttParser.RULE_operacao




    def operacao(self):

        localctx = ttParser.OperacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ttParser.OPERACAO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TendenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TENDENCIA(self):
            return self.getToken(ttParser.TENDENCIA, 0)

        def getRuleIndex(self):
            return ttParser.RULE_tendencia




    def tendencia(self):

        localctx = ttParser.TendenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tendencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ttParser.TENDENCIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACAO(self):
            return self.getToken(ttParser.ACAO, 0)

        def FII(self):
            return self.getToken(ttParser.FII, 0)

        def getRuleIndex(self):
            return ttParser.RULE_ativo




    def ativo(self):

        localctx = ttParser.AtivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ativo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantidadeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(ttParser.NUMERO, 0)

        def SIMBOLO_QUANTIDADE(self):
            return self.getToken(ttParser.SIMBOLO_QUANTIDADE, 0)

        def FRACAO(self):
            return self.getToken(ttParser.FRACAO, 0)

        def getRuleIndex(self):
            return ttParser.RULE_quantidade




    def quantidade(self):

        localctx = ttParser.QuantidadeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_quantidade)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(ttParser.NUMERO)
                self.state = 75
                self.match(ttParser.SIMBOLO_QUANTIDADE)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(ttParser.FRACAO)
                self.state = 77
                self.match(ttParser.SIMBOLO_QUANTIDADE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PORCENTAGEM(self):
            return self.getToken(ttParser.PORCENTAGEM, 0)

        def FRACAO(self):
            return self.getToken(ttParser.FRACAO, 0)

        def quantidade(self):
            return self.getTypedRuleContext(ttParser.QuantidadeContext,0)


        def NUMERO(self):
            return self.getToken(ttParser.NUMERO, 0)

        def ORDINAL(self):
            return self.getToken(ttParser.ORDINAL, 0)

        def getRuleIndex(self):
            return ttParser.RULE_numeros




    def numeros(self):

        localctx = ttParser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_numeros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 80
                self.match(ttParser.PORCENTAGEM)
                pass

            elif la_ == 2:
                self.state = 81
                self.match(ttParser.FRACAO)
                pass

            elif la_ == 3:
                self.state = 82
                self.quantidade()
                pass

            elif la_ == 4:
                self.state = 83
                self.match(ttParser.NUMERO)
                pass

            elif la_ == 5:
                self.state = 84
                self.match(ttParser.ORDINAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonetarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALOR_MONETARIO(self):
            return self.getToken(ttParser.VALOR_MONETARIO, 0)

        def MOEDA(self):
            return self.getToken(ttParser.MOEDA, 0)

        def getRuleIndex(self):
            return ttParser.RULE_monetario




    def monetario(self):

        localctx = ttParser.MonetarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_monetario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==24 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RendaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIVIDENDO(self):
            return self.getToken(ttParser.DIVIDENDO, 0)

        def JCP(self):
            return self.getToken(ttParser.JCP, 0)

        def getRuleIndex(self):
            return ttParser.RULE_renda




    def renda(self):

        localctx = ttParser.RendaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_renda)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PONTUACAO(self):
            return self.getToken(ttParser.PONTUACAO, 0)

        def OUTROS_CHARS(self):
            return self.getToken(ttParser.OUTROS_CHARS, 0)

        def EMOJI(self):
            return self.getToken(ttParser.EMOJI, 0)

        def getRuleIndex(self):
            return ttParser.RULE_char




    def char(self):

        localctx = ttParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_char)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 27917287424) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PalavraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALAVRA(self):
            return self.getToken(ttParser.PALAVRA, 0)

        def getRuleIndex(self):
            return ttParser.RULE_palavra




    def palavra(self):

        localctx = ttParser.PalavraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_palavra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ttParser.PALAVRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





