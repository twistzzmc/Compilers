# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('A_ADD', 'A_DIV', 'A_MUL', 'A_SUB', 'BREAK', 'CONTINUE', 'ELSE', 'EQ', 'EYE', 'FLOAT', 'FOR', 'GE', 'ID', 'IF', 'INT', 'LE', 'M_ADD', 'M_DIV', 'M_MUL', 'M_SUB', 'M_TRANSPOSE', 'NEQ', 'ONES', 'PRINT', 'RETURN', 'STRING', 'WHILE', 'ZEROS'))
_lexreflags   = 64
_lexliterals  = '+-*/=<>()[]{}:,;'
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_FLOAT>\\d*((\\d\\.|\\.\\d)\\d*([Ee][+-]?\\d+)?|\\d([Ee][+-]?\\d+)))|(?P<t_INT>\\d+)|(?P<t_STRING>"([^"\\\\]|\\\\.)*")|(?P<t_newline>\\n+)|(?P<t_M_ADD>\\.\\+)|(?P<t_M_MUL>\\.\\*)|(?P<t_ignore_COMMENT>\\#.*)|(?P<t_A_ADD>\\+=)|(?P<t_A_MUL>\\*=)|(?P<t_M_SUB>\\.-)|(?P<t_M_DIV>\\./)|(?P<t_EQ>==)|(?P<t_NEQ>!=)|(?P<t_LE><=)|(?P<t_GE>>=)|(?P<t_A_SUB>-=)|(?P<t_A_DIV>/=)|(?P<t_TRANSPOSE>\\\')', [None, ('t_ID', 'ID'), ('t_FLOAT', 'FLOAT'), None, None, None, None, ('t_INT', 'INT'), ('t_STRING', 'STRING'), None, ('t_newline', 'newline'), (None, 'M_ADD'), (None, 'M_MUL'), (None, None), (None, 'A_ADD'), (None, 'A_MUL'), (None, 'M_SUB'), (None, 'M_DIV'), (None, 'EQ'), (None, 'NEQ'), (None, 'LE'), (None, 'GE'), (None, 'A_SUB'), (None, 'A_DIV'), (None, 'TRANSPOSE')])]}
_lexstateignore = {'INITIAL': '  \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
