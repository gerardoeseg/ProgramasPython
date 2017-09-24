# numera_lineas2.py
# Imprime las lineas de un archivo con su numero
# Extraido de: https://goo.gl/A7G9Fo

# Se lee archivo
archivo = open("archivo.txt")
for i, linea in enumerate(archivo):
    linea = linea.rstrip("\\n")
    print " %4d: %s" % (i, linea)
archivo.close()
