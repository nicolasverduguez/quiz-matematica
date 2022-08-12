
# Funciones de calculo

import random


def obtenerOperandos(nivelDeDificultad):

    # Devuelve los numeros que se usaran en la operación

    num1 = None
    num2 = None
    
    if nivelDeDificultad == 1:
        num1 = random.randint(5,20)
        num2 = random.randint(5,20)
    else:
        num1 = random.randint(20,50)
        num2 = random.randint(20,50)

    return (num1,num2)


def generarCalculo(num, otroNum):

    # Genera la pregunta y retorna una tupla con el resultado
    # de dicha pregunta y el operador utilizado

    operacionAleatoria = random.choice(['+','-','*','/'])
    resultado = None

    print(f'¿Cuanto es {num} {operacionAleatoria} {otroNum}?\n')

    if operacionAleatoria == '+':
        resultado = num + otroNum
    elif operacionAleatoria == '-':
        resultado = num - otroNum
    elif operacionAleatoria == '*':
        resultado = num * otroNum
    else:
        resultado = num / otroNum

    return (resultado,operacionAleatoria)