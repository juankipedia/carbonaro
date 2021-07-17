import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from modules import emit
from modules import lex
from modules import parse

class Testing():

    def __init__(self):
        self.test_()

        #self.tes2()


    def test_(self):

        if len(sys.argv) != 2:
            sys.exit("Error: Compiler needs source file as argument.")
        with open(sys.argv[1], 'r') as inputFile:
            input = inputFile.read()

        # Initialize the lexer, emitter, and parser.
        lexer = Lexer(input)
        emitter = Emitter("out_1.txt")
        parser = Parser(lexer, emitter)

        parser.program() # Start the parser.
        emitter.writeFile() # Write the output to file.

        with open('out_1.txt', 'rb') as f:
            file_1 = f.read()
        
        with open('./out-correct/out_correct1.txt', 'rb') as f:
            file_2 = f.read()

        assert file_1 == file_2, "Doesnt Match"
    def test2(self):
        pass



if __name__ == '__main__':
    Testing()
    print('All good.')