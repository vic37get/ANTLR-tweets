grammar tt4;

prog: (monetario|palavra)+;

monetario: (VALOR_MONETARIO);
VALOR_MONETARIO: (SIMBOLO_MOEDA WS* VALOR RESTO*|VALOR RESTO+);
RESTO: ((WS* SIMBOLO_QUANTIDADE)|(WS* MOEDA));
SIMBOLO_MOEDA: [Rr]?'$'|[Uu][Ss]'$';
VALOR: ([1-9]DIGITO*(('.'DIGITO DIGITO DIGITO)|','DIGITO+)*);
DIGITO: [0-9];

SIMBOLO_QUANTIDADE: '[bm]ilhao'|'[bm]ilhoes'|'mil'|'k'|'m'|'bi';
MOEDA: 'de'WS*('real'|'reais'|'d'[oó]'lar''es'?|'dol');

palavra: (PALAVRA);
    PALAVRA: LETRA+;

LETRA: [A-Za-zÁáÂâÃãÀàÉéÊêÍíÓóÔôÕõÚúÜüÇç];

WS: [ \t\f\r\n] -> skip;