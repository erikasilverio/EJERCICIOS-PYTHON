"""
Ejercicio 022
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""


n1 = int(input("Número 1: ")) #20
n2 = int(input("Número 2: ")) #15 
n3 = int(input("Número 3: ")) #100
n4 = int(input("Número 4: ")) #100

"""if n1 > n2:
    if n1 > n3:
        print("Mayor:",n1)
    else:
        print("Mayor:",n3)
else:
    if n2 > n1:
        if n2 > n3:
            print("Mayor:",n1)
        else:
"""

mayor = n1

if n2 > mayor:
    mayor = n2

if n3 > mayor:
    mayor = n3

if n4 > mayor:
    mayor = n4

print("Mayor: ",mayor)


