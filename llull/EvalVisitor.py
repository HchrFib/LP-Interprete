
if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
    from .llullVisitor import llullVisitor
else:
    from llullParser import llullParser
    from llullVisitor import llullVisitor


class EvalVisitor(llullVisitor):
    def __init__(self):

        self.dictionaryParameters = {}
        self.program = {}
        self.stackFunctions = []  # pila de llamadas de funciones.

        # Visit a parse tree produced by llullParser#root.
    def setUp(self, init, parameters, flag):
    
        self.init_function = init
        self.listParametersTerminal = parameters
        self.flag_terminal = flag
       
    # A partir de la funcion visitRoot, hago un recorrido a demanda del arbol
    # para almacenar la informacion en estructura de datos. 
    def visitRoot(self, ctx):
        
        # Variable que contiene el nombre de la funcion de inicio del programa. Por defecto main.
        ctx_function_init = None
        listsTypeMethods = ctx.top().typeMethod()
        for typeMethod in listsTypeMethods:
            ctx_method = typeMethod.method()
            
            functionName = ctx_method.header().ID().getText().lower()          # lower(). ponemos todos los nombres de las funciones en minusculas, por si tenemos funciones con el mismo nombre
            typeMethod   = ctx_method.header().type_m().getText().lower()      # get type method: void or int.
            parameters   = ctx_method.block_parameters().getText()             # parametros de la funcion
            context      = ctx_method.block_instructions()                     # Important : save context!

            if not functionName in self.program:
                self.program[functionName] = typeMethod
            else:
                print("Error: '", functionName, " method ' already exists (finished).")
                exit()
            #print(self.program)

            #  Funcion de inicio del programa
            if functionName == self.init_function:
                ctx_function_init = ctx_method
                
            
            infoFunctions = {}
            infoFunctions['id']         = functionName
            infoFunctions['parameters'] = parameters
            infoFunctions['context']    = context

            self.stackFunctions.append(infoFunctions)
        
        #print(self.stackFunctions)  
        if ctx_function_init == None:
            print("'", self.init_function ,"' method has not been declared (finished).")        
            exit()
        #print(ctx_main.getText())
        return self.visit(ctx_function_init) # El ctx_main, le dice al método visit() a donde ir.
       

    # Visit a parse tree produced by llullParser#top.
    def visitTop(self, ctx):
        #print("visitTop")
        return self.visitChildren(ctx)

    def visitTypeMethod(self, ctx):
        return self.visitChildren(ctx)

    def visitMethod(self, ctx):
        #print("visitMethod")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#header.
    def visitHeader(self, ctx):

        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#block_parameters.
    def visitBlock_parameters(self, ctx: llullParser.Block_parametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#parameters.
    def visitParameters(self, ctx: llullParser.ParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#parameter.
    def visitParameter(self, ctx: llullParser.ParameterContext):
        return self.visitChildren(ctx)

# Block_instructions =============================================
    def visitBlock_instructions(self, ctx):
        #print("visitBlock_instructions")
        
        if self.flag_terminal:
            # Comprobaciones antes de llamar a la funcion.
            # ============================================
            
            # 1) Comprobamos que exista la funcion.
            list_parameters_function, info_function = self.verifyExistFunction(self.init_function)
            
            # 2) comprobamos el numero de argumentos, de la lista de parametros 
            #    entrada por el terminal y de la funcion pasada por terminal tambien 
            self.compareNumParameters(self.init_function, self.listParametersTerminal, list_parameters_function)
            # 3) convertir la lista de parámetros a un diccionario(el tipo de valor de cada parametro)
            self.dictionaryParameters = self.list2Dictionary(self.listParametersTerminal, list_parameters_function)       
        
        self.symbolTable = self.dictionaryParameters
       
        #print(self.symbolTable)
        #print(ctx.getText())
        return self.visitChildren(ctx)

# ================================================================
# ================================================================


# InstAssignament ================================================

    def visitInstAssignment(self, ctx):
        #print("visitInstAssignment")
        #print(ctx.getText())
        return self.visitChildren(ctx)

# =================================================================
# =================================================================
    

# InsIfStatement ==================================================

    def visitInsIfStatement(self, ctx):
                  
        return self.visitChildren(ctx)

# ==================================================================
# ==================================================================

# InsWhileStatement ================================================

    def visitInsWhileStatement(self, ctx):
        #print("visitInsWhileStatement")
        #print(ctx.getText())
        return self.visitChildren(ctx)

# ==================================================================
# ==================================================================

# InsForStatement ==================================================
    def visitInsForStatement(self, ctx):
        #print("visitInsForStatement")
        #print(ctx.getText())
        return self.visitChildren(ctx)
# ==================================================================
# ==================================================================

    # Visit a parse tree produced by llullParser#InstRead.
    def visitInstRead(self, ctx: llullParser.InstReadContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#InsWrite.
    def visitInsWrite(self, ctx: llullParser.InsWriteContext):
        return self.visitChildren(ctx)


# compareNumParameters ==============================================

    #Compara el numero de parametros de la llamada a la funcion con el numero de parametros de la funcion. 

    def compareNumParameters(self, called_function_name ,list_parameters_function_called, list_parameters_function):
        if len(list_parameters_function_called) != len(list_parameters_function):
            #print("'",called_function_name,"' name or number of arguments do not match (program finished).")
            print("Number of arguments do not match (program finished).")
            exit()

# ====================================================================
# ====================================================================

# Convierte una lista en un diccionario ==============================

    def list2Dictionary(self, list1, list2):
        #print(list1, "  -  " , list2)
        dictParameters = {}
        i = 0
        if self.flag_terminal:
            for value in list1:
                dictParameters[list2[i]] = str(value)            
                i = i + 1
        else:

            for element in list1:
                type_v, value  = element
                if type_v == "AtomId":              # si el elemento de lista es una variable.
                    if value in self.symbolTable:
                        dictParameters[list2[i]] = self.symbolTable[value]
                    else:
                        dictParameters[list2[i]] = str(0)
                elif type_v == "result" or type_v == "AtomNumber":
                    dictParameters[list2[i]] = str(value)
                i = i + 1
        return dictParameters
# ======================================================================
# ======================================================================

# Verifica si la funcion de llamada existe =============================
    
    def verifyExistFunction(self, called_function_name):
        # Antes de añadir una funcion a la pila debemos comprobar que ya se ha declarado.
        if not called_function_name in self.program:
            print(called_function_name, " has not been declared (program finished).")
            exit()
        else:
            
            info_function = next(x for x in self.stackFunctions if x["id"] == called_function_name)
            
            # Obtenemos los parametros de la funcion en formato lista
            if not info_function['parameters'] == '':
                list_parameters_function = info_function['parameters'].split(',')
            else:
                list_parameters_function = []
        return list_parameters_function, info_function

# =======================================================================
# =======================================================================


 
# InstructionArray ======================================================
    
    def visitInstructionArray(self, ctx):
        #print("visitInstructionArray")
        return self.visitChildren(ctx)

# ========================================================================
# ========================================================================


    def visitInstrCallFunction(self, ctx):
        return self.visitChildren(ctx)

# CALL_FUNCTION ==========================================================
    def visitCallFunction(self, ctx):
        #print("visitCallFunction")
        info_function = ""         # contiene la informacion de un procedimento
        

        called_function_name = ctx.ID().getText()   # call_function :   ID '(' exprList? ')'
        
        # En caso de que la funcion/procedimiento no tenga parametros.
        

        # Otenemos los parametros de la funcion de LLAMADA en formato lista.
        # ===================================================================

        if ctx.exprList() is not None:
            self.visit(ctx.exprList())
        else: 
            self.listParameters = []

        # ===================================================================
        # ===================================================================


        self.stackFunctions.append(called_function_name)
        
        # Comprobacion antes de realizar una llamada a una funcion.
        # ===================================================================

        # 1) Comprobamos que exista la funcion
        list_parameters_function, info_function = self.verifyExistFunction(called_function_name)

        # 2) # Comprobamos que el numero de parametros de la llamada y el de la funcion coincidan, en caso contrario, nos dará error.
        self.compareNumParameters(called_function_name, self.listParameters, list_parameters_function)

        # =====================================================================
        # =====================================================================

        # Creamos un diccionario de parámetros ================================
        self.dictionaryParameters = self.list2Dictionary(self.listParameters, list_parameters_function)
        # =====================================================================
        
        #print(self.dictionaryParameters)


        # Pasamos el contexto de la funcion y visitamos el bloque para que ejecute las operaciones correspondientes al bloque.
        # self.visitBlock_instructions(value["context"])
        
        # Encadenamos las tablas de simbolos, con esto mantenemos el ámbito de las variables.
        backUp = self.symbolTable
        self.visit(info_function['context'])
        self.symbolTable = backUp   

        return self.visitChildren(ctx)

# ==============================================================================
# ==============================================================================



# Asign ============================================================================================    
    
    def visitAsign(self, ctx):
        #print("visitAsign")
        #print(ctx.getText())   # = 3
        identifier = ctx.ID().getText()  # -> d
        type_v ,value = self.visit(ctx.expr())
        
        self.symbolTable[identifier] = value
        #print(identifier, " " , value)
        
        #print(self.symbolTable)
        return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================


# IfStatement ======================================================================================

    def visitIfStatement(self, ctx):
        #print("visitIfStatement")       
        #print(ctx.getText())            # --> if(a<c){write("se cumple")}else{write("no se cumple")}
        
        conditions = ctx.condition_block()
        evaluatedBlock = False;
        for condition in conditions:
          
            type_v , evaluated = self.visit(condition.expr().expr());
            #print(evaluated)
            if(evaluated == True):
                evaluatedBlock = True   
                
                self.visit(condition.statement_block())
                break
        # En el caso del bloque else
        if not ctx.block_else() == None:
            if(evaluatedBlock == False):
                
                self.visit(ctx.block_else())
            #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

# BlockCondition ===================================================================================

    def visitBlockCondition(self, ctx):
        #print("visitBlockCondition")
        #print(ctx.getText())            # --> (a<c){write("se cumple")}
        return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================
   
    # Visit a parse tree produced by llullParser#BlockElse.
    def visitBlockElse(self, ctx:llullParser.BlockElseContext):
        return self.visitChildren(ctx)


# WhileStatement ===================================================================================

    def visitWhileStatement(self, ctx):
        #print("visitWhileStatement")
        #print(ctx.getText())
        type_c , condition = self.visit(ctx.condition_block().expr().expr())  # EVALUACION DE LA CONDICION ->TRUE
        #conditions = ctx.bloque_condicion()
        
        
        while(condition): 
            
            self.visit(ctx.condition_block())  
            type_c, condition = self.visit(ctx.condition_block().expr().expr()) # EVALUACION DE LA CONDICION -> True o False
           
        
# ==================================================================================================
# ==================================================================================================
  

# ArrayDeclare =====================================================================================

    def visitArrayDeclare(self, ctx):
        #print("visitArrayDeclare")
        # Declaracion del array
        # =====================

        # 1) Obtenemos el identificador
        identifier = ctx.ID().getText()
        #print(identifier)
        # 2) Verificamos si existe el identificador
        if identifier in self.symbolTable: 
            print("'" ,identifier,"' already exists (program finished).")
            exit()
        
        # 3) inicializamos el array
        type_v, num_elements = self.visit(ctx.expr())
        list_array = [0]*int(num_elements)
        self.symbolTable[identifier] = list_array
        #print(self.symbolTable)
        #print("declare: ", list_array)
        #return self.visit(ctx.expr())
        #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

# ArrayGet =========================================================================================
   
    def visitArrayGet(self, ctx):
        #print("visitArrayGet")

        # 1) Obtenemos el identificador
        identifier = ctx.ID().getText() 

        # 2) Comprobamos si el array existe
        if not identifier in self.symbolTable:
            print("'",identifier,"' has not been declared (program finished).")        
            exit()

        # 4) Obtenemos el index 
        try:
            type_i, index = self.visit(ctx.expr())
        except Exception:
            print("'",index,"'Index does not exist ")
            exit()
        # 5) Comprobamos 
        if(not index.isdigit()):
            
            
            if not index in self.symbolTable:
                print("'",index,"'Index does not exist ")
                exit()
            inx = int(self.symbolTable[index])
        else:
            inx = int(index)

        # 6) Obtenemos el valor del array
        list_array = self.symbolTable[identifier]
        #print("get ",list_array[int(index)])
        
        return "result_GET", list_array[inx]
        #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

# ArraySet =========================================================================================

    def visitArraySet(self, ctx):
        
        # 1) Obtenemos el identificador
        identifier = ctx.ID().getText() 
        # 2) Comprobamos si el array existe
        if not identifier in self.symbolTable:
            print("'",identifier,"' has not been declared (program finished).")        
            exit()
        # 3) Obtenemos el array
        list_array = self.symbolTable[identifier]
       
        # 4) Obtenemos el index 
        type_i, index = self.visit(ctx.expr(0))
        
        # 5) Comprobamos 
        if(not index.isdigit()): 
            if not index in self.symbolTable:
                print("'",index,"'Index does not exist ")
                exit()
            inx = int(self.symbolTable[index])
        else:
            inx = int(index)

        # 6) Comprobamos el indice 
        try:
            list_array[int(inx)]
        except IndexError:
            print("'",inx,"' index out of range (program finished).")        
            exit()

        # 6) Obtenemos el valor
        type_v, value = self.visit(ctx.expr(1))
        # 7) Guardamos el valor en el array
        list_array[int(inx)] = int(value)
        #print("set",list_array)
        #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================


# ForStatement =====================================================================================
    
    def visitForStatement(self, ctx):
        #print("visitForStatement") 
        # Nos guardamos el contexto de la estructura del For, para hacer la llamada del for_update
        # en el orden correcto.

        ctx_init                    = self.visit(ctx.for_control().for_init())
        ctx_expression_condition    = self.visit(ctx.for_control().for_expression())  # condicion del for.
        ctx_update                  = self.visit(ctx.for_control().for_update())
        ctx_block                   = self.visit(ctx.statement_ForBlock())
        
        #print(ctx_init , " " , ctx_expression_condition, " ", ctx_update, " ", ctx_block.getText())
        
        # Pasos de for:
        # =============
        # 1) Inicializar variable
        # 2) Evaluar condicion
        # 3) Ejecutar bloque de instrucciones
        # 4) Actualizar indice

        # 1)
        self.visit(ctx_init.for_assignment())
        # 2)
        type_v, condition = self.visit(ctx_expression_condition.expr())
        
        while(condition):

            # 3)
        
            ctx_instrucions = ctx_block.instruction()
            for inst in ctx_instrucions:
                self.visit(inst)
            
            # 4) 
            self.visit(ctx_update.for_assignment())
            type_v, condition = self.visit(ctx_expression_condition.expr())

        
        #print(condition)



        #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

# ForControl =======================================================================================

    def visitForControl(self, ctx):
        #print("visitForControl")
        return ctx.getText()
        #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

# ForExpression ====================================================================================

    def visitForExpression(self, ctx):
        #print("visitForExpression")
        return ctx
        #print(ctx.getText())
        #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

# ForInit ==========================================================================================

    def visitForInit(self, ctx):
        #print("visitForInit")
        return ctx
        #return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

# ForUpdate ========================================================================================
    
    def visitForUpdate(self, ctx):
        #print("visitForUpdate")
        #print(ctx.getText())
        return ctx
        #return self.visitChildren(ctx)
# ==================================================================================================
# ==================================================================================================

# ForAssignment ====================================================================================

    def visitForAssignment(self, ctx): 
        #print("visitForAssignment")

        identifier = ctx.ID().getText()  
        type_v ,value = self.visit(ctx.expr())    
        self.symbolTable[identifier] = value
        return self.visitChildren(ctx)

# ==================================================================================================
# ==================================================================================================

    # Visit a parse tree produced by llullParser#StatementBlock.
    def visitStatementBlock(self, ctx: llullParser.StatementBlockContext):
        return self.visitChildren(ctx)

# StatementForBlock ===============================================================================

    def visitStatementForBlock(self, ctx):
        #print("visitStatementForBlock")
        #print(ctx.getText())
        return ctx
# ==================================================================================================
# ==================================================================================================


    # Visit a parse tree produced by llullParser#type_m.
    def visitType_m(self, ctx: llullParser.Type_mContext):
        return self.visitChildren(ctx)

# AddSub ==========================================================================================

    def visitExprAddSub(self, ctx):
        
        #print("visitExprAddSub")
        type_v_left , left   = self.visit(ctx.expr(0))
        type_v_right, right  = self.visit(ctx.expr(1))
        
        #print(type_v_left, " ", type_v_right)
        #print(type(left), " x ", type(right)) 

        # LEFT: en el caso de ser letra
        if(not left.isdigit()):
            if not left in self.symbolTable:
                   
                self.symbolTable[left] = 0
                num_left = 0     
            else:    
                num_left = int(self.symbolTable[left])
        else :   
                         
            num_left = int(left)
        
        # RIGHT: en el caso de ser letra
        if(not right.isdigit()):    
            if not right in self.symbolTable:
                self.symbolTable[right] = 0
                num_right = 0
            else:
                num_right = int(self.symbolTable[right])
        else :                      
            num_right = int(right)
        
        if ctx.op.type == llullParser.ADD:
            return "result", str(num_left + num_right)
        return "result", str(num_left - num_right)

        #print("addSum",ctx.getText())

        #print(left, " ", right)
        

# ================================================================================================
# ================================================================================================

# ExprCondition ==================================================================================
    def str2bool(self,v): 
        return v.lower() in ("true", "1")

    def visitExprCondition(self, ctx):
        type_v ,l =  self.visit(ctx.expr(0))
        type_v ,r =  self.visit(ctx.expr(1))
        

        # Lo Convierto a cadena, porque si tengo i < 10, me retornará i = 0, pero entero
        # esto nos supondrá un problema en esta función

        left  = str(l)       # convertimos a cadena
        right = str(r)       # convertimos a cadena   
        

        flagBoolean = False

        # LEFT: en el caso de ser letra
        if(not left.isdigit()):
           
            if (left == 'True') or (left == 'False'):           
                flagBoolean = True
                boolean_left = self.str2bool(left)
                
            else:  

                if not left in self.symbolTable:
                    self.symbolTable[left] = 0
                    num_left = 0
                else:
                    num_left = int(self.symbolTable[left])
        
        else :
            num_left = int(left)
        
        # RIGHT: en el caso de ser letra
        if(not right.isdigit()):

            if (right == 'True') or (right == "False"):   
                flagBoolean = True
                boolean_right = self.str2bool(right)
            else:
                if not right in self.symbolTable:
                    self.symbolTable[right] = 0
                    num_right = 0
                else:
                    num_right = int(self.symbolTable[right])
        else:
            num_right = int(right)
        # OR
        if ctx.op.type == llullParser.OR:
            return "result_Or",boolean_left or boolean_right
        # AND
        elif ctx.op.type == llullParser.AND:
            return "result_And", boolean_right and boolean_right
        # EQ
        elif ctx.op.type == llullParser.EQ:
            if flagBoolean:
                
                res  = boolean_left == boolean_right
                
                return "result_boolean_EQ",res
            else:
                return "result_num_EQ", num_left == num_right
        # NEQ
        elif ctx.op.type == llullParser.NEQ:
            if flagBoolean:
                return "result_boolean_NEQ", boolean_left != boolean_right
            else:
                return "result_num_NEQ",num_left != num_right
        # LT        
        elif ctx.op.type == llullParser.LT:
            return "result_LT",num_left < num_right    
        # GT    
        elif ctx.op.type == llullParser.GT:
            return "result_GT",num_left > num_right
        # GTEQ
        elif ctx.op.type == llullParser.GTEQ:
            return "result_GTEQ",num_left >= num_right
        # LTEQ
        elif ctx.op.type == llullParser.LTEQ:
            return "result_LTEQ",num_left <= num_right


# ================================================================================================
# ================================================================================================


    # Visit a parse tree produced by llullParser#ExprIndex.
    def visitExprIndex(self, ctx: llullParser.ExprIndexContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#ExprAtom.
    def visitExprAtom(self, ctx: llullParser.ExprAtomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by llullParser#ExprParentheses.
    def visitExprParentheses(self, ctx: llullParser.ExprParenthesesContext):
        return self.visitChildren(ctx)

# MulDiv ========================================================================================

    def visitExprMultDiv(self, ctx):
        type_v, left   = self.visit(ctx.expr(0))
        type_v, right  = self.visit(ctx.expr(1))
        
        # LEFT: en el caso de ser letra
        if(not left.isdigit()):     num_left = int(self.symbolTable[left])
        else :                      num_left = int(left)
        
        # RIGHT: en el caso de ser letra
        if(not right.isdigit()):    num_right = int(self.symbolTable[right])
        else :                      num_right = int(right)
        
        if ctx.op.type == llullParser.MUL:
            return "result", str(num_left * num_right)

        try:
            return "result", str(int(num_left / num_right)) 
        except ZeroDivisionError:
            print("Error division by zero: " ,num_left,"/", num_right)
            exit()
        
# ================================================================================================
# ================================================================================================


    # Visit a parse tree produced by llullParser#ExprPower.
    def visitExprPower(self, ctx: llullParser.ExprPowerContext):
        type_v, left   = self.visit(ctx.expr(0))
        type_v, right  = self.visit(ctx.expr(1))
        
        # LEFT: en el caso de ser letra
        if(not left.isdigit()):     num_left = int(self.symbolTable[left])
        else :                      num_left = int(left)

        # RIGHT: en el caso de ser letra
        if(not right.isdigit()):    num_right = int(self.symbolTable[right])
        else :                      num_right = int(right)
        
        return "result", str(num_left ** num_right)
       

    # Visit a parse tree produced by llullParser#exprList.
    
# ExprList (list parameters) =====================================================================

    def visitExprList(self, ctx):
        self.listParameters = []
        for parameter in ctx.expr():
            self.listParameters.append(self.visit(parameter))
        #print(self.listParameters)
        return self.listParameters

# ================================================================================================
# ================================================================================================

# ATOMS

# AtomBoolean =========================================================================================

    # Visit a parse tree produced by llullParser#AtomBoolean.
    def visitAtomBoolean(self, ctx: llullParser.AtomBooleanContext):
        return "AtomBoolean" , ctx.getText()

# ================================================================================================
# ================================================================================================


# AtomID =========================================================================================

    def visitAtomID(self, ctx: llullParser.AtomIDContext):
        #print("visitAtomID")
        #print(ctx.getText())
        return "AtomId", ctx.getText()

# ================================================================================================
# ================================================================================================

# AtomNumber =====================================================================================
    
    def visitAtomNumber(self, ctx):
        #print("visitAtomNumber")
        #print(ctx.getText())
        return "AtomNumber",ctx.getText()

# ================================================================================================
# ================================================================================================


# AtomString =====================================================================================
    
    def visitAtomString(self, ctx):  
        #print("visitAtomString")
        #print(ctx.getText())
        return "AtomString",ctx.getText()

# ================================================================================================
# ================================================================================================




# ========================================================

    def visitWriteLn(self, ctx): 
        #print("visitWriteLn")
        
        list_res = []
        for i in range(len(ctx.expr())):
            
            type_v, identifier  = self.visit(ctx.expr(i))
            
            if type_v == "AtomId":
                if identifier in self.symbolTable:
                    
                    list_res.append(self.symbolTable[identifier])
       
                    
                else:
                    self.symbolTable[identifier] = 0
                    list_res.append(0)             
                    print("'",identifier ,"' does not exist. Its value has been initialized to 0.")         
            else:
                list_res.append(identifier)
                #print(identifier)
        #print(type(list_res))
        
        values = ','.join(str(v) for v in list_res)
        #strlist_res = ",".join(list_res) 
        print(values)     
        #print(self.symbolTable)    
        return self.visitChildren(ctx)


# ReadLn =================================================
    def visitReadLn(self, ctx):
        type_v, identifier = self.visit((ctx.expr()))
        value = input()
        self.symbolTable[identifier] = value
        return self.visitChildren(ctx)
