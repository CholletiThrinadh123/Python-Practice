#program to print first n numbers
#step 1: let's take the n value from user
n=int(input("Enter a number:"))
#step 2: let's find the sum of first n numbers
i=1
sum=0
while(i<=n):
    sum = sum +i
    i=i+1
print(f"sum of first {n} numbers is =",sum)

