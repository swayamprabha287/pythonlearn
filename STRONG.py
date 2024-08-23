from math import factorial
a=int(input("Enter a number: "))
temp=a
sum=0
while(a>0):
    remainder = a%10
    fact=factorial(remainder)
    sum +=fact
    a//=10
if(temp == sum):
    print(temp,"is a strong number")
else:
     print(temp,"is  not a strong number")


