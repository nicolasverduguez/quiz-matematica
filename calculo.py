
# Funciones calculo

import random


def calcular(num1, num2):

    '''
    Imprime una pregunta al jugador y devuelve el resultado 
    de la operacion entre num1 y num2 junto con el operador
    '''

    op = random.choice(['+','-','*','/'])

    if op == '+':
        print(f'¿Cuanto es {num1} + {num2}?')
        return (num1 + num2, '+')
    elif op == '-':
        print(f'¿Cuanto es {num1} - {num2}?')
        return (num1 - num2, '-')
    elif op == '*':
        print(f'¿Cuanto es {num1} * {num2}?')
        return (num1 * num2, '*')
    elif op == '/':
        print(f'¿Cuanto es {num1} / {num2}? (Incluya 1 decima)')
        return (round(num1 / num2, 1), '/')


def calculo(dificultad):

    '''
    Devuelve el resultado de aplicar a la funcion calculo 
    valores aleatorios de acuerdo al valor de dificultad
    '''

    num1 = None
    num2 = None

    if dificultad == 1:
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
    else:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)

    return calcular(num1, num2)