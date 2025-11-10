# program to print product of numbers
n=int(input("Enter a number:"))
i=1
product =1
while (i<=n):
    product =product*i
    i=i+1
print(f"product of first {n} numbers is=",product)