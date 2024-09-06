c = 0
print("Ingresa un numero");
n = int(input())
print("Ingresa una base menor a 10");
b = int(input())
resu = 0
while(b<n): #Define el ciclo que va a seguir para cambiarlo de base, que va hasta que b sea mayor que n
    x = n%b     #Extrae el residuo de dividir n por a base
    pro = x *(10**c)     #Multiplica el residuo por una potencia de 10 para de este modo guardar lo mas adelante
    c = c + 1     #Aumenta la potenia de 10 de 1 en 1 paraque los resultadosse vallan guardando en orden
    resu =resu + pro   #Es la varable que guarda el resultado de la conversion 
    n = n/b  
    n = int(n)  #Se re define n omo la parte entera de dividiro por b para que de este modo se puedan haer las dvisiones consecutivas
    
resu = resu + (n*(10**c)) #Como el ciclo para cuando n es menor que b, por lo que no se puede dividir, se agrega el dijto de este ultimo valor que toma n al resultado
print(resu);   
    
