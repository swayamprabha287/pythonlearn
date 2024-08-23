n=int(input("Enter a number: "))
a=0
b=1
print("The fibonacci series is as follow:-")
print(a,end=" ")
print(b,end=" ")

for i in range(1,n-1):
    s=a+b
    print(s,end=" ")
    a=b
    b=s
    