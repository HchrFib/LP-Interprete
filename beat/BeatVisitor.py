import textwrap  
if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor
from termcolor import colored, cprint
from colorama import init


class BeatVisitor(llullVisitor):
    
    def __init__(self):
        self.nivell = 0
        self.OKBLUE = '\033[94m'
        self.ENDC = '\033[0m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        
    def colored(self,r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


    # Visit a parse tree produced by llullParser#root.
    def visitRoot(self, ctx:llullParser.RootContext):
       
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#top.
    def visitTop(self, ctx:llullParser.TopContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#typeMethod.
    def visitTypeMethod(self, ctx:llullParser.TypeMethodContext):
        
        return self.visitChildren(ctx)


    # Method =========================================================
    def visitMethod(self, ctx:llullParser.MethodContext):
        #print(ctx.getText())
        
        type_method = ctx.header().type_m().getText()
        name_method = ctx.header().ID().getText()
        parameters = self.visit(ctx.block_parameters())
   
        #  Tratamos el header de la funcion void hanoi(n, ori, dst, aux)   

        color_type_method = self.colored(207, 34, 46,  type_method)
        color_name_method = self.colored(130, 80, 223, name_method)
        s = color_name_method + '('
        name_parentheses = "".join(s.split())
        #print(name_parentheses)
        header = color_type_method + name_parentheses
        
        # void main( --> {0}
        # a, b, c --> {1}

        final_str = "{0}{1})".format(header,parameters) 
        print(final_str,'{')
        # ==============================================================
        
        # Tratamos el bloque de instrucciones


        # ===================================

        return self.visitChildren(ctx)


    # Header
    def visitHeader(self, ctx):
        return self.visitChildren(ctx)
        

    # block_parameters.
    def visitBlock_parameters(self, ctx):
        list_parameters =  ctx.getText().split(',')
        text =""
        for i in list_parameters:
            text = text + i + ','+ " "
        final_str = text[:-2]
        #print(final_str)
        return final_str


    # Visit a parse tree produced by llullParser#parameters.
    def visitParameters(self, ctx:llullParser.ParametersContext):
        #print("visitParameters",ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#parameter.
    def visitParameter(self, ctx:llullParser.ParameterContext):
        #print(ctx.getText())
        return ctx.getText()
        #return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#block_instructions.
    def visitBlock_instructions(self, ctx:llullParser.Block_instructionsContext):
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        print(self.nivell*'   '+'}')

    # Visit a parse tree produced by llullParser#InstAssignment.
    def visitInstAssignment(self, ctx:llullParser.InstAssignmentContext):
        # aqui no
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InsIfStatement.
    def visitInsIfStatement(self, ctx:llullParser.InsIfStatementContext):
        # aqui no       
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InsWhileStatement.
    def visitInsWhileStatement(self, ctx:llullParser.InsWhileStatementContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InsForStatement.
    def visitInsForStatement(self, ctx:llullParser.InsForStatementContext):
       
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InstRead.
    def visitInstRead(self, ctx:llullParser.InstReadContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InsWrite.
    def visitInsWrite(self, ctx:llullParser.InsWriteContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InstrCallFunction.
    def visitInstrCallFunction(self, ctx:llullParser.InstrCallFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InstructionArray.
    def visitInstructionArray(self, ctx:llullParser.InstructionArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#CallFunction.
    def visitCallFunction(self, ctx:llullParser.CallFunctionContext):
        return self.visitChildren(ctx)


    # Asign.
    def visitAsign(self, ctx:llullParser.AsignContext):
        ini = ctx.getText()
        #print(ini)
        expression = ctx.expr().getText()
        simbol_assign = ctx.ASSIGN()
        indentifier = ctx.ID()

        indice_suma = expression.find('+')

        
        indice_resta = expression.find('-')
        indice_mult = expression.find('*')
        indice_div = expression.find('/')
        indice_pot = expression.find('^')


        #print(indentifier, simbol_assign, expression)
        espai = self.nivell*'   '
       
        final_str = "{0} {1} {2}".format(indentifier,simbol_assign, expression) 
        print(textwrap.fill(final_str, 60, initial_indent= espai))
        return self.visitChildren(ctx)
    

    # IfStatement 
    def visitIfStatement(self, ctx):
        # aqui no
        conditions = ctx.condition_block()
        evaluatedBlock = False;
        
        instruction_name = "if"

        #instruction_name = self.colored(207, 34, 46,  "if")
        #instruction_name = self.colored(72,202,228 ,"if") 
        for condition in conditions:
          
            evaluated = self.visit(condition.expr().expr());
            espai = self.nivell*'   '
            
            final_str =  self.OKBLUE +  "if" + self.ENDC +"({0})".format(evaluated)  
            indentation = textwrap.fill(final_str+' {', 60, initial_indent= espai) 
            print(indentation)
            

        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#BlockCondition.
    def visitBlockCondition(self, ctx:llullParser.BlockConditionContext):
        #aqui no
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#BlockElse.
    def visitBlockElse(self, ctx:llullParser.BlockElseContext):
      
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#WhileStatement.
    def visitWhileStatement(self, ctx:llullParser.WhileStatementContext):
        
        condition = self.visit(ctx.condition_block().expr().expr()) # EVALUACION DE LA CONDICION -> True o False

        espai = self.nivell*'   '
        final_str =  self.OKBLUE +  "while" + self.ENDC +"({0})".format(condition)  
        indentation = textwrap.fill(final_str+' {', 60, initial_indent= espai)
        print(indentation)
        return self.visitChildren(ctx)

    # ArrayDeclare.
    def visitArrayDeclare(self, ctx):
        print(self.nivell*'   '+ ctx.getText())
        return self.visitChildren(ctx)


    # ArrayGet.
    def visitArrayGet(self, ctx):
        #print(self.nivell*'   '+ ctx.getText())
        return "result_GET", ctx.getText()


    # ArraySet.
    def visitArraySet(self, ctx):
        print(self.nivell*'   '+ ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ForStatement.
    def visitForStatement(self, ctx):
        
        init = self.visit(ctx.for_control().for_init()) # i = 0
        for_condition = self.visit(ctx.for_control().for_expression())  # condicion del for.
        update_index = self.visit(ctx.for_control().for_update())
       

        espai = self.nivell*'   '
        final_str =  self.OKBLUE +  "for" + self.ENDC +"({0}; {1}; {2})".format(init, for_condition, update_index)  
        indentation = textwrap.fill(final_str+' {', 60, initial_indent= espai)
        print(indentation)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ForControl.
    def visitForControl(self, ctx:llullParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ForExpression.
    def visitForExpression(self, ctx:llullParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ForInit.
    def visitForInit(self, ctx:llullParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ForUpdate.
    def visitForUpdate(self, ctx:llullParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ForAssignment.
    def visitForAssignment(self, ctx:llullParser.ForAssignmentContext):


        ini = ctx.getText()
    
        expression = ctx.expr().getText()
        simbol_assign = ctx.ASSIGN()
        indentifier = ctx.ID()

       
        espai = self.nivell*'   '
       
        final_str = "{0} {1} {2}".format(indentifier,simbol_assign, expression) 
        #print(textwrap.fill(final_str, 60, initial_indent= espai))
        
        return final_str 


    # Visit a parse tree produced by llullParser#StatementBlock.
    def visitStatementBlock(self, ctx:llullParser.StatementBlockContext):
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        print(self.nivell*'   '+'}')

    # Visit a parse tree produced by llullParser#StatementForBlock.
    def visitStatementForBlock(self, ctx:llullParser.StatementForBlockContext):
        self.nivell += 1
        self.visitChildren(ctx)
        self.nivell -= 1
        print(self.nivell*'   '+'}')
       
    # Visit a parse tree produced by llullParser#type_m.
    def visitType_m(self, ctx:llullParser.Type_mContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprAddSub.
    def visitExprAddSub(self, ctx:llullParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprCondition.
    def visitExprCondition(self, ctx):
        type_v ,l =  self.visit(ctx.expr(0))
        symbol = ctx.op.text
        type_v ,r =  self.visit(ctx.expr(1))
        
        #identifier = "while"
        #color_identifier = self.colored(45, 136, 45, identifier)

        final_str = "{0} {1} {2}".format(l,symbol,r) 
        return final_str


    # Visit a parse tree produced by llullParser#ExprIndex.
    def visitExprIndex(self, ctx:llullParser.ExprIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprAtom.
    def visitExprAtom(self, ctx:llullParser.ExprAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprParentheses.
    def visitExprParentheses(self, ctx:llullParser.ExprParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprMultDiv.
    def visitExprMultDiv(self, ctx:llullParser.ExprMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprPower.
    def visitExprPower(self, ctx:llullParser.ExprPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprGetElement.
    def visitExprGetElement(self, ctx:llullParser.ExprGetElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#exprList.
    def visitExprList(self, ctx:llullParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#AtomBoolean.
    def visitAtomBoolean(self, ctx:llullParser.AtomBooleanContext):
        return "AtomBoolean" , ctx.getText()


    # Visit a parse tree produced by llullParser#AtomID.
    def visitAtomID(self, ctx:llullParser.AtomIDContext):
        identifier = ctx.getText()
        color_id = self.colored(45, 136, 45,  identifier)
        return "AtomId", identifier

    # Visit a parse tree produced by llullParser#AtomNumber.
    def visitAtomNumber(self, ctx:llullParser.AtomNumberContext):
        number = ctx.getText()
        color_number = self.colored(8, 83, 174,number)
       
        return "AtomNumber", number

    # Visit a parse tree produced by llullParser#AtomString.
    def visitAtomString(self, ctx:llullParser.AtomStringContext):
        return "AtomString",ctx.getText()


    # Visit a parse tree produced by llullParser#WriteLn.
    def visitWriteLn(self, ctx):
        list_res = []
        for i in range(len(ctx.expr())):
           
            type_v, value  = self.visit(ctx.expr(i))
            list_res.append(value)
       
        strlist_res = ",".join(list_res)
        
        espai = self.nivell*'   '

        final_str =  self.OKGREEN +  "write" + self.ENDC + "({0})".format(strlist_res)  
        indentation = textwrap.fill(final_str+' {', 60, initial_indent= espai)
        print(indentation)

        #print(self.nivell*'   '+ ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ReadLn.
    def visitReadLn(self, ctx):
        
        identifier = ctx.READ()
        value = ctx.expr().getText()
        espai = self.nivell*'   '

        final_str =  self.OKGREEN +  "read" + self.ENDC + "({0})".format(value)  
        indentation = textwrap.fill(final_str+' {', 60, initial_indent= espai)
        print(indentation)
        
        return self.visitChildren(ctx)




