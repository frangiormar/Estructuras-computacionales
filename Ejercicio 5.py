c = 0
print("Ingresa un numero");
n = int(input())
print("Ingresa una base menor a 10");
b = int(input())
resu = 0
while(b<n):
    x = n%b
    pro = x *(10**c) 
    c = c + 1
    resu =resu + pro  
    n = n/b
    n = int(n)
    
resu = resu + (n*(10**c))
print(resu);   
    
