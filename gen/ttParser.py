# Generated from D:/Victor/Projetos/ANTLR-tweets\tt.g4 by ANTLR 4.12.0
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
        4,1,32,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,4,0,37,8,0,11,0,12,0,38,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,3,
        6,58,8,6,1,7,1,7,1,7,3,7,63,8,7,1,7,1,7,1,7,3,7,68,8,7,1,8,1,8,1,
        8,1,8,3,8,74,8,8,1,9,1,9,1,9,1,9,3,9,80,8,9,1,10,1,10,1,10,1,10,
        1,10,3,10,87,8,10,1,11,1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,
        14,16,18,20,22,24,0,5,1,0,1,2,1,0,7,8,1,0,9,10,1,0,11,12,1,0,26,
        27,104,0,36,1,0,0,0,2,40,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,8,51,
        1,0,0,0,10,53,1,0,0,0,12,57,1,0,0,0,14,67,1,0,0,0,16,73,1,0,0,0,
        18,79,1,0,0,0,20,86,1,0,0,0,22,88,1,0,0,0,24,90,1,0,0,0,26,37,3,
        4,2,0,27,37,3,8,4,0,28,37,3,10,5,0,29,37,3,12,6,0,30,37,3,24,12,
        0,31,37,5,31,0,0,32,37,3,16,8,0,33,37,3,20,10,0,34,37,5,30,0,0,35,
        37,3,2,1,0,36,26,1,0,0,0,36,27,1,0,0,0,36,28,1,0,0,0,36,29,1,0,0,
        0,36,30,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,34,
        1,0,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,
        39,1,1,0,0,0,40,41,7,0,0,0,41,3,1,0,0,0,42,48,5,3,0,0,43,48,3,6,
        3,0,44,48,5,4,0,0,45,48,5,5,0,0,46,48,5,6,0,0,47,42,1,0,0,0,47,43,
        1,0,0,0,47,44,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,5,1,0,0,0,49,
        50,7,1,0,0,50,7,1,0,0,0,51,52,7,2,0,0,52,9,1,0,0,0,53,54,7,3,0,0,
        54,11,1,0,0,0,55,58,3,14,7,0,56,58,5,15,0,0,57,55,1,0,0,0,57,56,
        1,0,0,0,58,13,1,0,0,0,59,60,5,14,0,0,60,62,5,13,0,0,61,63,5,19,0,
        0,62,61,1,0,0,0,62,63,1,0,0,0,63,68,1,0,0,0,64,65,5,13,0,0,65,66,
        5,19,0,0,66,68,5,15,0,0,67,59,1,0,0,0,67,64,1,0,0,0,68,15,1,0,0,
        0,69,74,5,17,0,0,70,74,5,16,0,0,71,74,3,18,9,0,72,74,5,18,0,0,73,
        69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,17,1,0,0,
        0,75,76,5,18,0,0,76,80,5,19,0,0,77,78,5,16,0,0,78,80,5,19,0,0,79,
        75,1,0,0,0,79,77,1,0,0,0,80,19,1,0,0,0,81,87,5,21,0,0,82,87,3,22,
        11,0,83,87,5,23,0,0,84,87,5,24,0,0,85,87,5,25,0,0,86,81,1,0,0,0,
        86,82,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,86,85,1,0,0,0,87,21,1,
        0,0,0,88,89,7,4,0,0,89,23,1,0,0,0,90,91,5,28,0,0,91,25,1,0,0,0,9,
        36,38,47,57,62,67,73,79,86
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
                     "<INVALID>", "<INVALID>", "'...'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "DATA_COM_BARRA", "DIA_SEMANA", "TURNO", 
                      "DIA_TEMPO", "MEDIDA_TEMPO", "MES", "HORA_EXTENSO", 
                      "HORA_FORMATADA", "RENDA_FIXA", "RENDA_VARIAVEL", 
                      "FII_ETF", "ACAO", "VALOR", "SIMBOLO_MOEDA", "MOEDA", 
                      "FRACAO", "PORCENTAGEM", "NUMERO", "SIMBOLO_QUANTIDADE", 
                      "DIGITO", "PONTUACAO", "RET", "OUTROS_CHARS", "ASPAS", 
                      "EMOJI", "ABRE_PARENTESES", "FECHA_PARENTESES", "PALAVRA", 
                      "LETRA", "MENCOES", "HASHTAGS", "WS" ]

    RULE_prog = 0
    RULE_datas = 1
    RULE_tempo = 2
    RULE_horas = 3
    RULE_tipo_investimento = 4
    RULE_ativo = 5
    RULE_monetario = 6
    RULE_valor_monetario = 7
    RULE_numeros = 8
    RULE_quantidade = 9
    RULE_char = 10
    RULE_parenteses = 11
    RULE_palavra = 12

    ruleNames =  [ "prog", "datas", "tempo", "horas", "tipo_investimento", 
                   "ativo", "monetario", "valor_monetario", "numeros", "quantidade", 
                   "char", "parenteses", "palavra" ]

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
    FII_ETF=11
    ACAO=12
    VALOR=13
    SIMBOLO_MOEDA=14
    MOEDA=15
    FRACAO=16
    PORCENTAGEM=17
    NUMERO=18
    SIMBOLO_QUANTIDADE=19
    DIGITO=20
    PONTUACAO=21
    RET=22
    OUTROS_CHARS=23
    ASPAS=24
    EMOJI=25
    ABRE_PARENTESES=26
    FECHA_PARENTESES=27
    PALAVRA=28
    LETRA=29
    MENCOES=30
    HASHTAGS=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
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


        def getRuleIndex(self):
            return ttParser.RULE_prog




    def prog(self):

        localctx = ttParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5, 6, 7, 8]:
                    self.state = 26
                    self.tempo()
                    pass
                elif token in [9, 10]:
                    self.state = 27
                    self.tipo_investimento()
                    pass
                elif token in [11, 12]:
                    self.state = 28
                    self.ativo()
                    pass
                elif token in [13, 14, 15]:
                    self.state = 29
                    self.monetario()
                    pass
                elif token in [28]:
                    self.state = 30
                    self.palavra()
                    pass
                elif token in [31]:
                    self.state = 31
                    self.match(ttParser.HASHTAGS)
                    pass
                elif token in [16, 17, 18]:
                    self.state = 32
                    self.numeros()
                    pass
                elif token in [21, 23, 24, 25, 26, 27]:
                    self.state = 33
                    self.char()
                    pass
                elif token in [30]:
                    self.state = 34
                    self.match(ttParser.MENCOES)
                    pass
                elif token in [1, 2]:
                    self.state = 35
                    self.datas()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3752329214) != 0)):
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
            self.state = 40
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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 42
                self.match(ttParser.TURNO)
                pass
            elif token in [7, 8]:
                self.state = 43
                self.horas()
                pass
            elif token in [4]:
                self.state = 44
                self.match(ttParser.DIA_TEMPO)
                pass
            elif token in [5]:
                self.state = 45
                self.match(ttParser.MEDIDA_TEMPO)
                pass
            elif token in [6]:
                self.state = 46
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
            self.state = 49
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
            self.state = 51
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


    class AtivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACAO(self):
            return self.getToken(ttParser.ACAO, 0)

        def FII_ETF(self):
            return self.getToken(ttParser.FII_ETF, 0)

        def getRuleIndex(self):
            return ttParser.RULE_ativo




    def ativo(self):

        localctx = ttParser.AtivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ativo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
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

        def valor_monetario(self):
            return self.getTypedRuleContext(ttParser.Valor_monetarioContext,0)


        def MOEDA(self):
            return self.getToken(ttParser.MOEDA, 0)

        def getRuleIndex(self):
            return ttParser.RULE_monetario




    def monetario(self):

        localctx = ttParser.MonetarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_monetario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14]:
                self.state = 55
                self.valor_monetario()
                pass
            elif token in [15]:
                self.state = 56
                self.match(ttParser.MOEDA)
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


    class Valor_monetarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMBOLO_MOEDA(self):
            return self.getToken(ttParser.SIMBOLO_MOEDA, 0)

        def VALOR(self):
            return self.getToken(ttParser.VALOR, 0)

        def SIMBOLO_QUANTIDADE(self):
            return self.getToken(ttParser.SIMBOLO_QUANTIDADE, 0)

        def MOEDA(self):
            return self.getToken(ttParser.MOEDA, 0)

        def getRuleIndex(self):
            return ttParser.RULE_valor_monetario




    def valor_monetario(self):

        localctx = ttParser.Valor_monetarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_valor_monetario)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(ttParser.SIMBOLO_MOEDA)
                self.state = 60
                self.match(ttParser.VALOR)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 61
                    self.match(ttParser.SIMBOLO_QUANTIDADE)


                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(ttParser.VALOR)
                self.state = 65
                self.match(ttParser.SIMBOLO_QUANTIDADE)
                self.state = 66
                self.match(ttParser.MOEDA)
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

        def getRuleIndex(self):
            return ttParser.RULE_numeros




    def numeros(self):

        localctx = ttParser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_numeros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 69
                self.match(ttParser.PORCENTAGEM)
                pass

            elif la_ == 2:
                self.state = 70
                self.match(ttParser.FRACAO)
                pass

            elif la_ == 3:
                self.state = 71
                self.quantidade()
                pass

            elif la_ == 4:
                self.state = 72
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
        self.enterRule(localctx, 18, self.RULE_quantidade)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(ttParser.NUMERO)
                self.state = 76
                self.match(ttParser.SIMBOLO_QUANTIDADE)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(ttParser.FRACAO)
                self.state = 78
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
        self.enterRule(localctx, 20, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 81
                self.match(ttParser.PONTUACAO)
                pass
            elif token in [26, 27]:
                self.state = 82
                self.parenteses()
                pass
            elif token in [23]:
                self.state = 83
                self.match(ttParser.OUTROS_CHARS)
                pass
            elif token in [24]:
                self.state = 84
                self.match(ttParser.ASPAS)
                pass
            elif token in [25]:
                self.state = 85
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
        self.enterRule(localctx, 22, self.RULE_parenteses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
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
        self.enterRule(localctx, 24, self.RULE_palavra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ttParser.PALAVRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





