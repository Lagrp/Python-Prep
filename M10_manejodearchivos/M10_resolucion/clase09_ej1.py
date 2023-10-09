

#1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección,
# verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos

import sys

if len(sys.argv)==4:
    print(f'el primer parametro ingresado es {sys.argv[1]} -> {type(sys.argv[1])}')
    print(f'el segundo parametro ingresado es {sys.argv[2]} -> {type(sys.argv[2])}')
    print(f'el tercero parametro ingresado es {sys.argv[3]} -> {type(sys.argv[3])}')
else:
    print('Error: no hay los paraetros necesarios')
    print(f'Ejemplo {sys.argv[0]} 1 2 3')