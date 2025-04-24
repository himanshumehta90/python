#OOP in python
#to map with real world scenarios, we started using objects in code. this is called object oriented programming.


#class and objects in python: class is a blueprint for createing objects.

#creating class:

class Student: #class object must be started in capital
    name = "himanshu"

    #create object (instance)

s1 = Student()
s2= Student()
print(s1)
print(s1.name)
print (s2.name)

#lets create a class Car and its components:

class Car:
    color = "blue"
    brand="pegeot"

car1 = Car()
print(car1.color)
print(car1.brand)