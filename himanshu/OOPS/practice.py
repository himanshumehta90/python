#create student class that takes name and marks of 3 subjects as arguments in constructor. then create a method to print the average

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.marks = [mark1, mark2, mark3]

    def print_average(self):
        average = sum(self.marks) / len(self.marks)
        print(f"{self.name}'s average marks: {average:.2f}")

# Example usage
student1 = Student("Alice", 85, 90, 78)
student1.print_average()