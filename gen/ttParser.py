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
        4,1,32,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,4,
        0,30,8,0,11,0,12,0,31,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,41,8,2,1,3,
        1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,56,8,7,1,8,1,
        8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,6,1,0,1,2,1,0,7,
        8,1,0,9,10,2,0,11,11,14,14,1,0,15,18,1,0,26,27,68,0,29,1,0,0,0,2,
        33,1,0,0,0,4,40,1,0,0,0,6,42,1,0,0,0,8,44,1,0,0,0,10,46,1,0,0,0,
        12,48,1,0,0,0,14,55,1,0,0,0,16,57,1,0,0,0,18,59,1,0,0,0,20,30,3,
        4,2,0,21,30,3,8,4,0,22,30,3,10,5,0,23,30,3,18,9,0,24,30,5,31,0,0,
        25,30,3,12,6,0,26,30,3,14,7,0,27,30,5,30,0,0,28,30,3,2,1,0,29,20,
        1,0,0,0,29,21,1,0,0,0,29,22,1,0,0,0,29,23,1,0,0,0,29,24,1,0,0,0,
        29,25,1,0,0,0,29,26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,31,1,
        0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,1,1,0,0,0,33,34,7,0,0,0,34,
        3,1,0,0,0,35,41,5,3,0,0,36,41,3,6,3,0,37,41,5,4,0,0,38,41,5,5,0,
        0,39,41,5,6,0,0,40,35,1,0,0,0,40,36,1,0,0,0,40,37,1,0,0,0,40,38,
        1,0,0,0,40,39,1,0,0,0,41,5,1,0,0,0,42,43,7,1,0,0,43,7,1,0,0,0,44,
        45,7,2,0,0,45,9,1,0,0,0,46,47,7,3,0,0,47,11,1,0,0,0,48,49,7,4,0,
        0,49,13,1,0,0,0,50,56,5,21,0,0,51,56,3,16,8,0,52,56,5,23,0,0,53,
        56,5,24,0,0,54,56,5,25,0,0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,
        0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,15,1,0,0,0,57,58,7,5,0,0,58,17,
        1,0,0,0,59,60,5,28,0,0,60,19,1,0,0,0,4,29,31,40,55
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
                      "HORA_FORMATADA", "FII_ETF", "ACAO", "VALOR_MONETARIO", 
                      "VALOR", "CIFRAO", "MOEDA", "FRACAO", "PORCENTAGEM", 
                      "QUANTIDADE", "NUMERO", "SIMBOLO_QUANTIDADE", "DIGITO", 
                      "PONTUACAO", "RET", "OUTROS_CHARS", "ASPAS", "EMOJI", 
                      "ABRE_PARENTESES", "FECHA_PARENTESES", "PALAVRA", 
                      "LETRA", "MENCOES", "HASHTAGS", "WS" ]

    RULE_prog = 0
    RULE_datas = 1
    RULE_tempo = 2
    RULE_horas = 3
    RULE_ativo = 4
    RULE_monetario = 5
    RULE_numeros = 6
    RULE_char = 7
    RULE_parenteses = 8
    RULE_palavra = 9

    ruleNames =  [ "prog", "datas", "tempo", "horas", "ativo", "monetario", 
                   "numeros", "char", "parenteses", "palavra" ]

    EOF = Token.EOF
    DATA_COM_BARRA=1
    DIA_SEMANA=2
    TURNO=3
    DIA_TEMPO=4
    MEDIDA_TEMPO=5
    MES=6
    HORA_EXTENSO=7
    HORA_FORMATADA=8
    FII_ETF=9
    ACAO=10
    VALOR_MONETARIO=11
    VALOR=12
    CIFRAO=13
    MOEDA=14
    FRACAO=15
    PORCENTAGEM=16
    QUANTIDADE=17
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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5, 6, 7, 8]:
                    self.state = 20
                    self.tempo()
                    pass
                elif token in [9, 10]:
                    self.state = 21
                    self.ativo()
                    pass
                elif token in [11, 14]:
                    self.state = 22
                    self.monetario()
                    pass
                elif token in [28]:
                    self.state = 23
                    self.palavra()
                    pass
                elif token in [31]:
                    self.state = 24
                    self.match(ttParser.HASHTAGS)
                    pass
                elif token in [15, 16, 17, 18]:
                    self.state = 25
                    self.numeros()
                    pass
                elif token in [21, 23, 24, 25, 26, 27]:
                    self.state = 26
                    self.char()
                    pass
                elif token in [30]:
                    self.state = 27
                    self.match(ttParser.MENCOES)
                    pass
                elif token in [1, 2]:
                    self.state = 28
                    self.datas()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3752316926) != 0)):
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
            self.state = 33
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 35
                self.match(ttParser.TURNO)
                pass
            elif token in [7, 8]:
                self.state = 36
                self.horas()
                pass
            elif token in [4]:
                self.state = 37
                self.match(ttParser.DIA_TEMPO)
                pass
            elif token in [5]:
                self.state = 38
                self.match(ttParser.MEDIDA_TEMPO)
                pass
            elif token in [6]:
                self.state = 39
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
            self.state = 42
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
        self.enterRule(localctx, 8, self.RULE_ativo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
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
        self.enterRule(localctx, 10, self.RULE_monetario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==11 or _la==14):
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


    class NumerosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PORCENTAGEM(self):
            return self.getToken(ttParser.PORCENTAGEM, 0)

        def NUMERO(self):
            return self.getToken(ttParser.NUMERO, 0)

        def FRACAO(self):
            return self.getToken(ttParser.FRACAO, 0)

        def QUANTIDADE(self):
            return self.getToken(ttParser.QUANTIDADE, 0)

        def getRuleIndex(self):
            return ttParser.RULE_numeros




    def numeros(self):

        localctx = ttParser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numeros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 50
                self.match(ttParser.PONTUACAO)
                pass
            elif token in [26, 27]:
                self.state = 51
                self.parenteses()
                pass
            elif token in [23]:
                self.state = 52
                self.match(ttParser.OUTROS_CHARS)
                pass
            elif token in [24]:
                self.state = 53
                self.match(ttParser.ASPAS)
                pass
            elif token in [25]:
                self.state = 54
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
        self.enterRule(localctx, 16, self.RULE_parenteses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
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
        self.enterRule(localctx, 18, self.RULE_palavra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ttParser.PALAVRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





