#program to print sum of first last digits
n=int(input("Enter a number:"))
l=n%10
while n>0:
    f = n % 10
    n=n//10

print(f"sum of {l} and {f} digits is:",(l+f))

