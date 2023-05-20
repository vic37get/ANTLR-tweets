grammar tt;

prog: (PALAVRAS | RET | HASHTAGS | CHARS | MENCOES | DATAS | EMOJIS)+;

DATAS: ('dia'WS*DIGITOS DIGITOS* | DIGITOS DIGITOS'/'[0-9][0-9]'/'[0-9][0-9][0-9][0-9]);
RET: '...';
CHARS: [.:;/?!(){}=,\-|];
PALAVRAS: [A-Za-zÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÂâÊêÎîÔôÛûÃãẼẽĨĩÕõŨũÇç]+;
MENCOES: '@'[a-zA-Z0-9]+;
HASHTAGS: '#'[a-zA-Z0-9]+;
WS: [ \t\f\r\n] -> skip;
DIGITOS: [0-9];
EMOJIS: [\p{Emoji}\uFE0F]+; // \uFE0F (Variation Selector-16) character is often used in combination with other emoji characters to indicate a specific visual presentation style

