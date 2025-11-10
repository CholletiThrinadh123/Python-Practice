#check whether given year is leap year or not
#step1:Take the Year from user
a=int(input("Enter a year:"))
#step2: a divisible by 4 and y not divisible by 100 or divisible by 400
if a%4==0 and a%100!=0 or a%400==0:
    print(f"Given year {a} is leap year")
else:
    print(f"Given year {a} is not leap year")