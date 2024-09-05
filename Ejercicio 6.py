
print("Es escriba un numero ")
x = int(input())

for k in range(1, x+1, 1):

  if(k%3 == 0) and (k%5 == 0):

     print( k," Es divisible en 3 y en 5"); 
  else: 
     
     if(k%3 == 0):
         print( k, " Es divisible en 3")
     else: 
       
         if(k%5 == 0):
             print( k, " Es divisible en 5")
         else: 
             print(k)
       
      
       
       

       

       
