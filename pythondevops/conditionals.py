day_of_week = input("enter day of week: ").lower() #this will convert our argument in lower case
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("this is weekend, weekend is a funday")
else:
    print("this is weekday")

num1 = int(input("enter num 1: "))
num2 = int(input("enter num2:"))

choice = input ("enter the operation: (operations +,-,*,/,%)")

if choice == "+":
    sum = num1 + num2
    print("addition", sum)
elif choice == "-":
    sub = num1-num2
    print("subtraction", sub)
elif choice == "*":
    mul = num1 * num2
    print("multiplication", mul)
elif choice =="/":
    div = num1/num2
    print("division", div)
elif choice == "%":
    mod = num1% num2
    print ("modulus", mod)
else:
    print("Invalid option")
