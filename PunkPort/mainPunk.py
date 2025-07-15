from PunkPort import lexer
from PunkPort2 import parser
from pprint import pprint

from ast_visual import construir_ast, imprimir_ast_visual


# leer codigo desde el archivo
nombre_archivo = "scan.punk"

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        data = archivo.read()
except FileNotFoundError:
    print(f" Error: El archivo '{nombre_archivo}' no fue encontrado.")
    exit(1)

# 1. ANALIZADOR LÉXICO 
print("== TOKENS RECONOCIDOS ==")
lexer.input(data)

tokens_encontrados = []
errores = []

while True:
    tok = lexer.token()
    if not tok:
        break
    token_info = {
        'Tipo': tok.type,
        'Valor': tok.value,
        'Linea': tok.lineno,
        'Posicion': tok.lexpos
    }
    tokens_encontrados.append(token_info)

# Mostrar tokens en formato de tabla
print(f"{'Tipo':<15}{'Valor':<20}{'Linea':<10}{'Posicion'}")
print("-" * 60)
for tok in tokens_encontrados:
    print(f"{tok['Tipo']:<15}{str(tok['Valor']):<20}{tok['Linea']:<10}{tok['Posicion']}")

# 2. ANALISIS SINTACTICO
print("\n== ANALISIS SINTACTICO ==")
# Manejamos error de parser manualmente
parser_error_occurred = False

def custom_error(p):
    global parser_error_occurred
    parser_error_occurred = True
    if p:
        print(f" Error de sintaxis en '{p.value}' (linea {p.lineno})")
    else:
        print(" Error de sintaxis: entrada inesperada (posiblemente EOF)")

# Asignar función personalizada de error
parser.errorfunc = custom_error

try:
    resultado = parser.parse(data)

    if parser_error_occurred or resultado is None:
        print(" Analisis sintactico fallido.")
    else:
        print(" Analisis sintactico exitoso.")
        print("== Arbol Sintactico ==")
        pprint(resultado, width=80)

        # === 3. Árbol AST ===
        print("\n== ARBOL DE SINTAXIS ABSTRACTA (AST) ==")
        ast_raiz = construir_ast(resultado)
        imprimir_ast_visual(ast_raiz)

except Exception as e:
    print(" Error durante el analisis sintactico:")
    print(str(e))