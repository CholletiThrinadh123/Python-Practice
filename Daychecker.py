#progam to check whether given day is weekday or weekend
#Enter day number
day =int(input("Enter a day number (1 to 7 only):"))
#find match acc to input
match(day):
    case 1 | 2 | 3 | 4 | 5:
        print(f"Enter day {day} is a weekday")
    case 6 | 7:
        print(f"Enter day {day} is a weekend")
    case _:
        print("Given entry is invalid")




