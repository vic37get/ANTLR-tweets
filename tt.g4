grammar tt;

prog: (tempo | tipo_investimento | ativo | monetario | palavra | HASHTAGS| numeros | char | MENCOES | datas)+;

datas: (DATA_COM_BARRA | DIA_SEMANA);
    DATA_COM_BARRA: (DIGITO DIGITO'/'DIGITO DIGITO'/'DIGITO DIGITO DIGITO DIGITO);
    DIA_SEMANA: [Ss]'egunda'[-]?'feira'|
                [Tt]'erça'[-]?'feira'|
                [Qq]'uarta'[-]?'feira'|
                [Qq]'uinta'[-]?'feira'|
                [Ss]'exta'[-]?'feira'|
                [Ss][aá]'bado'|
                [Dd]'omingo';

tempo: (TURNO | horas | DIA_TEMPO | MEDIDA_TEMPO | MES);
    TURNO: 'manhã' | 'tarde' | 'noite' | 'madrugada';
    DIA_TEMPO: 'ontem' | 'hoje' | 'amanh'[aã] | 'anteontem';
    MEDIDA_TEMPO: 'min' | 'hora' | 'h' | 'ano'[s]? | 'mês'| 'meses';
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

ativo: (ACAO | FII);
    FII: LETRA LETRA LETRA LETRA'11';
    ACAO: LETRA LETRA LETRA LETRA[3-9];

monetario: (VALOR_MONETARIO | MOEDA);
    //valor_monetario: (SIMBOLO_MOEDA FRACAO SIMBOLO_QUANTIDADE?) | (SIMBOLO_MOEDA NUMERO SIMBOLO_QUANTIDADE?) ;
    VALOR_MONETARIO: (SIMBOLO_MOEDA VALOR SIMBOLO_QUANTIDADE) | (VALOR SIMBOLO_QUANTIDADE MOEDA) ;
    //VALOR: (([0-9]{1,3}[,][0-9]{2})|((([0-9]){1,3}[.])+));
    VALOR: (([1-9]DIGITO{0,2}('.'DIGITO{3})*)|(([1-9]'.'DIGITO*)?DIGITO))(','NUMERO)? | NUMERO;
    SIMBOLO_MOEDA: [Rr]'$'|'$';
    MOEDA: 'real' | 'reais' | 'd'[oó]'lar''es'?|'dol';

    numeros: (PORCENTAGEM | FRACAO | quantidade | NUMERO);
    FRACAO: DIGITO+'.'|','DIGITO+;
    PORCENTAGEM: [-+]?FRACAO'%'|[-+]?DIGITO+'%';
    quantidade: (NUMERO SIMBOLO_QUANTIDADE) | (FRACAO SIMBOLO_QUANTIDADE);
    NUMERO: DIGITO+;
    SIMBOLO_QUANTIDADE: '[bm]ilhao'|'[bm]ilhoes'|'mil'|'k'|'m'|'bi';
    DIGITO: [0-9];

char: (PONTUACAO | parenteses | OUTROS_CHARS | ASPAS | EMOJI);
    PONTUACAO: [.:;?!,] | RET;
    RET: '...';
    OUTROS_CHARS: [/{}=\-|];
    ASPAS: ['"];
    EMOJI: [\p{Emoji}\uFE0F]+; // \uFE0F (Variation Selector-16) character is often used in combination with other emoji characters to indicate a specific visual presentation style

parenteses: (ABRE_PARENTESES | FECHA_PARENTESES);
    ABRE_PARENTESES: '(';
    FECHA_PARENTESES: ')';

palavra: (PALAVRA);
    PALAVRA: LETRA+;


//SITE: (('http'[s]?'://')|'w'{3};
LETRA: [A-Za-zÁáÂâÃãÀàÉéÊêÍíÓóÔôÕõÚúÜüÇç];
MENCOES: '@'[a-zA-Z0-9_]+;
HASHTAGS: '#'[a-zA-Z0-9]+;
WS: [ \t\f\r\n] -> skip;