from Matematicas.Funciones_matematicas import *
from os import system

def menu():
    """Muestra el menu de opciones

    Returns:
        Retorna un imput donde le pide al usuario que coloque una opción
    """
    system("cls")
    print(f"""
CALCULADORA:

1- Ingrese el primer operando
2- Ingresar el segundo operando
3- Operaciones
4- Mostrar resultado
5- Salir

A = {primer_operando}
B = {segundo_operando}
""")
    return input("Seleccione una opción: ").lower()

def opcion_uno():
    """Muestra el imput: "Ingrese el primer operando"

    Returns:
        Retorna un input pidiendole el primer operando al usuario
    """
    return (input("Ingrese el primer operando: "))

def opcion_dos():
    """Muestra el imput: "Ingrese el segundo operando"

    Returns:
        Retorna un input pidiendole el segundo operando al usuario
    """
    return (input("Ingrese el segundo operando: "))

def opcion_tres():
    """Muestra el menu de operaciones

    Returns:
        Retorna un input pidiendole al usuario que seleccione una opción
    """
    print("""
OPERACIONES:

a- Sumar
b- Restar
c- Multiplicar
d- Dividir
e- Factorial

""")
    return input("Ingrese una opción: ")

def opcion_cuatro():
    """Muestra el resultado de la operación realizada
    """
    print(f"El resultado de la {operacion_seleccionada} entre los numeros {primer_operando} y {segundo_operando} es: {resultado}")

def opcion_cuatro_factorial():
    """Muestra el resultado del factorial de los numeros ingresados
    """
    print(f"El factorial de {primer_operando} es: {resultado_1} y el factorial de {segundo_operando} es {resultado_2}")

def verificacion_isdigit(x)->bool:
    """Verifica si lo que ingreso el usuario es un digito

    Args:
        x (operando): Lo que ingreso el usuario dentro del operando

    Returns:
        bool: True o False dependiendo de si es o no un digito
    """
    verdad = x.isdigit()
    if verdad == False:
        x = None
        print("Ingrese un numero")
    else:
        x = int(x)
    return verdad

flag_opcion_a = False
flag_opcion_b = False
flag_opcion_c = False
operacion_seleccionada = None
primer_operando = "x"
segundo_operando = "y"

while True:
    match menu():
        case "1":
            primer_operando = opcion_uno()
            check_num = verificacion_isdigit(primer_operando)
            if check_num == False:
                primer_operando = "x"
            else:
                flag_opcion_a = True
                primer_operando = int(primer_operando)
            
        case "2":
            if flag_opcion_a == True:
                segundo_operando = opcion_dos()
                check_num = verificacion_isdigit(segundo_operando)
                if check_num == False:
                    segundo_operando = "y"
                else:
                    flag_opcion_b = True
                    segundo_operando = int(segundo_operando)
            else:
                print("Primero dame el primer operando")
            
        case "3":
            if flag_opcion_a == True and flag_opcion_b == True:
                flag_opcion_c = True
                match opcion_tres():
                    case "a":
                        resultado = suma(primer_operando, segundo_operando)
                        operacion_seleccionada = "suma"
                    case "b":
                        resultado = resta(primer_operando, segundo_operando)
                        operacion_seleccionada = "resta"
                    case "c":
                        resultado = multiplicacion(primer_operando, segundo_operando)
                        operacion_seleccionada = "multiplicacion"
                        
                    case "d":
                        try:
                            resultado = division(primer_operando, segundo_operando)
                        except ZeroDivisionError:
                            print("No se puede dividir por cero.")
                        operacion_seleccionada = "division"
                        
                    case "e":
                        resultado_1 = factorial(primer_operando)
                        resultado_2 = factorial(segundo_operando)
                        operacion_seleccionada = "factorial"
            else:
                print("Primero deberias pasarme los dos operandos")
            
        case "4":
            if operacion_seleccionada == "factorial":
                opcion_cuatro_factorial()
            else:
                if flag_opcion_a == False:
                    print("Primero deberias empezar por darme el primer operando")
                elif flag_opcion_b == False:
                    print("Antes tendrias que darme el segundo operando")
                elif flag_opcion_c == False:
                    print("No se realizo ninguna operación")
                else:
                    opcion_cuatro()
                
        case "5":
            break
            
        case _:            print("Error: Ingrese una opcion valida")
            
    system("pause")
    
print("Fin del programa.")