a=int(input("Enter a number: "))
prime_factors=[]
for i in range(2,a+1):
    if(a%i ==0):
        f=0
        for j in range(2,i):
            if(i%j ==0):
                f=1
                break
        if(f==0):
           prime_factors.append(i) 
print(prime_factors)           
    
