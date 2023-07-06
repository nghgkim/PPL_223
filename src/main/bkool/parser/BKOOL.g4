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
not_void_type: INT | FLOAT | BOOLEAN | STRING;
void_type: VOID;
prim_type: not_void_type | void_type;

// ARRAY TYPE
arr_type: not_void_type LSB INT_LIT RSB;

// CLASS TYPE

// 5. EXPRESSION
expr: expr1 (LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL) expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;
expr4: expr4 (MULOP | FLOAT_DIV | INTEGER_DIV | MOD) expr5 | expr5;
expr5: expr5 (CONCATENATION) expr6 | expr6;
expr6: NOT expr6 | expr7;
expr7: expr8 (ADDOP | SUBOP) expr7 | expr8;
expr8: expr9 LSB expr RSB | expr9;
expr9: expr9 DOT ID (LB exprlist? RB)? | ID DOT ID (LB exprlist? RB)?;
expr10: NEW ID LB exprlist? RB; 

exprlist: expr COMMA exprlist | expr COMMA;

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
STR_LIT: '"' CHAR* '"' {
	self.text = self.text[:];
};
arr_lit: LP arr_decl RP;
arr_decl: arr_val COMMA arr_decl | arr_val;
arr_val: (INT_LIT | bool_lit | FLOAT_LIT | STR_LIT);

// 6. STATEMENT

// 7. SCOPE

// 8. IO

// EXTRA: FRAGMENT
fragment UNDERSCORE: '_';
fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment DECIMAL: DOT DIGIT*;
fragment EXPONENT: [eE] (ADDOP | SUBOP)? DIGIT+;
fragment CHAR: ESC_SEQ | ~[\b\f\r\n\t"\\];
fragment ESC_SEQ: '\\' [bfrnt"\\];

// IDENTIFIER
ID: (UNDERSCORE | LETTER) (UNDERSCORE | LETTER | DIGIT)*;

/******************* Lexical Error *********************/


/*******************************************************/
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;