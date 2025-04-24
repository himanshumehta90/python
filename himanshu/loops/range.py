#range function returns a sequence of numbers, starting from 0 by default and increments by 1(by default) and stops before a specified number:
#e.g start?, stop, step
x=range(5) #from 0 to 5 # 5 is the stopping condition
for val in x:
    print(val)

    x=range(2,10) #from 0 to 5 # 2 is the start condition, 10 is the stopping condition
for val in x:
    print(val)

    x=range(2,10,2) #from 0 to 5 # 2 is the start condition, 10 is the stopping condition, 2 is the step size #WAP to print even numbers from 2 to 10
for val in x:
    print(val)