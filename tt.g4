grammar tt;

prog: (tempo | tipo_investimento | ativo | monetario | palavra | HASHTAGS| numeros | char | MENCOES | datas | indices | tendencia | bolsa | operacao | renda)+;

datas: (DATA_COM_BARRA | DIA_SEMANA);
    DATA_COM_BARRA: (DIGITO DIGITO'/'DIGITO DIGITO'/'DIGITO DIGITO DIGITO DIGITO | (DIGITO DIGITO'/'DIGITO DIGITO));
    DIA_SEMANA: [Ss]'egunda'[-]?'feira'|
                [Tt]'erça'[-]?'feira'|
                [Qq]'uarta'[-]?'feira'|
                [Qq]'uinta'[-]?'feira'|
                [Ss]'exta'[-]?'feira'|
                [Ss][aá]'bado'|
                [Dd]'omingo';

tempo: (TURNO | horas | DIA_TEMPO | MEDIDA_TEMPO | MES);
    TURNO: 'manhã' | 'tarde' | 'noite' | 'madrugada';
    DIA_TEMPO: 'ontem' | 'hoje' | 'amanh'[aã] | 'anteontem' | 'dia';
    MEDIDA_TEMPO: 'min' | 'hora'[s]? | 'h' | 'ano'[s]? | 'mês'| 'meses' | 'semana'[sl]? | ('bi'|'se'|'tri')'mestr'('al'|'e') | 'anual';
    MES: [Jj]'an''eiro'? | 'JANEIRO' |
         [Ff]'ev''ereiro'? | 'FEVEIRO' |
         [Mm]'arço' | 'MARÇO' |
         [Aa]'bril' | 'ABRIL' |
         [Mm]'ai''o'? | 'MAIO' |
         [Jj]'un''ho'? | 'JUNHO' |
         [Jj]'ul''ho'? | 'JULHO' |
         [Aa]'go''sto'? | 'AGOSTO' |
         [Ss]'et''embro'? | 'SETEMBRO' |
         [Oo]'ut''ubro'? | 'OUTUBRO' |
         [Nn]'ov''embro'? | 'NOVEMBRO' |
         [Dd]'ezembro' | 'DEZEMBRO';

horas: (HORA_FORMATADA | HORA_EXTENSO);
    HORA_EXTENSO:WS DIGITO DIGITO WS'da'WS TURNO;
    HORA_FORMATADA: DIGITO DIGITO[hH];

tipo_investimento: (RENDA_FIXA | RENDA_VARIAVEL);
    RENDA_FIXA: [Pp]'oupan'[cç]'a' | [Tt]'esouro' WS [Dd]'ireto' | ([Tt]'esouro' WS)? ('SELIC' | [Ss]'elic') | ([Tt]'esouro' WS)? ('IPCA' | [Ii]'pca') | 'CDB' | 'LCI' | 'LCA' | 'CRI' | 'CRA' | 'LC' | [Dd]'eb'[eê]'ntures' | 'LF';
    RENDA_VARIAVEL: [Aa][cç]([oõ]'es' | [aã]'o') | 'BDR''s'? | [Ff]'undo''s'? WS 'de' WS 'investimento''s'? | [Ff]'undo''s'? WS 'imobili'[aá]'rio''s'? | ('FII' | 'fii' )'s'? | 'ETF''s'? | [Ff]'iagro' | [Cc]'ripto''s'? | [Bb]'itcoin'
    | 'Fi-infra' | 'fip-ie';

indices: (INDICES);
    INDICES: [Ii]('bov'|'BOV')('espa'|'ESPA')? | [Ii]('fix'|'FIX') | [Ss]'mall11' | ('ivvb11'|'IVVB11');

bolsa: (BOLSA);
    BOLSA: ([Bb]'3' | 'NASDAQ' | 'nasdaq' | 'NYSE' | 'nyse');

operacao: (OPERACAO);
    OPERACAO: ([Cc]'all' | 'CALL' | [Pp]'ut' | 'PUT');

tendencia: (TENDENCIA);
    TENDENCIA: (ALTO|BAIXO);
    ALTO: ('alta'|'crescimento'|'subi'([ru]|'da')|'sobe');
    BAIXO: ('baixa'|'queda'|'desc'('e'[ru]|'ida')|'cai'[u]?);

ativo: (ACAO | FII);
    FII: LETRA LETRA LETRA LETRA'11';
    ACAO: LETRA LETRA LETRA LETRA[3-9];

monetario: (VALOR_MONETARIO | MOEDA);
    VALOR_MONETARIO: (SIMBOLO_MOEDA WS* VALOR ((WS* SIMBOLO_QUANTIDADE)|(WS* 'de'WS*MOEDA))*|VALOR ((WS* SIMBOLO_QUANTIDADE)|(WS* 'de'WS*MOEDA))+);
    SIMBOLO_MOEDA: [Rr]?'$'|[Uu][Ss]'$';
    VALOR: ([1-9]DIGITO*(('.'DIGITO DIGITO DIGITO)|','DIGITO+)*);
    DIGITO: [0-9];
    MOEDA: ('real'|'reais'|'d'[oó]'lar''es'?|'dol');

renda: (DIVIDENDO | JCP);
DIVIDENDO: ([Dd]'ividendo'[s]?);
JCP: ('JCP' | [Jj]'uro'[s]? WS [Ss]'obre' WS [Cc]'apital' WS [Pp]'r'[oó]'prio');

numeros: (PORCENTAGEM | FRACAO | quantidade | NUMERO | ORDINAL);
    FRACAO: DIGITO+'.'|','DIGITO+;
    PORCENTAGEM: [-+]?FRACAO'%'|[-+]?DIGITO+'%';
    ORDINAL: DIGITO+[ºª];

quantidade: (NUMERO SIMBOLO_QUANTIDADE) | (FRACAO SIMBOLO_QUANTIDADE);
    NUMERO: DIGITO+;
    SIMBOLO_QUANTIDADE: '[bm]ilhao'|'[bm]ilh'[oõ]'es'|'mil'|'k'|'m'|'bi ';

char: (PONTUACAO | OUTROS_CHARS| EMOJI);
    PONTUACAO: [.:;?!,] | RET;
    RET: '...';
    OUTROS_CHARS: [/{}=\-|'"()];
    EMOJI: [\p{Emoji}\uFE0F]+; // \uFE0F (Variation Selector-16) character is often used in combination with other emoji characters to indicate a specific visual presentation style

palavra: (PALAVRA);
    PALAVRA: LETRA+;


//SITE: (('http'[s]?'://')|'w'{3};
LETRA: [A-Za-zÁáÂâÃãÀàÉéÊêÍíÓóÔôÕõÚúÜüÇç];
MENCOES: '@'[a-zA-Z0-9_]+;
HASHTAGS: '#'[a-zA-Z0-9]+;
WS: [ \t\f\r\n] -> skip;