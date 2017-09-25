# Programa que a partir de un archivo obtiene sus valores y los pasa a una variable
# Se opera con las variables y se imprimen los valores en un archivo 
import math

def sen(grados):
    return math.sin(math.radians(grados))
def cos(grados):
    return math.sin(math.radians(grados))
print ("Proyecciones Cartograficas\n")

datos = []

with open("LongitudLatitud.txt") as archivo:
    for line in archivo:
        # Metodo 'append' va agregando los valores en la lista
        # Separa cada elemento de acuerdo al separador con 'split' ('\t')
        datos.append([float(n) for n in line.strip().split('\t')])

    with open("Resultado.txt", "w+") as resultado:
        # Divide los elementos y los asigna a una variable, los trata como numeros
        for pair in datos:
            try:
                # Los valores leidos del archivo tienen su 'x' y 'y' correspondiente
                x, y = pair[0], pair[1]

                # Se realiza cualquier operacion
                formula = x + y

                # Se imprime la longitud, latitud y el resultado de la formula
                # '%.5f' indica que solo va a imprimir el valor con 5 decimales
                print "Longitud: %.5f\tLatitud: %.5f\tResultado: %.5f" % (x, y, formula)

                # Imprime en archivo
                resultado.write("Longitud: ")
                resultado.write("%.5f" % x)
                resultado.write("\tLatitud: ")
                resultado.write("%.5f" % y)
                resultado.write("\tResultado: ")
                resultado.write("%.5f\n" % formula)

            # En caso de error imprime un mensaje
            except IndexError:
                print "No hay suficientes entradas."
    # Cierra archivo de resultados
    resultado.close()
# Se cierra el archivo
archivo.close()
