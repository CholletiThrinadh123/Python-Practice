#Program to print a number in words
"""n=input("Enter a number")
for i in n:
    if i=="0":
        print("zero")
    elif i=="1":
        print("one",end=" ")
    elif i=="2":
        print("two",end=" ")
    elif i=="3":
        print("three",end=" ")
    elif i=="4":
        print("four",end=" ")
    elif i=="5":
        print("five",end=" ")
    elif i=="6":
        print("six",end=" ")
    elif i=="7":
        print("seven",end =" ")
    elif i=="8":
        print("eight",end=" ")
    elif i=="9":
        print("nine",end=" ")"""

#program to print number in digits using match case:
"""n=input("Enter a number")
for i in n:
    match i:
        case "1":
            print("one",end=" ")
        case "2":
            print("two",end=" ")
        case "3":
            print("three",end=" ")
        case "4":
            print("four",end=" ")
        case "5":
            print("five",end=" ")
        case "6":
            print("six",end=" ")
        case "7":
            print("seven",end=" ")
        case "8":
            print("eight",end=" ")
        case "9":
            print("nine",end=" ")
        case "0":
            print("zero",end=" ")"""



#program to print number in words using dict
"""n=input("Enter a number")
words={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
for i in n:
    print(words[i])"""












#program to print number in words using without string
"""n=int(input("Enter a number:"))
r=0
while n>0:
    l=n%10
    r=((r*10)+l)
    n=n//10
print(r)

words={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"zero"}
while r>0:
    l=r%10

    r=r//10
    print(words[l])"""




#program to find factors of a number
"""n=int(input("Enter a number:"))
for i in range(1,n+1):
    if n%i==0:
     print(i)"""














#program to print exponent without using **:
"""b=2
e=5
p=1
for i in range(e):
    p=p*b
print(p)"""













#program to print numbers in reverse:
for i in range(10,0,-1):
    print (i)








#program for loop inside loop
"""for i in range(1,10):
    for j in range(1,6):
        print(i,j)"""




