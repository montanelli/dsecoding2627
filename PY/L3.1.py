"""object oriented programming"""

# Object-oriented programming (OOP) organizes a program around objects.
# An object combines data with the operations that can be performed on that data.
# A class defines a kind of object; an object is an instance of that class.

# some methods in a class are somehow common to any class
# They are also called dunder methods and their names start and end with double underscores
# their goal is to let objects work with Python’s built-in operations.
# Examples: __init__ , __str__, __len__

# OOP issues that will not be discussed (but recommended for further personal study):
## Encapsulation means keeping data and the methods that operate on it together, while controlling how the data is accessed. Python uses naming conventions rather than strict access restrictions:
### name is an example of public object property (visible from outside the object)
### _name is an example of restricted object property (intended for internal use/visibility).

## Polymorphism means that different objects can respond to the same method call in their own way.


class Student:
    # Class attributes represent properties shared by all the object of the class
    available_exams = ("Python", "Databases", "Statistics")

    # __init__ is the method to inizialize a new object (object constructor)
    # self is the reference to the current object
    # instance attributes represent properties with corresponding values of each object
    def __init__(self, name="", serial=""):
        # check if name and serial are not empty
        if name.strip() == "" or serial.strip() == "":
            raise ValueError(
                "Cannot create a student with empty name or serial number."
            )

        self.name = name
        self.serial = serial
        self.grades = {}

    def add_grade(self, exam, grade):
        """Add a new exam result"""
        is_ok = True
        # check if the exam taken is allowed
        if exam not in self.available_exams:
            print(f"{exam} is unknown.")
            is_ok = False

        # check if grade is valid
        if not isinstance(grade, int) or not 18 <= grade <= 30:
            print("The grade must be a valid integer value in the range [18,30].")
            is_ok = False

        if is_ok:
            self.grades[exam] = grade

    def get_grade(self, exam=""):
        """Returns the grade of the student in a given exam"""
        if exam not in self.available_exams:
            print(f"{exam} is unknown.")
        elif exam not in self.grades:
            return None
        else:
            return self.grades[exam]

    def average(self):
        """Returns the student average based on taken exams."""
        if not self.grades:
            return None

        return sum(self.grades.values()) / len(self.grades)

    def missing_exams(self):
        """Returns the missing exams."""
        # alternative solution based on sets:
        # return set(self.available_exams) - set(self.grades)
        missing_exams = []

        for e in self.available_exams:
            if e not in self.grades:
                missing_exams.append(e)

        return missing_exams

    # __str__ defines a default string to print for describing the object
    def __str__(self):
        avg = self.average()

        if avg is None:
            msg = "no exam taken."
        else:
            msg = "average grade is " + str(round(avg, 2))

        return f"{self.name} (matricola number: {self.serial}): " + msg


# Inheritance lets a class reuse or extend the behavior of another class.
# The original class is the parent or base class; the new one is the child or derived class.
class PhDStudent(Student):
    def __init__(self, name="", serial="", research_topic=""):
        # super() calls a method from the parent class.
        super().__init__(name, serial)
        self.research_topic = research_topic

    def __str__(self):
        return f"{self.name} ({self.serial}), PhD student in {self.research_topic}"


class Course:
    def __init__(self, title=""):
        if title.strip() == "":
            raise ValueError("A course title cannot be empty.")

        self.title = title
        self.students = {}

    def add_student(self, student):
        """Add a student to the course."""
        # check if the student is already registered to the course
        if student.serial in self.students:
            print(
                f"The student {student.name} (matricola: {student.serial}) is already registered to the course."
            )
        else:
            self.students[student.serial] = student

    def course_average(self):
        """Returns the average course grade considering all the students."""

        averages = [
            student.average()
            for student in self.students
            if student.average() is not None
        ]

        # print(averages)

        if not averages:
            return None

        return round(sum(averages) / len(averages), 2)

    def __str__(self):
        return f"{self.title}"


# main
s1 = Student("Stefano", "A37398")
print("the name of the student s is", s1.name)

s1.add_grade("Databases", 23)
db_result = s1.get_grade("Databases")
print(f"the student {s1.name} received {db_result} in databases")

s1.add_grade("Python", 30)

s1_avg = s1.average()
print(f"the average grade of the student {s1.name} is {s1_avg}")

m_exams = ", ".join(s1.missing_exams())
print(f"the missing exams of the student {s1.name} are: {m_exams}")

s2 = Student("Alice", "A43784")
print(s2)

s2.add_grade("Statistics", 29)
print(s2)

s2_m_exams = ", ".join(s2.missing_exams())
print(f"the missing exams of the student {s2.name} are: {s2_m_exams}")

# create a PhD student
ps1 = PhDStudent("Bob", "A42432", "Computer Science")
print(ps1)
ps1.add_grade("Databases", 24)
print(
    f"The student {ps1.name} received the grade {ps1.get_grade("Databases")} in Databases."
)

c1 = Course("Data Science")
c1.add_student(s1)
c1.add_student(s2)
s3 = s1
c1.add_student(s3)

print(f"Number of students of course {c1.title}: {len(c1.students)}")

print(s1.average())
print(s2.average())

c1_average = c1.course_average()
print(f"The grade average of students in course {c1.title} is {c1_average}.")
