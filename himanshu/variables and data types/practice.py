#wap to input user's first name and print its length

name = str(input("enter your first name: "))
length = len(name)
print("length of your name is:", length)

#wap to input 2 int numbers, a and b, Print true if a is greater than or equal to b, if not print false
a = int(input("enter number 1:"))
b = int(input("enter number 2: "))

c = a>=b
print ("answer is ", c)

#wap to input 2 floating numbers and print their average

a = float(input("enter number 1:"))
b = float(input("enter number 2: "))
c = (a+b)/2

print("average is: ", c)
#write a program to input 2 numbers and print their sum

a = int(input("enter first number: "))
b = int(input ("enter second number: "))
c = a+b
print ("your sum is : ", c)

#WAP to input side of aquare and print its area

side = float(input("enter side: "))
b = side**2
print("area", b)