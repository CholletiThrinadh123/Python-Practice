#program to print a number in words using if-elif
n=input("enter a number:")

for i in n:
   if i=="0":
       print("zer0",end=" ")
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
       print("seven",end=" ")
   elif i=="8":
       print("eight",end=" ")
   elif i=="9":
       print("nine",end=" ")

#program to print a number in words using match case;
n=input("Enter a number:")
for i in n:
      match i:
          case "0":
              print("zero")
          case "1":
              print("one")
          case "2":
              print("two")
          case "3":
              print("three")
          case "4":
              print("four")
          case "5":
              print("five")
          case "6":
              print("six")
          case "7":
              print("seven")
          case "8":
              print("eight")
          case "9":
              print("nine")






