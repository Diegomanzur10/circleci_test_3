## Simulacion de una calculadora

def suma(a: float, b: float) -> float:
    return a + b

def resta(a: float, b: float) -> float:
    return a - b

def multiplicacion(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 1