#Ingenieria Mecatronica: Inteligencia Artificial
#Jocelyn Mora Gómez
#20110164
#6E1

import os

#Grafo a utilizar
grafo = {'a': [('p',4), ('j',15), ('b',1)],
         	'b': [('a',1), ('d',2), ('e',2), ('c',3)],
			'j': [('a',15)],
			'p': [('a', 4)],
			'd': [('b',2), ('g',3)],
			'e': [('b',2), ('g',4), ('f',5), ('c',2)],
			'c': [('b',3), ('e',2), ('f',5), ('i',20)],
			'g': [('d',3), ('e',4), ('f',10), ('h',1)],
			'f': [('g',10), ('e',5), ('c',5)],
			'i': [('c',20)],
			'h': [('g',1)] 
		}

#Se muestra el grafo
print("Muestra el grafo antes del recorrido: \n")
for key, lista in grafo.items():
	print(key)
	print(lista)

print()
os.system("pause")
		
visitados = []
cola = []

origen = input("Ingresa el nodo origen: ")
print("\nLista de recorrido en anchura\n")
#Paso 1: En una cola se coloca el vertice origen
cola.append(origen)
#Paso 2: while la cola no este vacia
while cola:
	#paso 3: vertice actual
	actual = cola.pop(0)

	#paso 4: si no se ha llegado al vertice
	if actual not in visitados:
		#paso 5: mostrar vertice actual
		print("Vertice actual -> ", actual)
		#paso 6: Ccolocar el vertice en la lista de los vertices visitados
		visitados.append(actual)
	for key, lista in grafo[actual]:
		if key not in visitados:
			cola.append(key)

print()
os.system("pause")
