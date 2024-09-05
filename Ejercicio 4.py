
print("Ingresa un numero ");
n = int(input())
print("Ingresa otro numero ");
m = int(input())

if n>m: 
   for k in range(1, m + 1, 1): 
       if (m%k == 0) and (n%k == 0): 
         div = k
       else:  
           pass 
else:
   for k in range(1, n + 1, 1): 
       if (m%k == 0) and (n%k == 0): 
         div = k
       else:  
           pass 
       
print("El maximo coomun divisor es " , div);        
                  
      
     
 

