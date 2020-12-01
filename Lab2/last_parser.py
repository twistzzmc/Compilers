import numpy as np

import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ('left', '='),
    ('nonassoc', '<', '>', 'LE', 'GE'),
    ("left", '+', '-'),
    ("left", "*", "/"),
    ("left", 'M_ADD', 'M_SUB'),
    ("left", "M_MUL", "M_DIV"),
    ('right', 'UMINUS'),
    ("left", "M_TRANSPOSE"),
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE")
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(t):
    """program : instructions"""


def p_instructions(t):
    """instructions : instructions instruction
                | """


def p_empty_instruction(t):
    """instruction : ';'"""


def p_expression_value(t):
    """expression : INT
                  | FLOAT
                  | matrix
                  | STRING"""


def p_expression_ID(t):
    """expression : ID"""


def p_expression_gr(t):
    """expression : '(' expression ')'"""


def p_instruction_scope(t):
    """instruction : '{' instructions '}'"""


def p_expression_binop(t):
    """expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression"""


def p_expression_binop_matrix(t):
    """expression : expression M_ADD expression
                  | expression M_SUB expression
                  | expression M_MUL expression
                  | expression M_DIV expression"""


def p_expression_relation(t):
    """condition : expression '<' expression
                | expression '>' expression
                | expression LE expression
                | expression GE expression
                | expression NEQ expression
                | expression EQ expression"""


def p_uminus(t):
    """expression : '-' expression %prec UMINUS"""


def p_transpose(t):
    """matrix : expression M_TRANSPOSE"""


def p_matrix_generator(t):
    """matrix : ZEROS '(' expression ')'
              | ONES '(' expression ')'
              | EYE '(' expression ')'"""


def p_assignment(t):
    """instruction : ID '=' expression ';'
                    | ID A_ADD expression ';'
                    | ID A_SUB expression ';'
                    | ID A_MUL expression ';'
                    | ID A_DIV expression ';'"""


def p_position_assignment(t):
    """instruction : ID array '=' expression ';'
                   | ID array A_ADD expression ';'
                   | ID array A_SUB expression ';'
                   | ID array A_MUL expression ';'
                   | ID array A_DIV expression ';'"""  # A[0,1] = 5, etc.


def p_if_else(t):
    """instruction : IF '(' condition ')' instruction %prec IFX
                  | IF '(' condition ')' instruction ELSE instruction"""


def p_while(t):
    """instruction : WHILE '(' condition ')' instruction"""


def p_for(t):
    """instruction : FOR ID '=' expression ':' expression instruction"""


def p_special_instruction(t):
    """instruction : BREAK ';'
                   | CONTINUE ';'
                   | RETURN expression ';'"""


def p_print(t):
    """instruction : PRINT list ';'"""


def p_matrix(t):
    """matrix : '[' arraylist ']'"""


def p_arraylist(t):
    """arraylist : array
                 | arraylist ',' array"""


def p_array(t):
    """array : '[' list ']'"""


def p_list(t):
    """list : expression
            | list ',' expression"""


def p_array_access(t):
    """expression : ID array"""


parser = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            s = input('> > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)