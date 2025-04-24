str1="this is a string example. \nhere we are demonstarting the use of next line" #\n used to write the string in the next line

print(str1)

str2="this is a string example. \t here we are demonstarting the use of tab" #\t used to write the string in the next tab

print(str2)

#Example of concatenation: adding 2 strings

str3 ="himanshu"
str4="mehta"
c=str3 + str4
c=str3 + " " + str4 #in order to add space between 2 strings: add ""+ in between
print (len(c), c) #to store length of the string


#example of string

str="himanshu protiviti"
ch = str[0] #string starts with 0
print ("output of ch:" , ch)

#example of slicing - accessing part of a string

str2="himanshu mehta"
ch1 = str2[1:4]
ch2 = str2[9:]
print("output of ch1:" ,ch1)
print("output of ch2:" ,ch2)

#example of negative indexing - backward characters:

str3="himanshu mehta"
ch3 = str3[-4:-1]
ch4 = str3[-9:]
print("output of ch3:" ,ch3)
print("output of ch4:" ,ch4)

#example of string functions:

str="i am a coder"
str4 = str.endswith("er") #returns true if string ends with substr
str5 = str.capitalize() #capatalizes 1st char
str6 = str.replace("am","was") #replaces all ocurrences of old with new
str7 = str.find("coder") #returns 1st index of 1st occurence
str8 = str.count("am")  #counts the occurance of substring in a string

print("str4 output: ",str4)
print ("str5 output: ", str5)
print ("str6 output: ", str6)
print ("str7 output: ", str7)
print ("str8 output: ", str8)