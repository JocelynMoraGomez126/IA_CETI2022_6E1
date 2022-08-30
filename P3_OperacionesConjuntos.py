#Jocelyn Mora Gomez
#20110164
#Inteligencia artificial
#6E1

#####################################

#Operaciones con conjuntos
#unión, intersección, diferencia, diferencia simétrica

num1 = (input("Introduza el primer numero del conjunto A:"))
num2 = (input("Introduza el segundo numero del conjunto A:"))
num3 = (input("Introduza el tercer numero del conjunto A:"))
num4 = (input("Introduza el primer numero del conjunto B:"))
num5 = (input("Introduza el segundo numero del conjunto B:"))
num6 = (input("Introduza el tercer numero del conjunto B:"))

con_A = {num1, num2, num3}
print("El conjunto A es:",con_A)

con_B = {num4, num5, num6}
print("El conjunto B es:",con_B)

#AnB
union = {num1, num2, num3}.union({num4, num5, num6})
print("La union de los conjuntos A y B es:",union)

#AuB
inter = {num1, num2, num3}.intersection({num4, num5, num6})
print("La interseccion de los conjuntos A y B es:",inter)

#A-B
dif = {num1, num2, num3}.difference({num4, num5, num6})
print("La diferencia de los conjuntos A y B es:",dif)

#A*B
dif_sim = {num1, num2, num3}.intersection({num4, num5, num6})
print("La diferencia simetrica de los conjuntos A y B es:",dif_sim)
