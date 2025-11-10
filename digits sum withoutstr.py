#program to find sum of digits without string
n=int(input("Enter a number"))
n1=n
sum=0
while n>0:
    l=n%10
    sum=sum+l
    n=n//10
print(f"sum of {n1} digits is:",sum)