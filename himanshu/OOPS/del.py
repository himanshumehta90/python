#abstraction : hiding the implementation details of a class and only showing the essential features to the user

#encapsulation: wrapping data and functions into single unit(object)

#del keyword: used to delete object properties or object itself:

class Student:
    def __init__(self,name):
        self.name=name

s1= Student("himanshu")
print(s1.name)

del s1 #this will delete s1 from the memory
print(s1)