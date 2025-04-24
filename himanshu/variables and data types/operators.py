a = 5
b = 2

#arthematic operators: +,-,/,*,%,**
sum = a + b
diff = a-b
mul = a*b
div = a/b
mod = a % b #modular operator to find the remainder
pow = a **b #power operator used to calculate power of the number, like 5^2, 5 square

print (sum)
print (diff)
print (mul)
print (div)
print (mod)
print (pow)

#relational / Comparison Operators: ==,!=,>,<,>=,<=, should give output as true or false only
a=50
b=20

com = a == b #Comparison operator which should give output as false
comnot = a != b #Comparison operator which should give output as true
greater = a >= b
notgreater = a <= b
lessthan = a < b

print (com)
print(comnot)
print (greater)
print (notgreater)
print (lessthan)

#Assignment operators: =,+=,-=,*=,/=,%=,**=

num = 10

num %= 10
print ("num1 =",num)

#logical operators : not, and, or #boolean value
a = 50
b = 20
print(not False) #gives opposite answer
print (not True) #gives opposite answer
print (not (a>b)) #gives opposite answer

val1=True
val2=False

print ("and operator :", val1 and val2) #gives true only when both are same
print ("or operator :", val1 or val2) #gives true  when either of which is same
print ("or operator number :", a==b or a>=b)