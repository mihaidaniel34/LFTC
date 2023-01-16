
%{
#include <stdio.h>
#include <stdlib.h>

int yyerror(char *s);

#define YYDEBUG 1
%}

%token VAR;
%token CONST;
%token PRINT;
%token INPUT;
%token ELSE;
%token WHILE;
%token FOR;
%token LIST;
%token ADD;
%token INT;
%token STRING;
%token BOOL;
%token TRUE;
%token FALSE;

%token IDENTIFIER;
%token INTEGER;
%token STR;

%token PLUS;
%token MINUS;
%token TIMES;
%token DIV;
%token MOD;
%token EQUALS;
%token NOTEQUAL;
%token EQ;
%token LESSEQ;
%token GREATEREQ;
%token GREATER;
%token LESS;
%token AND;
%token OR;

%token BRACKETOPEN;
%token NEWLINE;
%token BRACKETCLOSED;
%token CURLYOPEN;
%token CURLYCLOSED;
%token SQUAREOPEN;
%token SQUARECLOSED;
%token COLON;
%token SEMICOLON;
%token COMMA;
%token ARROW;

%start Program

%%  

Program : Statement SEMICOLON Program {printf("Program -> Statement; Program\n");} | Statement SEMICOLON {printf("Program -> Statement;\n");} | SEMICOLON;
Statement : VarDeclStatement {printf("Statement -> VarDeclStatement\n");}
          | AssignStatement {printf("Statement -> AssignStatement\n");}
          | ListStatement {printf("Statement -> ListStatement\n");}
          | IfStatement     { printf("Statement -> IfStatement\n"); }
          | WhileStatement     { printf("Statement -> WhileStatement\n"); }
          | ForStatement     { printf("Statement -> ForStatement\n"); }
          | PrintStatement     { printf("Statement -> PrintStatement\n"); }
          | AddStatement     { printf("Statement -> AddStatement\n"); }
          | InputStatement     { printf("Statement -> InputStatement\n"); };    

VarDeclStatement : VAR Type Identifiers {printf("VarDeclStatement -> Identifiers");} | CONST Type Identifiers {printf("ConstDeclStatement -> Identifiers");};
Identifiers : IdentifierExp {printf("Identifiers -> IdentifierExp\n");} | IdentifierExp COMMA Identifiers {printf("Identifiers -> IdentifierExp, Identifiers\n");};
IdentifierExp : IDENTIFIER {printf("IdentifierExp -> IDENTIFIER\n");} | IDENTIFIER EQ Expression {printf("IdentifierExp -> IDENTIFIER = Expression\n");};
Expression : IntegerExp {printf("Expression -> IntegerExp \n");} | StringExp {printf("Expression -> StringExp \n");} ;
MathOperator : PLUS {printf("MathOperator -> + \n");} | MINUS {printf("MathOperator -> - \n");} | TIMES {printf("MathOperator -> * \n");} | DIV {printf("MathOperator -> / \n");} | MOD {printf("MathOperator -> % \n");} ;
IntegerExp : INTEGER {printf("IntegerExp -> INTEGER \n");} | IDENTIFIER {printf("IntegerExp -> IDENTIFIER \n");} | IntegerExp MathOperator IntegerExp {printf("IntegerExp -> IntegerExp MathOperator IntegerExp \n");};
StringExp : STRING {printf("StringExp -> STRING \n");};
ListStatement : VAR LIST Type IdentifierList {printf("ListStatement -> var list type IdentifierList\n");};
IdentifierList : IDENTIFIER {printf("IdentifierList -> IDENTIFIER\n");} | IDENTIFIER COMMA IdentifierList {printf("IdentifierList -> IDENTIFIER, IdentifierList\n");};
AssignStatement : IDENTIFIER EQ Expression {printf("AssignStatement -> IDENTIFIER = Expression \n");} ;
IfStatement : BRACKETOPEN Condition BRACKETCLOSED ARROW CURLYOPEN Program CURLYCLOSED {printf("IfStatement -> ( Condition ) => { Program } \n");} | BRACKETOPEN Condition BRACKETCLOSED ARROW CURLYOPEN Program CURLYCLOSED ELSE ARROW CURLYOPEN Program CURLYCLOSED {printf("IfStatement -> ( Condition ) =>  { Program } else => { Program } \n");} ;
RelationalOp : EQUALS {printf("RelationalOp -> ==\n");} | LESS {printf("RelationalOp -> <\n");} | LESSEQ {printf("RelationalOp -> <=\n");} | GREATER {printf("RelationalOp -> >\n");} | GREATEREQ {printf("RelationalOp -> >=\n");} |NOTEQUAL {printf("RelationalOp -> !=]n");} ;
Condition : Expression RelationalOp Expression {printf("Condition -> Expression RelationalOp Expression\n");}
			| Expression RelationalOp Expression AND Expression RelationalOp Expression {printf("Condition -> Expression RelationalOp Expression && Expression RelationalOp Expression\n");}
			| Expression RelationalOp Expression OR Expression RelationalOp Expression {printf("Condition -> Expression RelationalOp Expression || Expression RelationalOp Expression\n");} ;
WhileStatement : WHILE BRACKETOPEN Condition BRACKETCLOSED ARROW CURLYOPEN Program CURLYCLOSED {printf("WhileStatement -> while ( Condition ) => { Program }\n");} ;
ForStatement : FOR BRACKETOPEN ForDeclStmt COMMA Condition BRACKETCLOSED ARROW CURLYOPEN Program CURLYCLOSED {printf("ForStatement -> for ( var type identifier = expression, Condition ) => { Program }\n");} ;
ForDeclStmt : VAR Type IDENTIFIER EQ Expression {printf("ForDeclStatement -> var type IDENTIFIER = expression\n");};
PrintStatement : PRINT BRACKETOPEN IDENTIFIER BRACKETCLOSED { printf("PrintStatement -> print ( Expression )\n"); };
InputStatement : INPUT BRACKETOPEN IDENTIFIER BRACKETCLOSED     { printf("InputStatement -> input ( IDENTIFIER )\n"); }
Type : INT {printf("Type -> int \n");} | STR {printf("Type -> string\n");} | BOOL {printf("Type -> bool\n");};
AddStatement: ADD BRACKETOPEN IDENTIFIER COMMA IDENTIFIER BRACKETCLOSED {printf("AddStatement -> add(identifier, identifier)\n");};

%%
int yyerror(char *s) {
    printf("Error: %s", s);
}

extern FILE *yyin;

int main(int argc, char** argv) {
    if (argc > 1) 
        yyin = fopen(argv[1], "r");
    if (!yyparse()) 
        fprintf(stderr, "\tOK\n");
}