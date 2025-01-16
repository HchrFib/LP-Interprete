import sys
from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from antlr4.InputStream import InputStream
from EvalVisitor import EvalVisitor


list_parameters = []
if len(sys.argv) > 1:
   input_stream = FileStream(sys.argv[1])
else:
	input_stream = InputStream(input('? '))

lexer = llullLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = llullParser(token_stream)
tree = parser.root()
#print(tree.toStringTree(recog=parser))
visitorEval = EvalVisitor()

if len(sys.argv)  <= 2:
	visitorEval.setUp("main", [], False)
else:
	i = 3

	while i < len(sys.argv):
		list_parameters.append(sys.argv[i])
		i = i + 1

	visitorEval.setUp(sys.argv[2], list_parameters, True)


#print(list_parameters)
visitorEval.visit(tree)
