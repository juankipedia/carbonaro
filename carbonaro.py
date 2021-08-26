from modules.lex import *
from modules.emit import *
from modules.parse import *
import sys

def compile(source_code, output_name):
    lexer = Lexer(source_code)
    emitter = Emitter(output_name)
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.

    print("Compiling completed.")
    
    return emitter.code

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    compile(input, "out.c")
