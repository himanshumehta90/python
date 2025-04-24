#WAP to find factorial of first natural numbers

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


#WAP to find the sum of first natural numbers using while loop

n=5
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum=", sum)


#WAP to find the sum of first natural numbers using for loop

n=5
sum=0
for i in range(1, n+1):
    sum+=i
print("total sum=", sum)


#print multiplication tabe of a number:
x=int(input("enter a number"))
for i in range(1,10):
    print(x,"*", i, "=", i*x)




#WAP to print numbers from 100 to 1 using for loop 
for i in range(100,0,-1):
    print(i)

#WAP to print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1


#wap to print numbers from 1 to 100
for i in range (1,101):
    print(i)

#search for the number x and its index in this tuple using loop and print its output using continue function:
n = (1,4,9,16,25,36,49,64,81,100,9)
x = int(input("enter a number: "))
idx=0
for val in n:
    if (val == x):
        print(val, "found at", idx) #linear search
        continue
    print(val)
    idx+=1 
else:
    print("not found")




#search for the number x in this tuple using loop:
n = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter a number: "))
for val in n:
    if (val == x):
        print(val, "found")
        break
    print (val)
else:
        print("not found")

#print the elements of the following list using for loop:
n = [1,4,9,16,25,36,49,64,81,100]
for val in n:
    print(val)

#wap to print only even numbers from 1-10

i=0
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
#wap to print only odd numbers from 1-10

i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

#WAP to print numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1
print("end loop 1")

#WAP to print numbers from 100 to 1

i=100
while i>=1:
    print(i)
    i-=1

print("end loop 2")

#WAP to print multiplication table of a number n

n = int(input("enter a number: "))
i=1
while i<=10:
    print(n,"*", i, "=", n*i)
    i+=1
print("end loop 3")

#WAP to print the elements of the following list using a loop:

n = [1,4,9,16,25,36,49,64,81,100]
idx = 0 #traverse example
while idx < len(n):
    print(n[idx])
    idx +=1

print("end loop 4")

#search for number x in this tuple using loop:

n = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter your number: "))
i = 0
while i < len(n):
    if(n[i] == x):
        print("found at index: ", i)
    else:
        (print ("finding..."))
    i += 1