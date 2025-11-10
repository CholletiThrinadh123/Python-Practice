#program to demonstrate for loop in pyhton
s="python"
for i in s:
    print(i,"*")

s="java"
for i in s:
    print(i,end=" ")

s=[10,20,30]
for i in s:
    print(i+2)

s={"name":"bhanu","age":22,}
for i in s.items():
    print(i)
