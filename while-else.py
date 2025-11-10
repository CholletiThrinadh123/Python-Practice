#program to demonstrate while-else loop:
#step 1: read the input from user.
n=int(input("Enter a value:"))
#step2: demonstrate while-else condition
i=1
while i<=100:
    print(i)
    i=i+1
    if n>100:
        break
else:
    print("code is ended")


