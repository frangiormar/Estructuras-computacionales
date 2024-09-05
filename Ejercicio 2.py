print("Ingrese un numero")
n = int(input())     #Se pide que ingrese el numero al que le vamos a calcular el factorial
facto = 1 

for k in range (1, n+1, 1):        #Es el ciclo en el cual usando la variable k va a calcular el factorial debido a que aumenta de 1 en 1 hasta n
    facto = facto * k       #Usando la variable facto se va guardando las multiplicaciones de k
    
print(facto)