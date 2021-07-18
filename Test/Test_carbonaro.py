import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from modules.emit import *
from modules.lex import *
from modules.parse import *
import sys
 

class Testing():

    def __init__(self):
        self.test_()

        self.test_2()

        self.test_3()


    def test_(self):

        with open('./examples/example.carb', 'r') as inputFile:
            input = inputFile.read()

        lexer = Lexer(input)
        emitter = Emitter("out_1.txt")
        parser = Parser(lexer, emitter)

        parser.program() 
        emitter.writeFile() 

        with open('out_1.txt', 'rb') as f:
            file_1 = f.read()
        
        with open('./out_correct/out_correct_1.txt', 'rb') as f:
            file_2 = f.read()
        assert file_1 == file_2, "Failure in test 1"
        print('Passed test number 1 successfully')

    def test_2(self):
        with open('./examples/example2.carb', 'r') as inputFile:
            input = inputFile.read()

        lexer = Lexer(input)
        emitter = Emitter("out_1.txt")
        parser = Parser(lexer, emitter)

        parser.program() 
        emitter.writeFile() 

        with open('out_1.txt', 'rb') as f:
            file_1 = f.read()
        
        with open('./out_correct/out_correct_2.txt', 'rb') as f:
            file_2 = f.read()
        assert file_1 == file_2, "Failure in test 2"
        print('Passed test number 2 successfully')


    def test_3(self):
        with open('./examples/example3.carb', 'r') as inputFile:
            input = inputFile.read()

        lexer = Lexer(input)
        emitter = Emitter("out_1.txt")
        parser = Parser(lexer, emitter)

        parser.program() 
        emitter.writeFile() 

        with open('out_1.txt', 'rb') as f:
            file_1 = f.read()
        
        with open('./out_correct/out_correct_3.txt', 'rb') as f:
            file_2 = f.read()
        assert file_1 == file_2, "Failure in test 2"
        print('Passed test number 3 successfully')    



if __name__ == '__main__':
    Testing()
    print('Passed all tests successfully')