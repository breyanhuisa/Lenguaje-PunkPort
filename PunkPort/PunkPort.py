import ply.lex as lex

# Lista de tokens
tokens = [
    'MOD', 'FNX', 'LET', 'TXT', 'I32', 'F64', 
    'STRING', 'IDENTIFIER',
    'ASSIGN', 'DOUBLECOLON', 
    'LPAREN', 'RPAREN', # ( )
    'LBRACKET', 'RBRACKET', # [ ]
    'LANGLE', 'RANGLE', # < >
    'BLOCK_START', 'BLOCK_END', # @{ }@
    'COMMA', 
    'IF', 'GT', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE'
]

# Palabras clave (reservadas)
reserved = {
    'mod': 'MOD',
    'fnx': 'FNX',
    'let': 'LET',
    'txt': 'TXT',
    'i32': 'I32',
    'f64': 'F64',
    'if': 'IF' 
}

# Tokens simples (simbolos del lenguaje)
t_ASSIGN        = r':='
t_DOUBLECOLON   = r'::'
t_LPAREN        = r'\(' # PARA OPERACIONES MATEMATICAS
t_RPAREN        = r'\)' 
t_LBRACKET      = r'\[' # PARA FUNCIONES O ESTRUCTURAS DE CONTROL
t_RBRACKET      = r'\]'
# t_LANGLE        = r'\(' # para llamar funciones
# t_RANGLE        = r'\)'
t_BLOCK_START   = r'@\{'
t_BLOCK_END     = r'\}@'
t_COMMA         = r','
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_GT            = r'>'

# Definir token para numeros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Literales tipo string (dobles comillas)
def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Eliminar comillas
    return t

# Identificadores (nombres de variables, funciones, etc.)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verifica si es palabra clave
    return t

# Comentarios (ignorados)
def t_COMMENT(t):
    r'\#.*'
    pass  # Ignorar el comentario sin generar token

# Saltos de linea (importante para contar líneas)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para encontrar columna (posición en linea)
def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return token.lexpos - last_cr

# Manejo de errores léxicos
def t_error(t):
    line = t.lexer.lineno
    col = find_column(t.lexer.lexdata, t)
    print(f"[LEXICO] Caracter ilegal '{t.value[0]}' en linea {line}, columna {col}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
