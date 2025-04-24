#block of statements that performs a specific task. it takes input as parameters, runs some operation and give some output.


#function definition:
def calsum(a,b): #this complete block will decrease the redundancy of writing the code. #a,b are called parametrs
    sum = a+b #function call; arguments
    print(sum)
    return sum 

calsum(5,10)
calsum(15,10)
calsum(25,10)

#empty function example:
def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello() #this will print hello as per the function defined.


#default parameters

def cal_prod(a=2,b=3): #here we have put default value of a and b. here we could leave value of a and pass it in the argument but we cannot leave b and only assign value of a. the default value has to come after.
    print(a*b)
    return a*b
cal_prod()