name = input ("enter your name: ")

print ("welcome",name)

val = input ("enter a value: ")
print (type(val), val) #by default the type is string

val1=float(input("enter a floating val: ")) #in order to explicitly mention that the input is float
print(type(val1),val1)

#lets write the input in a form:

name = str(input("enter your name:"))
age = int (input("enter your age: "))
marks = float (input("enter your marks: "))

print ("hello", name, ", your age is", age, ", you have scored", marks)
