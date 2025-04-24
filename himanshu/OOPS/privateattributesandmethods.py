#conceptual Implementations in Python
#Private attributes and methods are meant to be used only within the clas and are not accessible from outside the class
#for every senstive information, we need to make sure that it remains inside the class only and deemed to be private class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #__denotes private attribute that cannot be accessed outside of the class

    def rest_pass(self):
        print(self.__acc_pass)

acc1=Account("12345","abcde")

print(acc1.acc_no)
# print(acc1.__acc_pass) #this will throw an error
print(acc1.rest_pass())