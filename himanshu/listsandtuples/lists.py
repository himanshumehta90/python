#list in python - a built in data type that stores a set of values
#it can store elements of different data types (int, float, str etc)
#marks = [87,64,33,95] --> marks [0], marks[1] etc
#student =["karan", 85, "Delhi"] --> student[0], student[1]
#student[0]="Arjun" -->allowed in python
#len(student) --> returns length

marks = [94.4, 87.0, 95.0, 66.4, 45.1]
print(type(marks), marks)
print (len(marks)) #returns length
print(marks[0], marks[1]) #prints 0th and 1st value
student =["karan", 85, "Delhi"] #can store different data types in one list
print(student)

#strings are immutable, meaning their value canno be changes: e.g:
# str1 = himanshu
#str[0] = 0 --> is not allowed

#lists are mutable, e.g

student =["karan", 85, "Delhi"] #can store different data types in one list
student[0]= "himanshu"
print(student)

#list slicing
marks1=[87,92,85,44,56,37,12]
c= marks1[1:4]
d=marks1[1:]
e=marks1[-4:-1]
print(c)
print(d)
print(e)

#list methods:

list = [2,1,3]
list.append(4) #adds one element at the end
print(list)
list.insert(1,5) #inserts elemnet at index
print(list)
list.sort() #sorts list in ascending order
print(list)
list.sort(reverse=True)  #sorts list in descending order
print(list)
list.reverse() #revrses list
print(list)
list.remove(1) #removes first occurance of element
print(list)
list.pop(2) #removes element at index
print(list)
 