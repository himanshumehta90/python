#Tuples in Python: A built- in data type that lets us create immutable sequences of values.abs

tup=(87, 92, 68, 47, 4, 86)
print(type(tup))
print(tup[0])
#tup[0] = 43 --> not allowed in python

tup1=() #--> is a valid empty tuple
print(tup1)
tup2=(1,)
print(tup2)
tup3=(1,2,3) #tuples are created same way that the lists were created, each value is comma separated
print(tup3)

#slicing works the same way that we used in lists:

tup4= tup[1:3]
print(tup4)
tup5= tup[1:]
print(tup5)
tup6= tup[-3:-1]
print(tup6)

#Tuple Methods

tup=(2,1,3,1)
print(tup.index(1)) #returns index of first occurance

print(tup.count(1)) #rturns total occurance of that element


