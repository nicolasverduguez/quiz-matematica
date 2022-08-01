
from calculo import *
from verificacion import *


JUGAR = 1
SALIR = 2
NORMAL = 1
DIFICIL = 2
NO = 0
SI = 1

opcion = None

print('Quiz Matematico'.center(45,'-'))
print('1. Jugar')
print('2. Salir\n')

while not esValido(opcion, JUGAR, SALIR):
    try:
        opcion = int(input('-> : '))
        mssgEsValido(opcion, JUGAR, SALIR)
    except:
        print('Valor incorrecto. Intente nuevamente\n')

if opcion == JUGAR:

    while opcion != NO:

        opcion = None
        turno = 0
        contadorPuntos = 0

        print('\n','Seleccione Dificultad'.center(45,'-'))
        print('1. Normal')
        print('2. Dificil\n')


        while not esValido(opcion, NORMAL, DIFICIL):
            try:
                opcion = int(input('>: '))
                mssgEsValido(opcion, NORMAL, DIFICIL)
            except:
                print('Valor incorrecto. Intente nuevamente\n')


        print('')
        

        while turno < 10:

            print(f'PREGUNTA {turno + 1}'.center(40,'-'))
            rtaCorrecta, op = calculo(opcion)
            rta = None

            if op != '/':
                while not esEntero(rta):
                    try:
                        rta = int(input('>: '))
                    except:
                        print('Valor incorrecto. Intente de nuevo')
            else:
                while not esFlotante(rta):
                    try:
                        rta = float(input('>: '))
                    except:
                        print('Valor incorrecto. Intente de nuevo')
            
            if respuestaCorrecta(rta, rtaCorrecta):
                contadorPuntos += 10
            turno += 1


        print(f'Puntaje final: {contadorPuntos}')
        print(f'Respuestas correctas: {int(contadorPuntos / 10)} de 10')

        opcion = None

        print(f'¿Jugar de nuevo?\nNO -> 0 | SI -> 1\n')

        while not esValido(opcion, NO, SI):
            try:
                opcion = int(input('>: '))
                mssgEsValido(opcion, NO, SI)
            except:
                print('Valor incorrecto. Intente nuevamente\n')

    print('Fin del juego'.center(45,'-'))

else:

    print('Fin del juego'.center(45,'-'))