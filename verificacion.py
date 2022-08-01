
# Funciones verificacion

def esValido(var1, var2, var3):
    return var1 == var2 or var1 == var3


def mssgEsValido(var1, var2, var3):
    if not esValido(var1, var2, var3):
        print('Valor incorrecto, ingrese valor nuevamente')


def esEntero(var):
    return type(var) == type(0)


def esFlotante(var):
    return type(var) == type(0.0)


def respuestaCorrecta(rta, rtaCorrecta):

    '''
    Verifica si rta es igual a rtaCorrecta e imprime un 
    mensaje de acuerdo al valor de verdad de dicha igualdad
    '''

    esCorrecto = rta == rtaCorrecta

    if esCorrecto:
        print('Correcto\n')
        return True
    else:
        print(f'Incorrecto. La respuesta era: {rtaCorrecta}\n')
        return False