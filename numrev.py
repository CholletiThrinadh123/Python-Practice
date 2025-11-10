n=int(input("Enter a number:"))
n1=n
r=0
while n>0:
    l=n%10
    r=(r*10)+l
    n=n//10
print(f"reverse of the given number {n1} is:",r)