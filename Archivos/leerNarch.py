# Programa que lee dos numeros de un archivo separados por una coma lee la
# linea, separa la cadena identificando una ',' como separador de los numeros
# despues, se hace un cast y se guarda cada uno en una variable

datos = []  # Lista (arreglo) donde se van a guardar los dos numeros
# Suponiendo que existe un archivo 'numeros' lo abre y lo guarda en 'archivo'
with open("numeros.txt") as archivo:
    # Lee la linea del archivo
    for line in archivo:
        # Metodo 'append' va agregando los valores en la lista
        # Separa cada elemento de acuerdo al separador con 'split' (',')
        datos.append([int(n) for n in line.strip().split(',')])
# Divide los elementos y los asigna a una variable, los trata como numeros
for pair in datos:
    try:
        x, y = pair[0], pair[1]
        # Se realiza cualquier operacion
        suma = x + y
        print "El valor de 'x':", x
        print "El valor de 'y':", y
        print "La suma de 'x' y 'y' es:", suma
    except IndexError:
        print "No hay suficientes entradas."
# Se cierra el archivo
archivo.close()
