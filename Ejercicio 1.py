suma = 0
print("Ingresa la cantidad de datos que quieres ingresar")
n = int(input())
for k in range(1, n + 1, 1):    #define el ciclo que va pedir la cantidad n de numeros que va a pedir
    print("Ingresa un numero")
    x = int(input()) 
    if x % 2 == 0:    #Evalua si el numero ingresado es par segun el residuo al dividir por 2
        suma = suma + x     #Variable que hace la sumatoria de todos los numeros pares ingresados  
        h = h+1     #Es el contador que indica la cantidad de nuemeros pares ingresados
div = suma / h     #Calcula el promedio de los numeros pares ingresados 
print("El promedio de los numeros pares es " , div)






