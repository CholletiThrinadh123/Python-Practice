#Program to check whether given number is prime or not
#step 1: Read the input from user.
n=int(input("Enter a number:"))

for i in range(2,n):
    if n%i==0:
        print(f"Enter number {n} is not a prime number")
        break
else:
    print(f"Enter number {n} is a prime number")
