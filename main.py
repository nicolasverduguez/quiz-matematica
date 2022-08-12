
# -- Quiz de Matematicas

from calculo import *
from verificacion import *


opcion = None

print(' Quiz Matematico '.center(35,'-'))
print('1. Jugar')
print('2. Salir\n')

while opcion not in [1,2]:
    try:
        opcion = int(input('-> Opcion: '))
        alerta(opcion,1,2)
    except:
        mssg()

if opcion == 1:

    while opcion != 0:

        dificultad = None
        contadorPuntos = 0
        opcion = None
        turno = 0

        print('\n',' Seleccione Dificultad '.center(45,'-'))
        print('1. Normal')
        print('2. Dificil\n')

        while opcion not in [1,2]:
            try:
                opcion = int(input('-> Opcion: '))
                dificultad = opcion
                alerta(opcion,1,2)
            except:
                mssg()

        while turno < 10:

            print(f'\n---------- PREGUNTA {turno + 1} ----------')
            operando1, operando2 = obtenerOperandos(dificultad)
            resultado, operacion = generarCalculo(operando1, operando2)
            rtaUsuario = None
            esCorrecta = None
            valorPermitido = False

            while not valorPermitido:
                try:
                    if operacion != '/':
                        rtaUsuario = int(input('-> Respuesta: '))
                    else:
                        rtaUsuario = float(input('-> Respuesta(agregue 2 decimas): '))
                        resultado = round(resultado,2)
                    valorPermitido = True
                except:
                    mssg()

            esCorrecta = respuestaCorrecta(rtaUsuario,resultado)
            if esCorrecta:
                contadorPuntos += 10
            turno += 1

        print(f'\nPuntaje final: {contadorPuntos}')
        print(f'Respuestas correctas: {int(contadorPuntos / 10)} de 10')

        opcion = None

        print('¿Jugar de nuevo?')
        print('NO -> 0 | SI -> 1\n')

        while opcion not in [0,1]:
            try:
                opcion = int(input('-> Opcion: '))
                alerta(opcion,0,1)
            except:
                mssg()

    print(' FIN DEL JUEGO '.center(45,'-'))

else:

    print(' FIN DEL JUEGO '.center(45,'-'))