class Car:
    @staticmethod
    def start():
        print("start car")

    def stop():
        print("stop car")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand=brand

class Fortuner(ToyotaCar): #this is first inheritin toyotacar and then Car
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesel")
car1.start()