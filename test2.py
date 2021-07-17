from modules.emit import *
from modules.lex import *
from modules.parse import *
import sys

class Testing():

    def __init__(self):
        self.test_()
        # self.test2()


    def test_(self):
        print('Entro aca')
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
        
        with open('out.txt', 'rb') as f:
            file_2 = f.read()

        assert file_1 == file_2, "Doesnt Match"


    def test2(self):
        assert 1 == 2, "Must fail"

if __name__ == '__main__':
    Testing()
    print('All good.')