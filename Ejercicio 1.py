suma = 0
print("Ingresa la cantidad de datos que quieres ingresar")
n = int(input())
for k in range(1, n + 1, 1):
    print("Ingresa un numero")
    x = int(input())
    if x % 2 == 0:
        suma = suma + x
        h = h+1
div = suma / h
print("El promedio es " , div)






