#program to check whether given number is divisible by both 3 and 11 or not?
#step 1: take number
a=int(input("Enter a number:"))

#step 2: check whether divisible by 3 and 11
if a%3==0 and a%11==0:
    print(f"Given number {a} is divisible by both 3 and 11")
else:
    print(f"Given numuber {a} is not divisible by both 3 and 11")
print("program ends, Visit again")


