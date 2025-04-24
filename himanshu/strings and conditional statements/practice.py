#WAP to check if the number is a multiple of 7
a = int(input("enter number: "))
b=a%7
if(b==0):
    print("number is divided by 7")
else:
    print("number is not divided by 7")


#WAP to chek greatest between the three numbers:
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a>=b and a>=c):
    print("a is greatest")
elif(b>=c and b>=a):
    print("b is greatest")
else:
    print("c is greatest.")

#WAP to check if a number entered by the user is odd or even

a=int(input("enter a number"))
if(a%2==0):
    print("number is even. ")
else:
    print("number is odd. ")

#example of nesting state statement: if within an if

age = 99
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive") 
else:
    print("cannot drive")

#wap to find occurences of '$' in a string
str= "i have got money in $. i have 500$ bills. $ is a striong currency"
count = str.count("$")
print("count is: ", count)