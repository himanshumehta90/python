#conditional statements
#if-elif-else (syntax)
# if(condition):
#     Statement1
#     elif(condition):
#     Statement2
#     else:
#         StatementN


#here if we write "if" statement again, it will still continue even if above statement is true

num = 5
if(num>2):
        print("number is greater than 2") #example of indentation  - proper spacing after a statement
if(num>3):
        print("number is greater than 3") #here if we write "if" statement again, it will still continue even if above statement is true


#elif statement will only run if if statement is false, 

light = "gren"
if(light == "red"):
    print("stop")
elif(light == "green"): #elif statement will only run if if statement is false, 
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

    #wap to grade students on the basis of marks

marks = int(input("enter the marks: "))

if(marks>=90):
    grade = "your grade is A"
elif(marks>=80):
    grade = "your grade is B"
elif(marks>=70):
    grade = "your grade is C"
else:
    grade = "your grade is D"

print (grade)

#example of nesting state statement: if within an if

age = 99
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive") 
else:
    print("cannot drive") 
