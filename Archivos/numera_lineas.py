# numera_lineas.py
# Imprime las lineas de un archivo con su numero
# Extraido de: https://goo.gl/A7G9Fo

# Se lee archivo
archivo = open("archivo.txt")
i = 1
for linea in archivo:
    # 'rstrip' es necesario para remover el fin de linea de cada linea
    # que se lee del archivo
    linea = linea.rstrip("\\n")
    print " %4d: %s" % (i, linea)
    i += 1
archivo.close()
