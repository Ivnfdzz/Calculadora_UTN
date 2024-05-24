def suma(a: int, b: int)-> int:
    """Calcula la suma de dos numeros

    Args:
        a (int): Primer operando
        b (int): Segundo operando

    Returns:
        int: Resultado de la suma
    """
    return a + b

def resta(a: int, b: int)-> int:
    """Calcula la resta de dos numeros

    Args:
        a (int): Primer operando
        b (int): Segundo operando

    Returns:
        int: Resultado de la resta
    """
    return a - b

def multiplicacion(a: int, b: int)-> int:
    """Calcula la multiplicación entre dos numeros

    Args:
        a (int): Primer operando
        b (int): Segundo operando

    Returns:
        int: Resultado de la multiplicación
    """
    return a * b

def division(a: int, b: int)-> int:
    """Calcula la division entre dos numeros

    Args:
        a (int): Primer operando
        b (int): Segundo operando

    Returns:
        int: Resultado de la división
    """
    return a / b

def factorial(n:int)->int:
    """Calcula el factorial de un numero

    Args:
        n (int): Numero cuyo factorial queremos calcular

    Raises:
        ValueError: Excepción en caso de recibir un valor negativo

    Returns:
        int: Retorna el factorial del numero ingresado
    """
    if n < 0:
        raise ValueError("No hay factorial de negativos")
    
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n-1)
    return fact