# PunkPort: Analizador Léxico y Sintáctico

Este proyecto implementa un **analizador léxico y sintáctico** para un lenguaje personalizado llamado **PunkPort**, diseñado con estilo técnico y rebelde. El analizador está construido con **Python** utilizando las bibliotecas `PLY` y `anytree`.

## ➕ Árbol de Sintaxis Abstracta (AST)
Si el análisis tiene éxito, se genera un AST jerárquico utilizando anytree, y se imprime en la terminal en forma visual.
---

## ⚙️ Requisitos

Instala los siguientes paquetes antes de ejecutar el proyecto:

bash
pip install ply
pip install anytree

## 📁 Estructura del Proyecto

```plaintext
PunkPort/
├── ast_visual.py         # Visualización del AST usando anytree
├── mainPunk.py           # Punto de entrada principal del analizador
├── parser.out            # Salida de PLY (parser)
├── parsetab.py           # Tabla generada automáticamente por PLY
├── PunkPort.py           # Analizador léxico (lexer)
├── PunkPort2.py          # Analizador sintáctico (parser)
├── scan.punk             # Ejemplo 1 válido
├── operation.punk        # Ejemplo 2 válido
├── badscan.punk          # Ejemplo 1 con errores
├── badoperation.punk     # Ejemplo 2 con errores
├── README.md             # Este archivo
└── __pycache__/          # Archivos generados por Python

