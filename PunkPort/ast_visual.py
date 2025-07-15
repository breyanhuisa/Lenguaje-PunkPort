from anytree import Node, RenderTree

# Función para convertir el árbol sintáctico (tupla) a árbol visual
def construir_ast(nodo, nombre="raíz"):
    if isinstance(nodo, tuple):
        etiqueta = nodo[0]
        actual = Node(etiqueta)
        for subnodo in nodo[1:]:
            hijo = construir_ast(subnodo)
            if hijo:
                hijo.parent = actual
        return actual
    elif isinstance(nodo, list):
        padre = Node("lista")
        for item in nodo:
            hijo = construir_ast(item)
            if hijo:
                hijo.parent = padre
        return padre
    else:
        return Node(str(nodo))
    
def imprimir_ast_visual(raiz):
    print("== ARBOL DE SINTAXIS ABSTRACTA (AST) ==")
    for pre, fill, node in RenderTree(raiz):
        print(f"{pre}{node.name}")