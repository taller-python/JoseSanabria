'''It performs operations (sum, subtraction, multiplication and division)
  with numbers from a Excel file and it writes results on a flat file

Args:
    path (string): Excel file path

Returns:
    ARCHIVO_SALIDA (flat file): Flat file with result of operations
'''

import sys
import os.path
import openpyxl


def calcular(oper, num1, num2):
    '''Perform the operation (sum, subtraction, multiplication and division)
      with the two numbers

    Args:
        oper (string): Operation to perform (SUMA, RESTA, MULTIPLICACIÓN
           and DIVISIÓN)
        num1 (int, float): Number 1 to opertate
        num2 (int, float): Number 2 to opertate

    Returns:
        result (string): Result of perform the string operation with the
           two numbers.
    '''
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if oper == 'SUMA':
            result = str(num1 + num2)
        elif oper == 'RESTA':
            result = str(num1 - num2)
        elif oper == 'MULTIPLICACIÓN':
            result = str(num1 * num2)
        elif oper == 'DIVISIÓN':
            try:
                result = str(num1 / num2)
            except ZeroDivisionError:
                result = 'Error'
    else:
        result = 'Error'
    return result

print("ingrese ruta y nombre del archivo excel")
RUTA = input()
# RUTA = 'C:\\Users\josesanabria\PycharmProjects\Retos_Seti\Taller_2\Fuente\operaciones.xlsx'
# RUTA = '.\Taller_2\Fuente\operaciones.xlsx'
if not os.path.exists(RUTA):
    print("Error leyendo archivo excel")
    sys.exit()
DOCEXCEL = openpyxl.load_workbook(RUTA)
# with open('./Taller_2/Salida/resultadoOperaciones.txt', 'w') as ARCHIVO_SALIDA:
with open('./resultadoOperaciones.txt', 'w') as ARCHIVO_SALIDA:
    ARCHIVO_SALIDA.write('')
for hoja in DOCEXCEL:
    c = 0
    with open('./resultadoOperaciones.txt', 'a') as ARCHIVO_SALIDA:
        ARCHIVO_SALIDA.write(hoja.title + '\n')
    for fila in hoja:
        if c > 0:
            resultado_calcular = calcular(str(hoja.title.upper()), fila[0].value, fila[1].value)
            # ARCHIVO_SALIDA.write(resultado_calcular + '\n')
            with open('./resultadoOperaciones.txt', 'a') as ARCHIVO_SALIDA:
                ARCHIVO_SALIDA.write(resultado_calcular + '\n')
        c += 1
    with open('./resultadoOperaciones.txt', 'a') as ARCHIVO_SALIDA:
        ARCHIVO_SALIDA.write('\n')
