# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo
# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo = nombre,apellido
print('El nombre completo es :',nombre_completo )

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
#pais = 'Argentina'
#argentina_len = len(pais)
#print(pais, 'tiene', argentina_len, 'caracteres')
nombre_letras = nombre+apellido
cantidad_letras = len(nombre_letras)
print ('El nombre completo tiene',cantidad_letras,'letras')