#Jocelyn Mora Gomez
#20110164
#Inteligencia artificial
#6E1

#####################################

#Conjunto universal y conjunto vacio

selection = input("Cual conjunto deseas conocer: Universal o Vacio?")
print("Elegiste:", selection)

if (selection == "universal"):
    print("En cualquier aplicación de la teoría de conjuntos, los elementos de todos los conjuntos en consideración pertenecen a un gran conjunto fijo llamado conjunto universal denominado U.")

if (selection == "vacio"):
    print("Se denomina así al conjunto que no tiene ningún elemento.")

if (selection != "vacio"):
    if (selection != "universal"):
     print("ERROR DE SELECCION INTENTA DE NUEVO")
