# Generated from C:/Users/marcelo.moraes/PycharmProjects/antilr/ANTLR-tweets\tt.g4 by ANTLR 4.12.0
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
        4,1,8,8,2,0,7,0,1,0,4,0,4,8,0,11,0,12,0,5,1,0,0,0,1,0,0,1,1,0,1,
        6,7,0,3,1,0,0,0,2,4,7,0,0,0,3,2,1,0,0,0,4,5,1,0,0,0,5,3,1,0,0,0,
        5,6,1,0,0,0,6,1,1,0,0,0,1,5
    ]

class ttParser ( Parser ):

    grammarFileName = "tt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'...'" ]

    symbolicNames = [ "<INVALID>", "DATAS", "RET", "CHARS", "PALAVRAS", 
                      "MENCOES", "HASHTAGS", "WS", "DIGITOS" ]

    RULE_prog = 0

    ruleNames =  [ "prog" ]

    EOF = Token.EOF
    DATAS=1
    RET=2
    CHARS=3
    PALAVRAS=4
    MENCOES=5
    HASHTAGS=6
    WS=7
    DIGITOS=8

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

        def PALAVRAS(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.PALAVRAS)
            else:
                return self.getToken(ttParser.PALAVRAS, i)

        def RET(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.RET)
            else:
                return self.getToken(ttParser.RET, i)

        def HASHTAGS(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.HASHTAGS)
            else:
                return self.getToken(ttParser.HASHTAGS, i)

        def CHARS(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.CHARS)
            else:
                return self.getToken(ttParser.CHARS, i)

        def MENCOES(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.MENCOES)
            else:
                return self.getToken(ttParser.MENCOES, i)

        def DATAS(self, i:int=None):
            if i is None:
                return self.getTokens(ttParser.DATAS)
            else:
                return self.getToken(ttParser.DATAS, i)

        def getRuleIndex(self):
            return ttParser.RULE_prog




    def prog(self):

        localctx = ttParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





