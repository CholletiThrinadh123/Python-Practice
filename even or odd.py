#Progam to see whether the number is even or odd
#step 1:let;s take a number from user and store it in variable a
a=int(input("Enter a number(only numbers need to enter):"))

#step 2: check whether n is divisible by 2, if remainder is o then even else odd
if (a%2==0):
    print(f"given number {a} is even")
else:
    print(f"given number {a} is odd")
