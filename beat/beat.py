import sys
from antlr4 import *
from llullLexer import llullLexer
from llullParser import llullParser
from antlr4.InputStream import InputStream
from BeatVisitor import BeatVisitor
from termcolor import colored


if len(sys.argv) > 1:
   input_stream = FileStream(sys.argv[1])
else:
	input_stream = InputStream(input('? '))

lexer = llullLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = llullParser(token_stream)
tree = parser.root()
#print(tree.toStringTree(recog=parser))
visitorBeat = BeatVisitor()

#print(list_parameters)
visitorBeat.visit(tree)
