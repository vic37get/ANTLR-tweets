grammar tt;

prog: (tempo | ativo | monetario | palavra | HASHTAGS| numeros | char | MENCOES | datas)+;

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
    MEDIDA_TEMPO: 'min' | 'hora' | 'h' | 'ano'[s]? | 'mes''es'?;
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

ativo: (ACAO | FII_ETF);
    FII_ETF: LETRA LETRA LETRA LETRA'11';
    ACAO: LETRA LETRA LETRA LETRA[3-9];

monetario: (VALOR_MONETARIO | MOEDA);
    VALOR_MONETARIO: (CIFRAO FRACAO) | (CIFRAO NUMERO) ;
    VALOR: (([0-9]{1,3}[,][0-9]{2})|((([0-9]){1,3}[.])+));
    CIFRAO: '[rR]$'|'$';
    MOEDA: 'dolar'|'dol';

numeros: (PORCENTAGEM | NUMERO | FRACAO | QUANTIDADE);
    FRACAO: DIGITO+[/,.]DIGITO+;
    PORCENTAGEM: [-+]?FRACAO'%'|[-+]?DIGITO+'%';
    QUANTIDADE: (NUMERO SIMBOLO_QUANTIDADE) | (FRACAO SIMBOLO_QUANTIDADE);
    NUMERO: DIGITO+;
    SIMBOLO_QUANTIDADE: '[bm]ilh[aã]o'|'[bm]ilh[oõ]es'|'mil'|'k'|'m'|'bi';
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
LETRA: [A-Za-zÇç];
MENCOES: '@'[a-zA-Z0-9_]+;
HASHTAGS: '#'[a-zA-Z0-9]+;
WS: [ \t\f\r\n] -> skip;