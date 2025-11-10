# Program to check whether given  character is vowel or not
#step 1: take character from user
a=(input("Enter a letter:"))

#check whether letter is in a,e,i,o,u if yes print vowel else consonant

l="a e i o u  A E I O U "
if len(a)==1:
  if a in l:
    print(f"Given Character {a} is a vowel")
  else:
    print(f"Given Character {a} is not a vowel")
else:
   print("Please enter a single letter")
