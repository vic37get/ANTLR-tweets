grammar tt;

prog: (tempo | PALAVRAS | HASHTAGS | SITE | char | MENCOES | datas | EMOJIS | numeros)+;


datas: (DATA_COM_BARRA | DIA_SEMANA);
    DATA_COM_BARRA: (DIGITO DIGITO'/'DIGITO DIGITO'/'DIGITO DIGITO DIGITO DIGITO);
    DIA_SEMANA: [Ss]'egunda'[-]?'feira'|
                [Tt]'erça'[-]?'feira'|
                [Qq]'uarta'[-]?'feira'|
                [Qq]'uinta'[-]?'feira'|
                [Ss]'exta'[-]?'feira'|
                [Ss][aá]'bado'|
                [Dd]'omingo';

tempo: (TURNO | horas | DIA_TEMPO);
    TURNO: 'manhã' | 'tarde' | 'noite' | 'madrugada';
    DIA_TEMPO: 'ontem' | 'hoje' | 'amanh'[aã] | 'anteontem';

horas: (HORA_FORMATADA | HORA_EXTENSO);
    HORA_EXTENSO:WS DIGITO DIGITO WS'da'WS TURNO;
    HORA_FORMATADA: DIGITO DIGITO[hH];

char: (PONTUACAO | parenteses | OUTROS_CHARS | ASPAS);
    PONTUACAO: [.:;?!,] | RET;
    RET: '...';
    OUTROS_CHARS: [/{}=\-|];
    ASPAS: ['"];

parenteses: (ABRE_PARENTESES | FECHA_PARENTESES);
    ABRE_PARENTESES: '(';
    FECHA_PARENTESES: ')';

numeros: (PORCENTAGEM | DIGITO | FRACAO);
    FRACAO: DIGITO+[/,.]DIGITO+;
    PORCENTAGEM: FRACAO'%'|DIGITO+'%';

SITE: (('http'[s]?'://')|'w'{3}|((':'?(?! ).)*'.com'))(?:(?! ).)*



PALAVRAS: [A-Za-zÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÂâÊêÎîÔôÛûÃãẼẽĨĩÕõŨũÇç]+;
MENCOES: '@'[a-zA-Z0-9_]+;
HASHTAGS: '#'[a-zA-Z0-9]+;
WS: [ \t\f\r\n] -> skip;
NUMEROS: DIGITO+;
DIGITO: [0-9];
EMOJIS: [\p{Emoji}\uFE0F]+; // \uFE0F (Variation Selector-16) character is often used in combination with other emoji characters to indicate a specific visual presentation style