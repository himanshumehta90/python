#Methods are functions that belongs to objects.

#class is a collection of data (attributes) and methods

class Student:
    college_name="abc college" #class.attr
    name = "anonymous"  #class.attr

    def __init__(self, name,marks): #full name is the new variable
        self.name=name #obj.attr
        self.marks = marks #obj.attr
    
    def welcome(self): #method
        print("welcome to abc college",self.name)

    def get_marks(self): #method
        return self.marks


s1=Student("himanshu", 90)
s2=Student("karan", 92)
s1.welcome() #calling a method
print(s1.name, s1.marks) #obj attr > class attr
print(s2.name, s1.marks)
print(s2.college_name)
print(s1.get_marks()) #calling a method