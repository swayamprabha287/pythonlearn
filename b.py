marks={"Swayam":81, "subhadeep": 85, "souhardya" : 80 ,"soumyapriya": 89}
print(marks)
b=sorted(marks.items(), key = lambda x: x[1])
print(b)