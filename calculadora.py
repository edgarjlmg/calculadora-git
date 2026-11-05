# calculadora.py
"""
Calculadora modular en Python.
Módulo básico para la práctica de control de versiones con Git y GitHub.
"""


def presentacion():
    """Muestra el mensaje de bienvenida y título del programa."""
    print("====================================")
    print("  CALCULADORA MODULAR EN PYTHON     ")
    print("====================================")


def sumar(a, b):
    """Retorna la suma de dos números (a + b)."""
    return a + b


def restar(a, b):
    """Retorna la resta de dos números (a - b)."""
    return a - b


def multiplicar(a, b):
    """Retorna el producto de dos números (a * b)."""
    return a * b


def dividir(a, b):
    """
    Retorna la división de dos números (a / b).
    Valida y controla el caso de división entre cero.
    """
    if b == 0:
        return "Error: no es posible dividir entre cero"
    return a / b


if __name__ == "__main__":
    presentacion()
