
# Funciones de verificación


def mssg():
    print('Valor incorrecto, ingrese valor nuevamente\n')


def alerta(valorIngresado, var1, var2):
    if valorIngresado not in [var1, var2]:
        mssg()


def respuestaCorrecta(rtaDelUsuario, rtaCorrecta):

    # Verifica si la respuesta del usuario es correcta y retorna el valor de verdad 
    # correspondiente junto con un mensaje de consola 

    esCorrecto = rtaDelUsuario == rtaCorrecta

    if esCorrecto:
        print('Correcto')
    else:
        print(f'Incorrecto. La respuesta era: {rtaCorrecta}')

    return esCorrecto