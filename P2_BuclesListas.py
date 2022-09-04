#Ingenieria Mecatronica: Inteligencia Artificial
#Jocelyn Mora Gómez
#20110164
#6E1

##########LISTAS##########
#Esta práctica abarcará los capitulos 10-30 del curso de python: https://www.programacionfacil.org/cursos/python_basico/capitulo_1_instalacion_ide_python.html

sel1 = ""

while sel1 != "NO":

    #PARTE 1: Le pedimos al usuario que elija o no crear una lista nueva
    sel1 = (input("***LISTA DE COMPRAS*** \n" "Deseas crear una nueva lista de compras?\n" "Si\n" "No\n"))
    #Con upper() obligamos a que lo que inserte el usuario sea mayuscula
    sel1 = sel1.upper()

    if (sel1 == "SI"):
        item = int(input("Cuantos elementos deseas agregar a la lista de compras?\n"))
        compras = []

        for i in range(0,item):
            if (i == item):
                break
            elemento = (input("Escribe el elemento \n"))
            compras.insert(i, elemento)

        print(compras)    

    sel2 = (input("Deseas borrar algun elemento de la lista?\n" "Si\n" "No\n"))

    if (sel1 == "SI"):
        delet_e = (input("Que elemento deseas eliminar?\n"))
        compras.remove(delet_e)
        print("La lkista final es:", compras)

    if (sel1 == "NO"):
        print("La lista final es:", compras)
