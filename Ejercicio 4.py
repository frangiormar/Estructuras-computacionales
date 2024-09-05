
print("Ingresa un numero ");
n = int(input())
print("Ingresa otro numero ");
m = int(input()) 
#Pide los dos numeros a los que les va a hallar el MCD
if n>m:    #El condicional evalua cual de los dos numeros es mayor 
   for k in range(1, m + 1, 1):    #Define el ciclo que llegaria hasta que k sea igual a m, siendo m<n
       if (m%k == 0) and (n%k == 0):    #Evalua si k divide m y n, y si es verdad guarda k como div
         div = k     #Como div cambia segun se encuentra un nuevo divisor comun de m y n, al final div va a ser el MCD
       else:  
           pass 
else:
   for k in range(1, n + 1, 1):  #Se usa el mismo ciclo con la diferencia que evalua hasta que k sea n, ya que seria n<m
       if (m%k == 0) and (n%k == 0): 
         div = k
       else:  
           pass 
       
print("El maximo coomun divisor es " , div);        
                  
      
     
 

