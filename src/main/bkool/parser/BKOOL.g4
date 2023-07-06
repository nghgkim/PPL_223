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
class_decl: CLASS ID (EXTENDS ID)? LP member* RP;
member: attribute_decl | method_decl;

// ATTRIBUTE DECLARATION
attribute_decl: (STATIC | FINAL | STATIC FINAL | FINAL STATIC)? var_decl;
var_decl: (immutable_attribute | mutable_attribute) SEMI;
immutable_attribute: data_type attribute;
mutable_attribute: data_type attribute;
attribute: idlist;
idlist: (ID (EQUAL expr)?) COMMA idlist | ID (EQUAL expr)?;
// METHOD DECLARATION
method_decl: (STATIC? (data_type | void_type) ID LB paralist RB block_stmt) | (ID paralist block_stmt);
paralist: para_decl SEMI paralist | ;
para_decl: idlist;

// 4. TYPE
data_type: not_void_type | arr_type | class_type;
// PRIMITIVE TYPE
not_void_type: INT | FLOAT | BOOLEAN | STRING;
void_type: VOID;

// ARRAY TYPE
arr_type: not_void_type LSB INT_LIT RSB;

// CLASS TYPE
class_type: ID;

// 5. EXPRESSION
expr: expr1 (LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL) expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;
expr4: expr4 (MULOP | FLOAT_DIV | INTEGER_DIV | MOD) expr5 | expr5;
expr5: expr5 (CONCATENATION) expr6 | expr6;
expr6: NOT expr6 | expr7;
expr7: (ADDOP | SUBOP) expr7 | expr8;
expr8: expr9 LSB expr RSB | expr9;
expr9: expr9 DOT ID (LB exprlist? RB)? | ID DOT ID (LB exprlist? RB)?;
expr10: NEW ID LB exprlist? RB expr10?;
expr11: LB expr RB | ID | literal | THIS | NIL;

exprlist: expr COMMA exprlist | expr COMMA;

// 6. STATEMENT
stmt: block_stmt | assignment_decl;
block_stmt: LP mem_stmt? RP;
mem_stmt: (FINAL? var_decl)* stmt*;
assignment_decl: (ID | expr8) ASSIGN expr SEMI;

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
SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

// LITERAL
literal: INT_LIT | BOOL_LIT | FLOAT_LIT | STR_LIT | arr_lit;
INT_LIT: DIGIT+;
BOOL_LIT: TRUE | FALSE;
FLOAT_LIT: 
		DIGIT+ DECIMAL
		| DIGIT+ EXPONENT
		| DIGIT+ DECIMAL EXPONENT;
STR_LIT: '"' CHAR* '"' {
	self.text = self.text[:];
};
arr_lit: LP arr_decl RP;
arr_decl: arr_val COMMA arr_decl | arr_val;
arr_val: (INT_LIT | BOOL_LIT | FLOAT_LIT | STR_LIT);

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