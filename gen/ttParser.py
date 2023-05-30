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
        4,1,37,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,4,0,41,8,0,11,0,
        12,0,42,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,4,1,4,1,
        5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,70,8,9,1,10,1,
        10,1,10,1,10,3,10,76,8,10,1,11,1,11,1,11,1,11,1,11,3,11,83,8,11,
        1,12,1,12,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,5,1,0,1,2,1,0,7,8,1,0,9,10,1,0,15,16,1,0,31,32,98,0,40,1,0,
        0,0,2,44,1,0,0,0,4,51,1,0,0,0,6,53,1,0,0,0,8,55,1,0,0,0,10,57,1,
        0,0,0,12,59,1,0,0,0,14,61,1,0,0,0,16,63,1,0,0,0,18,69,1,0,0,0,20,
        75,1,0,0,0,22,82,1,0,0,0,24,84,1,0,0,0,26,86,1,0,0,0,28,41,3,4,2,
        0,29,41,3,8,4,0,30,41,3,14,7,0,31,41,3,16,8,0,32,41,3,26,13,0,33,
        41,5,36,0,0,34,41,3,18,9,0,35,41,3,22,11,0,36,41,5,35,0,0,37,41,
        3,2,1,0,38,41,3,10,5,0,39,41,3,12,6,0,40,28,1,0,0,0,40,29,1,0,0,
        0,40,30,1,0,0,0,40,31,1,0,0,0,40,32,1,0,0,0,40,33,1,0,0,0,40,34,
        1,0,0,0,40,35,1,0,0,0,40,36,1,0,0,0,40,37,1,0,0,0,40,38,1,0,0,0,
        40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,1,1,0,
        0,0,44,45,7,0,0,0,45,3,1,0,0,0,46,52,5,3,0,0,47,52,3,6,3,0,48,52,
        5,4,0,0,49,52,5,5,0,0,50,52,5,6,0,0,51,46,1,0,0,0,51,47,1,0,0,0,
        51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,54,7,1,
        0,0,54,7,1,0,0,0,55,56,7,2,0,0,56,9,1,0,0,0,57,58,5,11,0,0,58,11,
        1,0,0,0,59,60,5,12,0,0,60,13,1,0,0,0,61,62,7,3,0,0,62,15,1,0,0,0,
        63,64,5,17,0,0,64,17,1,0,0,0,65,70,5,23,0,0,66,70,5,22,0,0,67,70,
        3,20,10,0,68,70,5,24,0,0,69,65,1,0,0,0,69,66,1,0,0,0,69,67,1,0,0,
        0,69,68,1,0,0,0,70,19,1,0,0,0,71,72,5,24,0,0,72,76,5,25,0,0,73,74,
        5,22,0,0,74,76,5,25,0,0,75,71,1,0,0,0,75,73,1,0,0,0,76,21,1,0,0,
        0,77,83,5,26,0,0,78,83,3,24,12,0,79,83,5,28,0,0,80,83,5,29,0,0,81,
        83,5,30,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,
        0,0,82,81,1,0,0,0,83,23,1,0,0,0,84,85,7,4,0,0,85,25,1,0,0,0,86,87,
        5,33,0,0,87,27,1,0,0,0,6,40,42,51,69,75,82
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "'...'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "DATA_COM_BARRA", "DIA_SEMANA", "TURNO", 
                      "DIA_TEMPO", "MEDIDA_TEMPO", "MES", "HORA_EXTENSO", 
                      "HORA_FORMATADA", "RENDA_FIXA", "RENDA_VARIAVEL", 
                      "INDICES", "TENDENCIA", "ALTO", "BAIXO", "FII", "ACAO", 
                      "VALOR_MONETARIO", "SIMBOLO_MOEDA", "VALOR", "DIGITO", 
                      "MOEDA", "FRACAO", "PORCENTAGEM", "NUMERO", "SIMBOLO_QUANTIDADE", 
                      "PONTUACAO", "RET", "OUTROS_CHARS", "ASPAS", "EMOJI", 
                      "ABRE_PARENTESES", "FECHA_PARENTESES", "PALAVRA", 
                      "LETRA", "MENCOES", "HASHTAGS", "WS" ]

    RULE_prog = 0
    RULE_datas = 1
    RULE_tempo = 2
    RULE_horas = 3
    RULE_tipo_investimento = 4
    RULE_indices = 5
    RULE_tendencia = 6
    RULE_ativo = 7
    RULE_monetario = 8
    RULE_numeros = 9
    RULE_quantidade = 10
    RULE_char = 11
    RULE_parenteses = 12
    RULE_palavra = 13

    ruleNames =  [ "prog", "datas", "tempo", "horas", "tipo_investimento", 
                   "indices", "tendencia", "ativo", "monetario", "numeros", 
                   "quantidade", "char", "parenteses", "palavra" ]

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
    TENDENCIA=12
    ALTO=13
    BAIXO=14
    FII=15
    ACAO=16
    VALOR_MONETARIO=17
    SIMBOLO_MOEDA=18
    VALOR=19
    DIGITO=20
    MOEDA=21
    FRACAO=22
    PORCENTAGEM=23
    NUMERO=24
    SIMBOLO_QUANTIDADE=25
    PONTUACAO=26
    RET=27
    OUTROS_CHARS=28
    ASPAS=29
    EMOJI=30
    ABRE_PARENTESES=31
    FECHA_PARENTESES=32
    PALAVRA=33
    LETRA=34
    MENCOES=35
    HASHTAGS=36
    WS=37

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


        def getRuleIndex(self):
            return ttParser.RULE_prog




    def prog(self):

        localctx = ttParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5, 6, 7, 8]:
                    self.state = 28
                    self.tempo()
                    pass
                elif token in [9, 10]:
                    self.state = 29
                    self.tipo_investimento()
                    pass
                elif token in [15, 16]:
                    self.state = 30
                    self.ativo()
                    pass
                elif token in [17]:
                    self.state = 31
                    self.monetario()
                    pass
                elif token in [33]:
                    self.state = 32
                    self.palavra()
                    pass
                elif token in [36]:
                    self.state = 33
                    self.match(ttParser.HASHTAGS)
                    pass
                elif token in [22, 23, 24]:
                    self.state = 34
                    self.numeros()
                    pass
                elif token in [26, 28, 29, 30, 31, 32]:
                    self.state = 35
                    self.char()
                    pass
                elif token in [35]:
                    self.state = 36
                    self.match(ttParser.MENCOES)
                    pass
                elif token in [1, 2]:
                    self.state = 37
                    self.datas()
                    pass
                elif token in [11]:
                    self.state = 38
                    self.indices()
                    pass
                elif token in [12]:
                    self.state = 39
                    self.tendencia()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 120087355390) != 0):
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
            self.state = 44
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 46
                self.match(ttParser.TURNO)
                pass
            elif token in [7, 8]:
                self.state = 47
                self.horas()
                pass
            elif token in [4]:
                self.state = 48
                self.match(ttParser.DIA_TEMPO)
                pass
            elif token in [5]:
                self.state = 49
                self.match(ttParser.MEDIDA_TEMPO)
                pass
            elif token in [6]:
                self.state = 50
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
            self.state = 53
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
            self.state = 55
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
            self.state = 57
            self.match(ttParser.INDICES)
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
        self.enterRule(localctx, 12, self.RULE_tendencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
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
        self.enterRule(localctx, 14, self.RULE_ativo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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


    class MonetarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALOR_MONETARIO(self):
            return self.getToken(ttParser.VALOR_MONETARIO, 0)

        def getRuleIndex(self):
            return ttParser.RULE_monetario




    def monetario(self):

        localctx = ttParser.MonetarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_monetario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ttParser.VALOR_MONETARIO)
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

        def getRuleIndex(self):
            return ttParser.RULE_numeros




    def numeros(self):

        localctx = ttParser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numeros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 65
                self.match(ttParser.PORCENTAGEM)
                pass

            elif la_ == 2:
                self.state = 66
                self.match(ttParser.FRACAO)
                pass

            elif la_ == 3:
                self.state = 67
                self.quantidade()
                pass

            elif la_ == 4:
                self.state = 68
                self.match(ttParser.NUMERO)
                pass


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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(ttParser.NUMERO)
                self.state = 72
                self.match(ttParser.SIMBOLO_QUANTIDADE)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(ttParser.FRACAO)
                self.state = 74
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


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PONTUACAO(self):
            return self.getToken(ttParser.PONTUACAO, 0)

        def parenteses(self):
            return self.getTypedRuleContext(ttParser.ParentesesContext,0)


        def OUTROS_CHARS(self):
            return self.getToken(ttParser.OUTROS_CHARS, 0)

        def ASPAS(self):
            return self.getToken(ttParser.ASPAS, 0)

        def EMOJI(self):
            return self.getToken(ttParser.EMOJI, 0)

        def getRuleIndex(self):
            return ttParser.RULE_char




    def char(self):

        localctx = ttParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 77
                self.match(ttParser.PONTUACAO)
                pass
            elif token in [31, 32]:
                self.state = 78
                self.parenteses()
                pass
            elif token in [28]:
                self.state = 79
                self.match(ttParser.OUTROS_CHARS)
                pass
            elif token in [29]:
                self.state = 80
                self.match(ttParser.ASPAS)
                pass
            elif token in [30]:
                self.state = 81
                self.match(ttParser.EMOJI)
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


    class ParentesesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_PARENTESES(self):
            return self.getToken(ttParser.ABRE_PARENTESES, 0)

        def FECHA_PARENTESES(self):
            return self.getToken(ttParser.FECHA_PARENTESES, 0)

        def getRuleIndex(self):
            return ttParser.RULE_parenteses




    def parenteses(self):

        localctx = ttParser.ParentesesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parenteses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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
        self.enterRule(localctx, 26, self.RULE_palavra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ttParser.PALAVRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





