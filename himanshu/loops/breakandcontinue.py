#break: used to terminate the loop when encountered
#continue: terminates execution in the current iteration and continues execution of the loop with the next iteration

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1


#search for number x in this tuple using loop and exit when found:

n = (1,4,9,16,25,36,49,64,81,100,49)
x = int(input("enter your number: "))
i = 0
while i < len(n):
    if(n[i] == x):
        print("found at index: ", i)
        break
    else:
        (print ("finding..."))
    i += 1

#exmaple of continue

i=0
while i<=5:
        if(i==3):
            i+=1
            continue #this will skip the 3
        print(i)
        i+=1

