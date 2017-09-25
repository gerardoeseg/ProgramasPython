import math
import pprint

def sen(grados):
    return math.sin(math.radians(grados))
def cos(grados):
    return math.sin(math.radians(grados))
print ("Proyecciones Cartograficas\n")

datos = []
x = []
y = []

with open("LongitudLatitud.txt") as archivo:
    for line in archivo:
        # Metodo 'append' va agregando los valores en la lista
        # Separa cada elemento de acuerdo al separador con 'split' ('\t')
        datos.append([float(n) for n in line.strip().split('\t')])

    # Divide los elementos y los asigna a una variable, los trata como numeros
    for pair in datos:
        try:
            x, y = pair[0], pair[1]
            # Se realiza cualquier operacion
            print "El valor de x es: %f\tEl valor de y es: %f" % (x, y)
        except IndexError:
            print "No hay suficientes entradas."
# Se cierra el archivo
archivo.close()
