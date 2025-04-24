#example of nested dictionary:

student={
    "name":"himanshu",
    "score":{
        "devops":10,
        "python":5,
        "dba":9
    }
}
print(student)
print(student["score"]["devops"]) #to print a particular nested key output


#dictionary methods:

print(student.keys()) #print all the keys
print(list(student.keys())) #type casts keys into a list
print(len(student)) # returns total number of key value pairs


print(student.values()) #returns all the values
print(list(student.values())) #type casts values into a list

print(student.items()) #returns all (key , val) pairs as tuples
print(list(student.items())) #this will convert our tuple into a list

pairs  = list(student.items())
print(pairs[0]) #to access a particular key value

print(student["name"]) #this will print vale of the key
#print(student["name2"]) -- >this will throw an error
print(student.get("name2")) #this will throw an output as none but not an error. this is called method

student.update({"city":"patiala"}) #this will add a new key value pait in our dictionary
print(student)

student1 = {"hobbies": "cricket", "age":16, "name":"sazzy"}
student.update(student1) #this will also append and update the student dictionary

print(student)
