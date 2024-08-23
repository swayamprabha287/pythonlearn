a=int(input("Enter a number: "))
sum=0
order= len(str(a))
a1=a
while(a>0):
    digit=a%10
    sum+= int(digit) **order 
    a=a/10


if(sum==a1):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

    