#init function: constructor: All classes have a function called _init_(), which is always executed when the object is being initiated.
#self parameter is a refrence to the current instance of the class and is used to access variables that belongs to the class.

#default constructor:
class Student:
    name = "himanshu"
    def __init__(self): #this will initialize the first object, i.e. s1 #even if we dont write this, this will be invoked automatically in python
        print("addning a new entry")
        print(self) #(both the location of self variable and s1 is the same.)

s1=Student()
print(s1)

#now if want to input multiple students: #paramterized constructor

class Student:
    
    def __init__(self, name,marks): #full name is the new variable
        self.name=name
        self.marks = marks
        print("addning a new entry")

s1=Student("himanshu", 90)
s2=Student("karan", 92)

print(s1.name, s1.marks)
print(s2.name, s1.marks)