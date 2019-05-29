'''Este módulo contiene el código fuente para probar las clases de las
   compuertas lógicas (CompuertaAND y CompuertaOR)
   Solicita al usuario los parámetros de entrada para las compuertas,
   realiza la operación de la compuerta seleccionada y retorna la salida.
'''

from Taller_3.compuerta.compuerta import CompuertaAND
from Taller_3.compuerta.compuerta import CompuertaOR

SELECCION_OK = False
while not SELECCION_OK:
    print("BIENVENIDO")
    print("Seleccione la compuerta que desea trabajar (1 o 2):")
    print("1 - Compuerta AND")
    print("2 - Compuerta OR")
    OPCION = input()
    if OPCION not in ('1', '2'):
        print("Opción ingresada no válida")
        print(" ")
    else:
        SELECCION_OK = True

if OPCION == '1':
    COMP_LOGICA = CompuertaAND()
else:
    COMP_LOGICA = CompuertaOR()
SELECCION_OK = False
while not SELECCION_OK:
    print("Ingrese Valor puerta A: ")
    VALOR = input()
    if COMP_LOGICA.set_entrada_a(VALOR):
        SELECCION_OK = True
    else:
        print("Valor entrada A No válido. Debe ser 1 o 0")
SELECCION_OK = False
while not SELECCION_OK:
    print("Ingrese Valor puerta B: ")
    VALOR = input()
    if COMP_LOGICA.set_entrada_b(VALOR):
        SELECCION_OK = True
    else:
        print("Valor entrada B No válido. Debe ser 1 o 0")
COMP_LOGICA.operar()
print("Resultado: " + COMP_LOGICA.get_salida_x())
