
print("Es escriba un numero ")
x = int(input())

for k in range(1, x+1, 1):   #Es EL ciclo que va a tener el programa que se va a repetir hasta llegar al numero dijitado, k actua como contador para evaluar cada numero que hay hasta x

  if(k%3 == 0) and (k%5 == 0):  #Evalua si el numero (K) es divisible entre 3 y 5 a la vez

     print( k," Es divisible en 3 y en 5"); 
  else: 
     
     if(k%3 == 0):     #De no ser divisible entre 3 y 5 a la vez, evalua si es divisible por 3
         print( k, " Es divisible en 3")
     else: 
       
         if(k%5 == 0):    #Mira si el numero es divisible por 5
             print( k, " Es divisible en 5")
         else: 
             print(k)   #Al no ser divisible ni por 3 ni 5 muestra el numero sin mas 
       
      
       
       

       

       
