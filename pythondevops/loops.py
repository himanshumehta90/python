list_of_clouds = ["aws", "gcp","azure", "utho","alibaba"] #list is a data structure which can hold multiple values of multiple type.
cloud = "gcp" #variable

print(list_of_clouds)

#add a new value to list:
list_of_clouds.append("salesforce") #adds to the end of the list
print(list_of_clouds)

list_of_clouds.insert(2,"heroku") #adds the value to the particular location

print(list_of_clouds)

print(len(list_of_clouds)) #prints length of the list (number of elements in the list)

#insert the value at 0th index

list_of_clouds.insert(0,"himanshu")

print(list_of_clouds)

#lets iterate the list: using for loop

for cloud in list_of_clouds:
    print(" ")
    print(cloud)

#lets print range:
for i in range(0,10): #it will end at 9 since ending is 10-1
    print("himanshu")

