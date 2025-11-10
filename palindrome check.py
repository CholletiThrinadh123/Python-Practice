#program to check whether given number is a palindrome or not
n=int(input("Enter a number:"))
n1=n
r=0
while n>0:
    l=n%10
    r=(r*10)+l
    n=n//10
if r==n1:
        print("palindrome")
else:
        print("not a palindrome")