#file I/O in python: python can be used to perform operations on a file.
#types of files:
#text files: .txt, .docx, .log etc (characters can be stored in it)
#binary files:.mp4, .mov,.png,.jpeg etc (any other format)


#open, read and close file:
#f=open("filename", "mode") #filename can be name of file.
# #mode can be 
# r: readmode, 
# w: write mode, (overwrite) 
# x: create a new file and open it for writing
# a: open for writing, appending to the end of the file if it exists (add something at the end)
# b: binary mode
# t: text mode (defaut)
# +: open a disk file for updating (reading and writing)
#reading a file:
#data = f.read() #reads entire file
#data=f.realine #reads one line at a time


f = open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/demo.txt","rt")
# data = f.read()
# data = f.read(5) #in order to read first five charcters of the file, if we want to read entire file, leave it blank.
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)


# print(type(line2))
f.close()

#writing to a file
f = open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/demo.txt","w")
f.write("i want to learn code")
f.close()

#write mode when the file does not exist
f = open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/sample.txt","w") #same goes with append mode as well.
f.close()

#append mode:
f = open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/demo.txt","a")
f.write("\n my company is protiviti")
f.close()

#overite a file
f = open("demo.txt", "r+") #this will overite the file from the start
f.write("\n abc \n")
print(f.read())
f.close()

# #to truncate the file and then write
f = open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/demo.txt","a+")
print(f.read())
f.write("abc")
f.close()

#use of with syntax:

with open("demo.txt", "a+") as f:
    
    data = f.read()

    print(data) #no need to close the file when using with syntax

#use of syntax to write:

with open("demo.txt", "w") as f:
    f.write("new data to write")

#deleting a file: using the os module: Module (like a codelibrary) is a file already written by another programmer that generally has a function we can use. 
#pip3 install tensorflow - to install the os library

# import os
# os.remove("demo.txt")