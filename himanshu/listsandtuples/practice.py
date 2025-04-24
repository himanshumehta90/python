

#WAP to store below values in a list and sort them from "A" to "D":
# ["C", "D", "A", "A", "B", "B", "A"]

list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort() 
print(list)

#WAP to count the number of students with the grade "A"n the following tuple:
# ["C", "D", "A", "A", "B", "B", "A"]

tup = ("C", "D", "A", "A", "B", "B", "A")

print(tup.count("A"))

#WAP to check if a list contains a palindrome of elements
list1 = [1,2,3,4,3,2,1]
list1_copy = list1.copy()

list1_copy.reverse()


if(list1==list1_copy):
    print("it is a pallindrome")
else:
    print("it is not a pallindrome")



#WAP to ask user to enter names of their 3 favorite movies and store them in a list:
movies = []
a= input("enter your fav movie 1: ")
b= input("enter your fav movie 2: ")
c= input("enter your fav movie 3: ")

movies.append(a)
movies.append(b)
movies.append(c)

print(movies)