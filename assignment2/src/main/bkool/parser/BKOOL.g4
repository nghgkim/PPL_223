// ID: 2111617

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (class_declare)+ EOF;

// 2.Program Structure

class_declare: CLASS ID ( EXTENDS ID)? LP members* RP;
members: (attribute_declare | method_declare);

// Atrribute

attribute_declare: (STATIC | FINAL | FINAL STATIC | STATIC FINAL)? var_decl;
var_decl: (immutable_attribute | mutable_attribute) SEMI;
immutable_attribute: data_type attribute;
mutable_attribute: data_type attribute;

// Method

method_declare: (STATIC) (data_type | VOID) ID LB paralist RB block_statement | (data_type | VOID)? ID LB paralist RB block_statement;

// 5.Expressions

expr: expr1 (LT | GT | LE | GE) expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 ( ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD | INT_DIV) expr5 | expr5;
expr5: expr5 (CONCATENATION) expr6 | expr6;
expr6: NOT expr6 | expr7;
expr7: (ADD | SUB) expr7 | expr8;
expr8: expr9 LSB expr RSB | expr9;
expr9: expr9 DOT ID (LB exprlist? RB)? | ID DOT ID (LB exprlist? RB)? | expr10;
expr10: NEW ID LB (exprlist)? RB expr10? | expr11;
expr11: LB expr RB | ID | literal | THIS | NIL;
exprlist: expr COMMA exprlist | expr COMMA;

// 6.Statements

statement: assignment_statement | if_statement | for_statement | break_statement | continue_statement | return_statement | method_invocation_statement | block_statement;
block_statement: LP member_block? RP;
member_block: (FINAL? var_decl)* statement+;
assignment_statement: (ID | expr8) ASSINGMENT expr SEMI;
if_statement: IF expr THEN statement (ELSE statement)?;
for_statement: FOR ID ASSINGMENT expr (TO | DOWNTO) expr DO statement;
break_statement: BREAK SEMI;
continue_statement: CONTINUE SEMI;
return_statement: RETURN expr SEMI;
member_access: (ID | expr) DOT ID LB exprlist? RB;

method_invocation_statement: member_access SEMI;

// 4.Type

data_type: type_not_void | array_type | class_type;
type_not_void: INT | FLOAT | BOOLEAN | STRING;
array_type: type_not_void LSB INTLIT RSB;
literal: array_lit | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;
class_type: ID;

attribute: idlist;
paralist: para_decl SEMI paralist | ;
para_decl: idlist;
idlist: (ID (EQUAL expr)?) COMMA idlist | ID (EQUAL expr)?;

// 3.Lexers

// COMMENT

LINE_COMMAT: '#' ~[\r\n]* -> skip;
BLOCK_COMMAT: '/*' .*? '*/' -> skip;

// KEYWORDS

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
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

// OPERATORS

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
INT_DIV: '\\';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
NEW_OP: NEW;
ASSINGMENT: ':=';
ASSIGN: '=';

LSB: '[';
RSB: ']';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
SEMI: ';';
CL: ':';
DOT: '.';
COMMA: ',';

// LITERALS

BOOLLIT: 'true' | 'false';
STRINGLIT: '"' STR_CHAR* '"' {
    self.text = self.text[:]
};
array_lit: LP array_declare RP;
array_declare: expr array_list;
array_list: COMMA expr array_list |;
FLOATLIT: DIGIT+ DOT | DIGIT+ DOT DIGIT+ | DIGIT+ (DOT DIGIT+)? [eE] [+-]? DIGIT+ | DIGIT+ DOT [eE] [+-]? DIGIT+;
INTLIT: DIGIT+;
ID: [_a-zA-Z][_a-zA-Z0-9]*;

// FRAGMENT
fragment DIGIT: [0-9];
fragment STR_CHAR: ~[\b\t\n\f\r"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [btnfr"\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr"\\] | '\\';

WS: [ \t\r\f]+ -> skip;
NEWLINE: '\n'+ -> skip;

UNCLOSE_STRING: '"' STR_CHAR* {
    raise UncloseString(self.text[:])
};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[:])
};

ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};