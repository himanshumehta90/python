#Methods that dont use the self parameter, class level methods
#decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

class Student:
    @staticmethod #decorator
    def hello():
        print("hello")
        
s1=Student()
print(s1)
s1.hello()