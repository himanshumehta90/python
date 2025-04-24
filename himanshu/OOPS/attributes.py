#Class and Instance Attributes:

#attributes: any data
#class.attr: that is common for all the objects, e.g. name of the college.
#obj.attr (instance attr): which is different for all the objects, e.g name of the student: self.name, self.marks.

class Student:
    college_name="abc college" #class.attr
    name = "anonymous"  #class.attr

    def __init__(self, name,marks): #full name is the new variable
        self.name=name #obj.attr
        self.marks = marks #obj.attr
        print("addning a new entry")

s1=Student("himanshu", 90)
s2=Student("karan", 92)

print(s1.name, s1.marks) #obj attr > class attr
print(s2.name, s1.marks)
print(s2.college_name)