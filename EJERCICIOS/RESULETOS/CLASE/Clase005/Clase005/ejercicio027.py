"""
Ejercicio 027

escribir un programa que permita ingresar una edad (entre 1 y 120 años), 
un género ('F'para mujeres, 'M' para hombres) y un nombre. 
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), 
informar tal situación indicando el nombre de la persona. 
Si los datos están bien ingresados el programa debe indicar, sabiendo que 
las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, 
si la persona está en edad de jubilarse.
"""





EDAD_JUB_MASC = 65
EDAD_JUB_FEM = 60

edad = int(input ("Edad: "))
genero = input ("Genero: ").upper()
nombre = input("Nome:").title()


if edad >= 1 and edad <= 120: #CAPA DE DEFENSA (VALIDACAO)

    if genero == "M" or genero == "F": # CAPA DE DEFENSA (VALIDACAO)

        if genero == "M":
            se_jubila = edad >= EDAD_JUB_MASC
        else:
            se_jubila = edad >= EDAD_JUB_FEM

        if se_jubila:
            print( f"{nombre} Genero: {genero} se jubila")
        else:
            print(f"{nombre} Genero: {genero} No se jubila")

    else:
        print(f"{genero} NO ES GENERO VALIDO")

else:
    print(f"{edad} NO ES EDAD VALIDA")








"""
edad = int(input("Edad: "))
genero = input("Genero: ").upper()
nombre = input("Nombre: ").title()


if edad >= 1 and edad <= 120:
    if genero == 'M' or genero == 'F':
        if genero == 'M':
            se_jubila = edad >= EDAD_JUB_MASC
        else:
            se_jubila = edad >= EDAD_JUB_FEM
        if se_jubila:
            print(f"{nombre} Genero: {genero} se jubila")
        else:
            print(f"{nombre} Genero: {genero} no se jubila")
    else:
        print(f"{genero} No es un genero valido")        
else:
    print(f"{edad} No es una edad valida")        

"""