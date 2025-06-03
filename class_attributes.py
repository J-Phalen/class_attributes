# Create a Class Named Student with Attributes; Modify and Print Original and Modified Values
"""
Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire
attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.
"""


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_class(self, student_class):
        self.student_class = student_class

    def get_name(self):
        if self.student_name:
            return self.student_name
        else:
            print("Student name not found")
            raise SystemExit

    def display_attributes(self):
        attributes = self.__dict__  # I had to cheat and look up how to cast this to a dict
        return attributes

    def remove_student_name(self):
        if self.student_name:
            del self.student_name
        else:
            print("Student name not found")
            raise SystemExit


# Create the first student object
studentx = Student(1, "Jimmy")
# Create the second student object
studenty = Student(2, "Joi")

# Add a class to them
studentx.add_class("PCET")
studenty.add_class("PCET")

# Print out the attributes of the first student
name = studentx.get_name()
attributes = studentx.display_attributes()
print(f"The attributes of {name} are:")
for k, v in attributes.items():
    print(f"{k}: {v}")

# Print out the attributes of the second student
name = studenty.get_name()
attributes2 = studenty.display_attributes()
print(f"The attributes of {name} are:")
for k, v in attributes2.items():
    print(f"{k}: {v}")

# Remove that students name
studentx.remove_student_name()
studenty.remove_student_name()

# Reprint the attributes of the first student.
print(f"The attributes of {name} are now:")
attributes = studentx.display_attributes()
for k, v in attributes.items():
    print(f"{k}: {v}")

# Reprint the attributes of the second student.
print(f"The attributes of {name} are now:")
attributes2 = studenty.display_attributes()
for k, v in attributes2.items():
    print(f"{k}: {v}")
