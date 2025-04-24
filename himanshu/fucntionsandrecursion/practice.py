#WAF to find number is even or odd

def oddeven(n):
    x=n%2
    if (x==0):
        print("number is even")
    else:
        print("number is odd")

oddeven(int(input("enter number: ")))

#WAF to convert usd to inr:

def usdtoinr(n):
        x=n*100
        print("usd value = ", x , "INR")

usdtoinr(int(input("enter number: ")))

#WAF to find factorial of a number:


def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)

fact(int(input("enter a number: ")))

#WAF to print the elements of a list in a single line:
cities = ["delhi", "mumbai", "pune", "banglore", " chennai", "patiala"]

def print_line(list):
    for item in list:
        print(item, end="")

print_line(cities)

#WAF to print the length of a list.
cities = ["delhi", "mumbai", "pune", "banglore", " chennai", "patiala"]
name= ["a","b","c","d","e"]

def print_len(list):
    print(len(list))

print()
print_len(cities)



#WAP to calculate average of 3 numbers using functions

def average(a,b,c):
    x=a+b+c
    avg=x/3
    print(avg)
    return avg

average(22,22,22)