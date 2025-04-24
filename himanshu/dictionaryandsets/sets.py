#Set in python: Set is a colletcion of unordered items. Each element in the set must be unique and immutable
# only boolean, int, float, str, tuple can be stores in the sets, because these are immutable

collection1 = {1,2,3,4,"hellow", "world", "world", 2,3,4,5}
print(len(collection1), type(collection1), collection1) #every time the output of order will be different because these are unordered. 

#lets create an empty set

collection = set ()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add((3,4,5,6))
collection.add("himanshu")
print(collection)
print(collection.pop()) #removes a random value from our set

collection.remove(1) #in order to remove an element from sets
print(collection)


collection.clear() #clear our set
print(collection)
