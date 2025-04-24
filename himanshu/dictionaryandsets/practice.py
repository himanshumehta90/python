#WAP to enter marks of 3 subjects from the user and store them in a dicionary. start with an empty dictionary and add one by one. Use subject name a ke and marks as value

marks = {}
x=int(input("enter marks of phy: "))
marks.update({"phy marks =" : x})

x=int(input("enter marks of chem: "))
marks.update({"chem marks =" : x})

x=int(input("enter marks of math: "))
marks.update({"math marks =" : x})

print(marks)



#WAP: you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students
#"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

requiredclass = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("required classes: ", len(requiredclass))

#WAP to store following word meaings in a python dictionary:
#table: "a piece of furniture", "list of facts and figures"
#cat: "a small animal"

dict = {
    "table": ("a piece of furniture", "list of facts and figures"),
    "cat": "a small animal"
}

print(dict)