import ply.yacc as yacc
from PunkPort import tokens

# ---------------------
# Precedencia de operadores
# ---------------------
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# ---------------------
# Reglas del parser
# ---------------------

# Programa principal
def p_program(p):
    '''program : statements'''
    p[0] = ('program', p[1])

# Múltiples statements
def p_statements_multiple(p):
    '''statements : statement statements'''
    p[0] = [p[1]] + p[2]

def p_statements_single(p):
    '''statements : statement'''
    p[0] = [p[1]]

# Importación de módulos
def p_statement_import(p):
    '''statement : MOD IDENTIFIER DOUBLECOLON'''
    p[0] = ('import', p[2])

# Declaración de funciones
def p_statement_funcdef(p):
    '''statement : FNX IDENTIFIER LBRACKET paramlist RBRACKET BLOCK_START statements BLOCK_END'''
    p[0] = ('function_def', p[2], p[4], p[7])

# Parámetros
def p_paramlist_single(p):
    '''paramlist : type IDENTIFIER'''
    p[0] = [(p[1], p[2])]

def p_paramlist_multiple(p):
    '''paramlist : type IDENTIFIER COMMA paramlist'''
    p[0] = [(p[1], p[2])] + p[4]

# Tipos de datos
def p_type(p):
    '''type : TXT
            | I32
            | F64'''
    p[0] = p[1]

# Asignaciones (única regla válida)
def p_statement_assignment(p):
    '''statement : LET type IDENTIFIER ASSIGN expression DOUBLECOLON'''
    p[0] = ('assign', p[2], p[3], p[5])

# Expresiones numéricas, identificadores, strings, agrupadas
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GT expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_atomic(p):
    '''expression : IDENTIFIER
                  | NUMBER'''
    p[0] = p[1]

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = ('string', p[1])

# If condicional
def p_statement_if(p):
    '''statement : IF LBRACKET expression RBRACKET BLOCK_START statements BLOCK_END'''
    p[0] = ('if', p[3], p[6])

# Llamadas a funciones
def p_statement_funccall(p):
    '''statement : IDENTIFIER LPAREN args RPAREN DOUBLECOLON'''
    p[0] = ('call', p[1], p[3])

def p_args_single(p):
    '''args : expression'''
    p[0] = [p[1]]

def p_args_multiple(p):
    '''args : expression COMMA args'''
    p[0] = [p[1]] + p[3]

# Manejo de errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis: entrada inesperada")

# ---------------------
# Construcción del parser
# ---------------------
parser = yacc.yacc()
