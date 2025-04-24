#for loops are used for sequential traversals. for traversing list, string, tuples, etc
num = [1,2,3,4,5,6,7]
for val in num:
    print(val)

    #lets use in tuple

tup = (1,2,3,4,5,6,7)
for val in tup:
    print(val)

#usage in string:

name = "himanshu"
for val in name:
    print(val)


#example of for else: find a character in a particular string

name = "himanshu"
x=str(input("enter character:"))
for val in name:
    if (val == x):
        print(val , "found")
        break   
    print(val)
else:
        print("scanned and not found")

        