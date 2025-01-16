grammar llull;

root : top EOF;

top : typeMethod+;

typeMethod : method;

method : header '('block_parameters')' block_instructions ;


header 					: 	type_m ID 					;
block_parameters 		: 	parameters*  				;
parameters				: 	parameter (',' parameter)* 	;
parameter 				:	expr						;	


block_instructions : '{'instruction*'}';

instruction	: 		assignment				# InstAssignment
				| 	if_statement			# InsIfStatement
				|	while_statement			# InsWhileStatement 
				|	for_statement			# InsForStatement
				|	read					# InstRead
				|	write					# InsWrite
				|	call_function			# InstrCallFunction
				| 	instruction_array		# InstructionArray
				;

call_function	:	ID '(' exprList? ')' 													# CallFunction 		;
assignment 		:   ID ASSIGN expr 															# Asign 			;


if_statement		: 	IF condition_block (ELSE IF condition_block)* (block_else)? 			# IfStatement 		;
condition_block 	: 	expr statement_block	   												# BlockCondition	;
block_else         	: 	ELSE statement_block 	              									# BlockElse        	;
while_statement 	:	WHILE condition_block													# WhileStatement    ;

instruction_array	:	ARRAY'(' ID  ',' expr ')'												# 	ArrayDeclare	
					|	GET'('   ID  ',' expr ')'												#	ArrayGet		
					|	SET'('   ID  ',' expr ',' expr')'										#	ArraySet		
					;									

// For statement =================================================================================
for_statement		   :	FOR '(' for_control ')' statement_ForBlock					# ForStatement			;

for_control            :   	for_init? ';' for_expression? ';' for_update?			    # ForControl        	;
for_expression         :   	expr                                                     	# ForExpression     	;
for_init               :   	for_assignment	                                        	# ForInit           	;
for_update             :   	for_assignment                                             	# ForUpdate         	;  
for_assignment		   :	ID ASSIGN expr 												# ForAssignment 		;		
// ===============================================================================================

statement_block			:  	OBRACE instruction* CBRACE							# StatementBlock;
statement_ForBlock		:	OBRACE instruction* CBRACE							# StatementForBlock;

type_m : VOID | INT ;

expr:   expr '[' expr ']'                                               # ExprIndex
    |   <assoc=right> expr POTENCIA expr                                # ExprPower
    |   expr op=(MUL|DIV) expr                                          # ExprMultDiv
    |   expr op=(ADD|SUB) expr                                          # ExprAddSub
    |   expr op=(OR|AND|EQ|NEQ|GT|LT|GTEQ|LTEQ) expr                    # ExprCondition
    |	atom					                                        # ExprAtom
    |   '(' expr ')'                                                    # ExprParentheses
    |	instruction_array												# ExprGetElement
    ;



exprList 	: 	expr (',' expr)* 	  ;

atom 	:  (TRUE | FALSE) 	# AtomBoolean
		|  ID             	# AtomID
 		|  NUM		       	# AtomNumber 
 		|  STRING           # AtomString
 		;

write 		:	WRITE '(' expr (',' expr)* ')'  	# WriteLn		;
read  		:   READ  '('expr')'  					# ReadLn		;



POTENCIA:   '^'    		;
ADD     :   '+'     	;
SUB     :   '-'     	;
MUL     :   '*'     	;
DIV     :   '/'     	;
OR 		:  	'||'		;
AND 	: 	'&&'		;
EQ 		: 	'=='		;
NEQ 	: 	'<>'		;
GT 		: 	'>'			;
LT 		: 	'<'			;
GTEQ 	: 	'>='		;
LTEQ 	: 	'<='		;
ASSIGN	:	'='			;
ARRAY 	:	'array'		;
GET     :	'get'		;
SET 	:	'set'		;
OBRACE	:	'{'			;
CBRACE	:	'}'			;
READ	:	'read'		;
WRITE	:	'write'		;
FOR 	:	'for'		;
WHILE 	:	'while'		;
IF      : 	'if'    	;
ELSE    : 	'else'  	;
TRUE	: 	'True'		;
FALSE	:	'False'		;
NUM 	:	[0-9]+		;
VOID	:   'void'		;
INT     :   'int'		;
FUNCTION :	'function'	;
ID	:	LETRA (LETRA | [0-9])*				;
LETRA	:	[a-zA-Z]						;
STRING      : '"' (~["\r\n] | '""')* '"'    ;
WS  :   [ \t\n\r]+ -> skip 					;
NEWLINE : 	'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
SL_COMMENT	:   '#' .*? '\n' -> skip		;


