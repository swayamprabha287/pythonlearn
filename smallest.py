a=int(input("Enter 4 number: "))
max=min=a
for i in range(3):
    a=int(input())
    if(max<a):
        max=a
    elif(min>a):
        min=a
print("Largest no between 4 numbers is =",max)
print("smallest no between 4 numbers is =",min)