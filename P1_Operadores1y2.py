#Ingenieria Mecatronica: Inteligencia Artificial
#Jocelyn Mora Gómez
#20110164
#6E1

##########OPERADORES MATEMATICOS##########
#Esta práctica abarcará los capitulos 1-8 del curso de python: https://www.programacionfacil.org/cursos/python_basico/capitulo_1_instalacion_ide_python.html


#PARTE 1: Le pedimos al usuario que inserte la operacion que desea realizar
sel1 = (input("Que operación deseas realizar: \n" "SUMA.\n" "RESTA.\n" "MULTIPLICACION.\n" "DIVISION.\n" "EXPONENTE.\n"))

#Con upper() obligamos a que lo que inserte el usuario sea mayuscula
sel2 = sel1.upper()

#Dependiendo la opcion seleccionada por el usuario es la operacion que se realizará
if (sel2 == "SUMA"):
    #Se piden los numeros a operar
    num1 = int(input("Escribe el primer numero que deseas sumar: \n"))
    num2 = int(input("Escribe el segundo numero que deseas sumar: \n"))

    #Se realiza la operacion y se muestra el resultakkdo
    res = num1 + num2
    print("El resultado de la suma es: ", res)
else:
    if (sel2 == "RESTA"):
        #Se piden los numeros a operar
        num1 = int(input("Escribe el primer numero que deseas restar: \n"))
        num2 = int(input("Escribe el segundo numero que deseas restar: \n"))

        #Se realiza la operacion y se muestra el resultado
        res = num1 - num2
        print("El resultado de la resta es: ", res)
    else: 
        if (sel2 == "MULTIPLICACION"):
            #Se piden los numeros a operar
            num1 = int(input("Escribe el primer numero que deseas multiplicar: \n"))
            num2 = int(input("Escribe el segundo numero que deseas multiplicar: \n"))
            
            #Se realiza la operacion y se muestra el resultado
            res = num1 * num2
            print("El resultado de la multiplicacion es: ", res)
        else:
            if (sel2 == "DIVISION"):
                #Se piden los numeros a operar
                num1 = int(input("Escribe el primer numero que deseas dividir: \n"))
                num2 = int(input("Escribe el segundo numero que deseas dividir: \n"))

                #Se realiza la operacion y se muestra el resultado
                res = num1 / num2
                print("El resultado de la division es: ", res)
            else:
                if (sel2 == "EXPONENTE"):
                    #Se piden los numeros a operar
                    num1 = int(input("Escribe el numero que deseas elevar: \n"))
                    num2 = int(input("Escribe la potencia a la que deseas elevarlo: \n"))

                    #Se realiza la operacion y se muestra el resultado
                    res = num1 ** num2
                    print("El resultado de la division es: ", res)
                else: 
                    #Se evalua si la entrada del usuario esta dentro del rango permitido
                    if (sel2 != "SUMA" and sel2 != "RESTA" and sel2 != "MULTIPLICACION" and sel2 != "DIVISION" and sel2 != "EXPONENTE"):
                        print("ERROR AL ELEGIR LA OPCION")        

