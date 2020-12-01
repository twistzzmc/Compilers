import sys
import ply.yacc as yacc
import last_parser
import TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = last_parser.parser
    # parser = yacc.yacc(module=Mparser)
    text = file.read()
    ast = parser.parse(text, lexer=last_parser.scanner.lexer)
    ast.printTree()