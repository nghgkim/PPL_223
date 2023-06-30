// ID: 2111617

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: ;

// 2. PROGRAM STRUCTURE
// CLASS DECLARATION

// ATTRIBUTE DECLARATION

// METHOD DECLARATION

// 4. TYPE
// PRIMITIVE TYPE

// ARRAY TYPE

// CLASS TYPE

// 3. LEXICAL STRUCTURE
// COMMENT
LINE_CMT: '#' ~[\r\n]* ('\r'? '\n' | EOF) -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

// KEYWORD
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

// OPERATOR
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
FLOAT_DIV: '/';
INTEGER_DIV: '\\';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LESS: '<';
GREATER: '>';
LESS_OR_EQUAL: '<=';
GREATER_OR_EQUAL: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
ASSIGN: ':=';

// SEPARATOR
LSB: '[';
RSB: ']';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
SEMI_COLONE: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

// LITERAL
INT_LIT: DIGIT+;
bool_lit: TRUE | FALSE;
FLOAT_LIT: 
		DIGIT+ DECIMAL
		| DIGIT+ EXPONENT
		| DIGIT+ DECIMAL EXPONENT;
STR_LIT: '"' CHAR* '"';

// 5. EXPRESSION

// 6. STATEMENT

// 7. SCOPE

// 8. IO

// EXTRA: FRAGMENT
fragment UNDERSCORE: '_';
fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment DECIMAL: DOT DIGIT*;
fragment EXPONENT: [eE] (ADDOP | SUBOP)? DIGIT+;
fragment CHAR: ~;
fragment SPECIAL_CHAR: '\\' [bfrnt"\\];

// IDENTIFIER
ID: (UNDERSCORE | LETTER) (UNDERSCORE | LETTER | DIGIT)*;

/******************* Lexical Error *********************/


/*******************************************************/
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;