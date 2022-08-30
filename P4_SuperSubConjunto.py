#Jocelyn Mora Gomez
#20110164
#Inteligencia artificial
#6E1

#####################################

#Super conjunto y sub conjunto

sel = input("Introduce el conjunto que deseas conocer:\n" "1. Super Conjunto\n" "2. Sub Conjunto\n")

if sel == "super conjunto":
    num1 = (input("Introduza el primer numero del conjunto A:"))
    num2 = (input("Introduza el segundo numero del conjunto A:"))
    num3 = (input("Introduza el tercer numero del conjunto A:"))
    num4 = (input("Introduza el cuarto numero del conjunto A:"))
    num5 = (input("Introduza el primer numero del conjunto B:"))
    num6 = (input("Introduza el segundo numero del conjunto B:"))
    super = {num1, num2, num3, num4}.issuperset({num5, num6}) 
    print("El super conjunto es:", super)
else:
    if sel == "subconjunto":
        num1 = (input("Introduza el primer numero del conjunto A:"))
        num2 = (input("Introduza el segundo numero del conjunto A:"))
        num3 = (input("Introduza el primer numero del conjunto B:"))
        num4 = (input("Introduza el segundo numero del conjunto B:"))
        num5 = (input("Introduza el tercero numero del conjunto B:"))
        sub = {num1, num2}.issubset({num3, num4, num5})
        print("El sub conjunto es:", sub)
    else:
        if sel != "super conjunto":
            print("ERROR")
        else:
            if sel != "subconjunto":
                print("ERROR")
