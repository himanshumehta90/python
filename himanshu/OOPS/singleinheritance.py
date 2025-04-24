#inheritance: when one class(child/derived) derives the properties and methods of another class(parent/base). 

#examle of single inheritance:
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotCar(Car): #inherited properties of Car
    def  __init__(self,name):
        self.name=name

car1=ToyotCar("fortuner")
car2=ToyotCar("prius")

print(car1.name)
print(car1.start()) #this will call Car via toyottcar function
print(car1.color) #this will call Car via toyotcar function