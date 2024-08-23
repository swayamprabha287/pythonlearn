a=int(input("Enter a number: "))
count=0
if a>1:
    for i in range(1,a+1):
        if(a%i ==0):
            count+=1
if(count ==2):
    print("prime no")
else:
     print(" Not a Prime no") 