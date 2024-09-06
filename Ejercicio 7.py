print("Ingrese un numero")
n = int(input())

while(n != 0):  #Declara el ciclo que va a estar funionando hasta que se djite el numero 0
    if(n>0):   #Es el condicional que permite saber si el numero dijitado es positivo
        print(n, " es postivo") 

    if(n<0):   #Es el condicional que permite saber si el numero dijitado es negativo
        print(n, " es negativo")
        
    n = int(input())
   
