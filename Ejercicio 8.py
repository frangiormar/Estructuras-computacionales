
print("Escriba un numero")
n = int(input())
k = 0
num = 0
while(n>0):
    
    n = n/10 
    x = 10 * ( n - int(n))
    num = num + (x * (10**k))
    k = k + 2
    n = int(n)

print(int(num))
     
    
    
    
    
    
    
