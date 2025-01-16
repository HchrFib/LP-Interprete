# Generated from llull.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .llullParser import llullParser
else:
    from llullParser import llullParser

# This class defines a complete generic visitor for a parse tree produced by llullParser.

class llullVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by llullParser#root.
    def visitRoot(self, ctx:llullParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#top.
    def visitTop(self, ctx:llullParser.TopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#typeMethod.
    def visitTypeMethod(self, ctx:llullParser.TypeMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#method.
    def visitMethod(self, ctx:llullParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#header.
    def visitHeader(self, ctx:llullParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#block_parameters.
    def visitBlock_parameters(self, ctx:llullParser.Block_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#parameters.
    def visitParameters(self, ctx:llullParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#parameter.
    def visitParameter(self, ctx:llullParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#block_instructions.
    def visitBlock_instructions(self, ctx:llullParser.Block_instructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InstAssignment.
    def visitInstAssignment(self, ctx:llullParser.InstAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#InsIfStatement.
    def visitInsIfStatement(self, ctx:llullParser.InsIfStatementContext):
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


    # Visit a parse tree produced by llullParser#Asign.
    def visitAsign(self, ctx:llullParser.AsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#IfStatement.
    def visitIfStatement(self, ctx:llullParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#BlockCondition.
    def visitBlockCondition(self, ctx:llullParser.BlockConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#BlockElse.
    def visitBlockElse(self, ctx:llullParser.BlockElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#WhileStatement.
    def visitWhileStatement(self, ctx:llullParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ArrayDeclare.
    def visitArrayDeclare(self, ctx:llullParser.ArrayDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ArrayGet.
    def visitArrayGet(self, ctx:llullParser.ArrayGetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ArraySet.
    def visitArraySet(self, ctx:llullParser.ArraySetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ForStatement.
    def visitForStatement(self, ctx:llullParser.ForStatementContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#StatementBlock.
    def visitStatementBlock(self, ctx:llullParser.StatementBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#StatementForBlock.
    def visitStatementForBlock(self, ctx:llullParser.StatementForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#type_m.
    def visitType_m(self, ctx:llullParser.Type_mContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprAddSub.
    def visitExprAddSub(self, ctx:llullParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ExprCondition.
    def visitExprCondition(self, ctx:llullParser.ExprConditionContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#AtomID.
    def visitAtomID(self, ctx:llullParser.AtomIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#AtomNumber.
    def visitAtomNumber(self, ctx:llullParser.AtomNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#AtomString.
    def visitAtomString(self, ctx:llullParser.AtomStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#WriteLn.
    def visitWriteLn(self, ctx:llullParser.WriteLnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by llullParser#ReadLn.
    def visitReadLn(self, ctx:llullParser.ReadLnContext):
        return self.visitChildren(ctx)



del llullParser