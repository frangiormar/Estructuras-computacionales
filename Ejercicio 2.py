
print("Ingresa un nuemero entero ");
n = int(input())
raiz = pow(n, 0.5)        #Saca la raiz cuadrada del numero entero ingresado

dif = raiz - int(raiz)        #Guarda la parte real de la raiz calculada, en dif

if dif == 0:        #Evalua si la raiz tiene parte real direfente de 0, en otras palabras, si es una exacta o decimal 
       print("Es potencia cuadrada de " , raiz); 
else:
       print("No es potencia cuadrada de un entero");
