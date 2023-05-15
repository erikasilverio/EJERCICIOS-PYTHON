"""
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre
del mes en letras ("abril"). Verificar que el mes sea válido e informar
en caso que no lo sea.
"""

import random


# numero_mes = int(input("Numero de mes: "))
numero_mes = random.randint(1,12)

if numero_mes == 1:
    nombre = "enero"
elif numero_mes == 2:
    nombre = "febrero"
elif numero_mes == 3:
    nombre = "febrero"
elif numero_mes == 4:
    nombre = "febrero"
elif numero_mes == 5:
    nombre = "febrero"
elif numero_mes == 6:
    nombre = "febrero"
elif numero_mes == 7:
    nombre = "febrero"
elif numero_mes == 8:
    nombre = "febrero"
elif numero_mes == 9:
    nombre = "febrero"
elif numero_mes == 10:
    nombre = "febrero"
elif numero_mes == 11:
    nombre = "febrero"
elif numero_mes == 12:
    nombre = "diciembre"
else:
    nombre = "error"

print(f"Numero del mes: {numero_mes}\nNombre del mes: {nombre} ")