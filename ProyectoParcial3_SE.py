import mysql.connector
from mysql.connector import errorcode

class adivinaquien:
   
   
   def _init_(self):
      self.conexion = mysql.connector.connect(host = "localhost", user = "root", password = "Red21Neuronal", database = "juegodemesa")
      self.cursor = self.conexion.cursor()
   
   def _del_(self):
       print("Destruido")

   def NewChar(self):
      try:
         sentencia = ("INSERT INTO juegos (idj, nombre, ojos, pelo, piel, raza )" "VALUES (%s, %s, %s, %s, %s, %s)")
         nameChar = input("\nDame el nombre de tu personaje\n")
         eyeColor= input("\nDame el color de ojos de tu personaje\n")
         hairColor= input("\nDame el color de pelo de tu personaje\n")
         skinColor= input("\nDame el color de piel de tu personaje\n")
         breed = input("\nDame la nacionalidad de tu personaje\n")
         self.cursor.execute("SELECT COUNT(*) FROM juegos;")
         records = self.cursor.fetchone()
         record = int(records[0])
         eyelist = []
         hairlist = []
         skinlist = []
         breedlist= []
         namelist = []
         idlist = []
         self.cursor.execute("SELECT*FROM juegos")
         characters = self.cursor.fetchall() #Recupera los datos de la consulta en una lista, donde tenemos n cantidad de personajes y cada uno tiene 6 atributos de 0-5 
         y = len(characters)
         no=True 
         print(characters,y,record)
         for x in range(record):                      #(sabemos cuantos personajes hay)
            for xx in range(4):                       #(#personajes)Nos importa contar cuantos atributos hay de cada uno y sacar el que mas probabilidad tenga solo nos importa saber de 2-5 para cada personaje
               counter = xx-4   
               if(xx == 0): idlist.append(characters[x][xx])
               if(xx == 1): namelist.append(characters[x][xx])
               if(counter == -1): breedlist.append(characters[x][counter])
               if(counter == -2): skinlist.append(characters[x][counter])
               if(counter == -3): hairlist.append(characters[x][counter])
               if(counter == -4): eyelist.append(characters[x][counter])
         #print(breedlist)
         for x in range(record):
            for xx in range(y):
               counter = xx-4
               print(x,xx)
               if(nameChar == namelist[xx]) and (breed == breedlist[xx]) and (skinColor == skinlist[xx]) and (hairColor == hairlist[xx]) and (eyeColor == eyelist[xx]):
                  print("Datos invalidos: Personaje repetido")
                  no = False
                  break
            if(nameChar == namelist[xx]) and (breed == breedlist[xx]) and (skinColor == skinlist[xx]) and (hairColor == hairlist[xx]) and (eyeColor == eyelist[xx]):
               print("Datos invalidos: Personaje repetido")
               break   
         nameChar = nameChar.capitalize() 
         eyeColor = eyeColor.capitalize() 
         hairColor= hairColor.capitalize() 
         skinColor= skinColor.capitalize() 
         breed = breed.capitalize()
         datos = (record,nameChar, eyeColor, hairColor, skinColor, breed)
         if(no == True):
            self.cursor.execute(sentencia,datos)
         #print('Ok ',nombre_bd)
         self.conexion.commit()
         #cursor.execute("INSERT INTO juegos (0111, Leo, cafes, negro, Blanco, Mexicano ) VALUES (idj, nombre, ojos, pelo, piel, raza)")
         self.cursor.close()
         self.conexion.close()
      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
               print("Something went wrong")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
               print("Database doesnt exist")
         else:
            print(err)
      else:
         if(no==True):
            print("Nuevo personaje agregado con exito")
         else:
            print("Peronaje Repetido")

   def preguntas(self):
      self.cursor.execute("SELECT COUNT(*) FROM juegos;")
      records = self.cursor.fetchone()
      record = int(records[0])
      S1 = []
      S2 = []
      S3 = []
      S4 = []
      S5 = []
      enfermedad = []
      idlist = []
      self.cursor.execute("SELECT*FROM juegos")
      characters = self.cursor.fetchall() #Recupera los datos de la consulta en una lista, donde tenemos n cantidad de personajes y cada uno tiene 6 atributos de 0-5 
      y = len(characters) 
      #print(characters,y,records)
      for x in range(record):                      #(sabemos cuantos personajes hay)
         for xx in range(5):                       #(#personajes)Nos importa contar cuantos atributos hay de cada uno y sacar el que mas probabilidad tenga solo nos importa saber de 2-5 para cada personaje
            counter = xx-5 
            print(xx,counter,y)  
            if(xx == 0): idlist.append(characters[x][xx])
            if(xx == 1): enfermedad.append(characters[x][xx])
            if(counter == -1): S1.append(characters[x][counter])
            if(counter == -2): S2.append(characters[x][counter])
            if(counter == -3): S3.append(characters[x][counter])
            if(counter == -4): S4.append(characters[x][counter])
            if(counter == -5): S5.append(characters[x][counter])
      #print(breedlist,y)
      nido = [S1,S2,S3,S4,S5]
      C = True
      d = 4
      while(C):
        for L in range(d):
         a = 0
         b=0
         answer=""
         for x in range(record):
            b=x
            if(len(nido[L])!=record):
                C=False
            #print(L,x,nido)
            eyeans=input("Uno de tus sintomas es "+nido[L][x]+"\n")
            print(x,record)
            if(x==record-1):
               answer = input("\nTu enfermedad no parece coincidir:\nTeg gustaria introducir tu enfermedad?\n")
               if(answer == 'si') or (answer == 'Si'):
                  self.NewChar()
                  break
            if(answer == 'si') or (answer == 'Si'):
                  self.NewChar()
                  break   
            if(eyeans=='Si') or (eyeans=='si'):
               for xx in range(y):
                  sies = nido[L][b] 
                  print(nido[L],a,xx,x,b)
                  if(nido[L][b]!=nido[L][a]):
                     del idlist[a]
                     del enfermedad[a]
                     del S1[a]
                     del S2[a]
                     del S3[a]
                     del S4[a]
                     del S5[a]
                     #print(nido[L],a,xx,x,b,record)
                     a=a-1
                     yy = len(nido[L])
                     for n in range(yy):
                        if(nido[L][n]==sies):
                            b=n
                     if(len(nido[L])==1):
                        break 
                     
                    
                  a = a+1
                  if(len(nido[L])==1):
                     break 
               if(len(nido[L])==1):
                  break
            if(len(nido[L])==1):
               break             
         if(len(nido[L])==1):
             break
        print("Tu enfermedad es : "+enfermedad[0]) 
             

if _name_ == "_main_":
   juega = adivinaquien()
   input("\t\t\t\tBienvenido a jugar, presiona enter para continuar")
   juega.preguntas()
   again=input("\nDeseas seguir jugando?")
   again = again.capitalize()
   if(again=="Si"):
      juega.jugar()
   else:
      print("\n\t\t\t\tHasta la proxima")
      input("Presiona enter para continuar")
