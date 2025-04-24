#create a new file practice.txt using python and add following data in it:#hi everyone
#we are learning file I/O
#using python
#i like python

with open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/practice.txt", "w") as f:
    f.write("we are learning file I/O \nusing python \ni like python ")

#WAF that replaces all occurences of "python" with "java" in above lines
   
# Step 1: Read the original file content
with open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/practice.txt", "r") as f:
    data = f.read()

# Step 2: Replace "python" with "java"
new_data = data.replace("python", "java")
print(new_data)

# Step 3: Write the updated content back to the file
with open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/practice.txt", "w") as f:
    f.write(new_data)

#search if the word learning exists in our file or not
word = "learning"
with open("/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) !=-1):
        print("found")
    else:
        print("not found")

#WAF to find which line of the file does the word " learning occurs first. Print -1 if word is not found"

def find_word_line(filepath, word):
    with open(filepath, "r") as f:
        for line_num, line in enumerate(f, start=1):
            if word in line:
                return line_num
    return -1

# Usage
filepath = "/home/protivitiadmin/PythonPractice/himanshu/fileinputoutput/practice.txt"
word = "learning"
result = find_word_line(filepath, word)
print(result)