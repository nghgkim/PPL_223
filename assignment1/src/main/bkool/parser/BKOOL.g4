grammar BKOOL;

@lexer::header {
from lexererr import *
}


program: class_decl+ EOF;

/*** Class declaration ***/
class_decl: CLASS ID (EXTENDS ID)? class_mem;
class_mem: LCB class_mem_list RCB;
class_mem_list: (class_mem_decl class_mem_list) | ;
class_mem_decl
    : method_decl
    | const_attr_decl
    | static_attr_decl
    | static_const_attr_decl
    | attr_decl
    | constructor_decl
    ;

/*** Attribute declaration ***/
attr_decl: decl_type attr_decl_list SEMI;
const_attr_decl: FINAL decl_type attr_decl_list SEMI;
static_attr_decl: STATIC decl_type attr_decl_list SEMI;
static_const_attr_decl
    : FINAL STATIC decl_type attr_decl_list SEMI
    | STATIC FINAL decl_type attr_decl_list SEMI
    ;
attr_decl_list: attr_decl_unit COMMA attr_decl_list | attr_decl_unit;
attr_decl_unit: ID (INIT expr)?;

/*** Method declaration ***/
method_decl: STATIC? class_type ID LP param_list RP block_stmt;
param_list: param_decl | ;
param_decl: param SEMI param_decl | param;
param: decl_type idlist;
idlist: ID COMMA idlist | ID;

/*** Constructor ***/
constructor_decl: ID LP param_list RP block_stmt;

class_type
    : decl_type
    | VOID
    ;

decl_type
    : primitive_type
    | array_type
    | ID
    ;

primitive_type
    : INT
    | FLOAT
    | STRING
    | BOOLEAN
    ;
array_type: (primitive_type | ID) LSB INTLIT RSB;

/*** Statement ***/
stmt
    : block_stmt
    | assign_stmt
    | if_stmt
    | for_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    | method_invocation_stmt
    ;

// Block statement
block_stmt:
    LCB
        local_var_decls?
        stmts?
    RCB;

local_var_decls: local_var_decl local_var_decls | local_var_decl;
local_var_decl: (var_decl | const_decl);
var_decl: decl_type decl_list SEMI;
const_decl: FINAL decl_type decl_list SEMI;
decl_list: decl_unit COMMA decl_list | decl_unit;
decl_unit: ID (INIT expr)?;

stmts: stmt stmts | stmt;

// Assignment statement
assign_stmt: lhs ASSIGN expr SEMI;

lhs: LP lhs RP | lhs_unit;
lhs_unit
    : ID
    | lhs_index_expr
    | lhs_member_access_expr
    ;
lhs_member_access_expr
    : expr11 bop=DOT (method_call)
    | expr11 bop=DOT (ID)
    ;
lhs_index_expr: expr10 (LSB expr RSB);

// If statement
if_stmt: if_then_stmt | if_then_else_stmt;
if_then_else_stmt: IF expr THEN stmt ELSE stmt;
if_then_stmt: IF expr THEN stmt;

// For statement
for_stmt: FOR (ID ASSIGN expr) (TO | DOWNTO) expr DO stmt;

// Break statement
break_stmt: BREAK SEMI;

// Continue statement
continue_stmt: CONTINUE SEMI;

// Return statement
return_stmt: RETURN expr SEMI;

// Method
method_invocation_stmt: expr DOT method_call SEMI;

/*** Expression ***/
expr: expr1;

expr1
    : expr2
    (   LT
    |   GT
    |   LTE
    |   GTE
    ) expr2
    | expr2
    ;

expr2
    : expr3
    (   EQUAL
    |   NE
    ) expr3
    | expr3
    ;

expr3
    : expr3
    (   AND
    |   OR
    ) expr4
    | expr4
    ;

expr4
    : expr4
    (   ADD
    |   SUB
    ) expr5
    | expr5
    ;

expr5
    : expr5
    (   MUL
    |   FLOAT_DIV
    |   INT_DIV
    |   MOD
    ) expr6
    | expr6
    ;

expr6
    : expr6
    (   CONCATENATION
    ) expr7
    | expr7
    ;

expr7
    :
    (   NOT
    ) expr7
    | expr8
    ;

expr8
    :
    (   ADD
    |   SUB
    ) expr8
    | expr9
    ;

expr9
    : expr10 LSB expr RSB
    | expr10
    ;

expr10
    : expr10 bop=DOT method_call
    | expr10 bop=DOT ID
    | expr11
    ;

expr11
    : NEW ID LP (expr_list)? RP
    | expr12
    ;

expr12
    : literal
    | ID
    | THIS
    | LP expr RP
    | NIL
    ;

method_call: ID LP (expr_list)? RP;

expr_list
    : expr COMMA expr_list
    | expr
    ;

/*** Literal ***/
literal
    : INTLIT
    | FLOATLIT
    | STRINGLIT
    | BOOLLIT
    | arrlit
    ;

arrlit: LCB literal_list RCB;

literal_list
    : literal COMMA literal_list
    | literal
    ;

/*** COMMENT ***/
COMMENT: (BLOCK_CMT | LINE_CMT) -> skip;
BLOCK_CMT: '/*' .*? ('*/' | EOF);
LINE_CMT: '#' ~([\n])* EOF?;

/*** KEYWORD ***/

// Primitive type
BOOLEAN: 'boolean';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
VOID: 'void';

// Condition keyword
IF: 'if';
THEN: 'then';
ELSE: 'else';

// Loop keyword
FOR: 'for';
TO: 'to';
DOWNTO: 'downto';
DO: 'do';
BREAK: 'break';
CONTINUE: 'continue';

// Class keyword
CLASS: 'class';
EXTENDS: 'extends';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';

fragment TRUE: 'true';
fragment FALSE: 'false';

// OTHERS
NIL: 'nil';
NEW: 'new';
RETURN: 'return';

/*** OPERATORS ***/
ADD: '+';
SUB: '-';
MUL: '*';
FLOAT_DIV: '/';
INT_DIV: '\\';
MOD: '%';
NE: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
ASSIGN: ':=';
INIT: '=';

/*** SEPARATORS ***/
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
LP: '(';
RP: ')';
SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

/*** LITERALS ***/
INTLIT: DigitSequence;

FLOATLIT
    : DigitSequence DecimalPart ExponentPart
    | DigitSequence DecimalPart
    | DigitSequence ExponentPart
    ;

fragment DIGIT: [0-9];
fragment DigitSequence: DIGIT+;
fragment Exponent: [Ee];
fragment SIGN: [+-];
fragment DecimalPart: DOT DigitSequence?;
fragment ExponentPart: Exponent SIGN DigitSequence;

BOOLLIT: TRUE | FALSE;

STRINGLIT: ('"') CHAR* ('"');
UNCLOSE_STRING:
	'"' CHAR* {
    raise UncloseString(self.text[:])
};
ILLEGAL_ESCAPE:
	'"' CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[:])
};

fragment CHAR
    :  ~[\b\t\n\f\r"\\]
    | ESCAPE_SEQUENCE
    ;
fragment ESCAPE_SEQUENCE
    : '\\b'
    | '\\f'
    | '\\r'
    | '\\n'
    | '\\t'
    | '\\"'
    | '\\\\'
    ;
fragment ESC_ILLEGAL
    : '\\' ~[btnfr"\\]
    | '\\'
    ;

ID: [_A-Za-z][_A-Za-z0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};