class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


kitty = Student('Kitty', 85)
daniel = Student('Daniel', 80)

print(kitty.name)
print(kitty.grade)

#name and grade is an attribute of the object
#kitty is the object; you have instantiated an object