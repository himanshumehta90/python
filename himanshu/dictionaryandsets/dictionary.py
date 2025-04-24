#Dictionary in python: Dictionaries are used to store data value in key:value pairs
#they are unordered, changeble and dont allow duplicate keys meaning they dont have an index

info= {
    
    "name":"himanshu",
    "learning":"coding",
    "subject":["c++","python","devops"],
    "age":32,
    "is_adult":True
}

print(type(info), info)
print(info["name"]) #to print a particular key

info["name"] = "sazzy" #to change a particular value of a key
print(info["name"])

info["surname"] = "Mehta" #to add a new key value pair
print(info)

#lets create a null dictionary and values in it

null_dict={}
null_dict["name"] = "Ashutosh"
null_dict["age"] = 35
null_dict["adult"] = True
print(null_dict)



