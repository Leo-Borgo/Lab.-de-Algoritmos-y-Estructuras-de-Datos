import time, os, random
os.system("cls")

glosario = {
    "variable": "Espacio en memoria para almacenar un valor.",
    "funcion": "Bloque de código reutilizable que realiza una tarea específica.",
    "condicion": "Expresión lógica que determina el flujo del programa (if, else).",
    "bucle": "Estructura que repite un bloque de código (for, while).",
    "objeto": "Instancia de una clase en programación orientada a objetos.",
    "algoritmo": "Conjunto de pasos ordenados y finitos que resuelven un problema o realizan una tarea específica.",
    "array": "Estructura de datos que almacena múltiples valores en una sola variable.",
    "clase": "Plantilla o modelo en la programación orientada a objetos que define atributos y métodos para crear objetos.",
    "compilador": "Programa que traduce código fuente escrito en un lenguaje de programación a código máquina para que el procesador pueda ejecutarlo.",
    "depuracion": "Proceso de identificar y corregir errores o fallos en el código de un programa.",
}

for key, value in glosario.items():
    print(f"\n{key}", ":")
    print(f"{value}"), time.sleep(1)