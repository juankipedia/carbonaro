# Carbonaro

Carbonaro is an small compiler built with the purpose of learning how compilers work.

It supports:

- Numerical variables
- Basic arithmetic
- If statements
- While loops
- Print text and numbers
- Input numbers
- Labels and goto
- Comments

Take a look at docs to see an example code and language grammar.

## How to install

The compiler will work with python3

The code formatter is `clang-format`, to install it use

    brew install clang-format

## Some useful commands

Format every .c under tests/ directory

    find tests/ -iname '\*.c' | xargs clang-format -i -style=Microsoft
