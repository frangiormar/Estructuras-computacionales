
print("Escriba un numero")
n = int(input())
k = 0       #El contador que va a aumentar las potencias de 10
num = 0     #La varaible que va a ir guardando el resultado 
while(n>0): 
    
    n = n/10     #Divide el numero dijitado en 10
    x = 10 * ( n - int(n))      #Toma la parte decimal de la division y la multiplica por 10 para tenerla como un numero entero (x)
    num = num + (x * (10**k))   #Multiplica (x) por una potencia de 10, que esta dada por k para asi guardarla sucesivamente en (num) he ir obteniendo el resultado
    k = k + 2     #Aumenta k de 2 en 2 para que la diferencia para que los dijitos tengan un espacio de separacion
    n = int(n)    #Toma solo la parte entera n, para asi retomar el ciclo dividiendo de nuevo esa parte entera

print(int(num))     #De este modo se obtiene el numero dijitado al inicio pero con un 0 separando cada dijito
     
    
    
    
    
    
    
