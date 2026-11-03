# lamba functions
# Lambda functions are similar to user-defined functions but without a name.
# They're commonly referred to as anonymous functions. Syntax
# lambda argument(s): expression
## lambda is a keyword in Python for defining the anonymous function.
## argument(s) is a placeholder, that is a variable that will be used to hold the value you want to pass into the function expression. A lambda function can have multiple variables depending on what you want to achieve
## expression is the code you want to execute in the lambda function.

# example1: single parameter
square = lambda x: x**2
print(square(4))

# example2: two params
s = lambda x, y: x + y
print(s(4, 5))


# equivalent syntax
def s(x, y):
    return x + y


# example3: use of conditions
gt = lambda a, b: a if a > b else b
print(gt(6, 5))
print(gt(5, 6))
print(gt(6, 6))

# lambda functions are useful when you need a short function to pass to another function like sorted, map, or filter
words = ["databases", "AI", "statistics", "model", "data", "form"]
# sort the list of items in input according to the length of each word
# sorted_ python built-in function to sort a given iterable
sorted_result = sorted(words, key=lambda w: (len(w), w))
print(sorted_result)

# sort the list of tuples in input according to the value of the second item in each tuple
my_tuples = [(1, 3), (4, 1), (2, 2)]
sorted_tuples = sorted(my_tuples, key=lambda t: t[1])
print(sorted_tuples)

# sort the students from highest to lowest considering the grade.
# sort by name in case of same grade
students = [
    {"name": "Alice", "grade": 28},
    {"name": "Mark", "grade": 22},
    {"name": "Sarah", "grade": 28},
    {"name": "George", "grade": 19},
    {"name": "Hector", "grade": 22},
]
sorted_students = sorted(students, key=lambda s: (-s["grade"], s["name"]))
print(sorted_students)

# sort by course and grade
students = [
    {"name": "Alice", "course": "databases", "grade": 28},
    {"name": "Mark", "course": "databases", "grade": 22},
    {"name": "Sarah", "course": "databases", "grade": 28},
    {"name": "George", "course": "python", "grade": 19},
    {"name": "Hector", "course": "python", "grade": 22},
    {"name": "Tom", "course": "python", "grade": 23},
    {"name": "David", "course": "python", "grade": 30},
]

# example with filter
my_data = [1, 2, 3, 4, 5, 6]
even_data = list(filter(lambda x: x % 2 == 0, my_data))
print(even_data)


# map is a Python built-in function that applies a given function to any item of a given iterable
# By default, the map() function returns a map object, which is an iterator. In many cases, we will need to convert this iterator to a list to work with the results directly.
# map(function, iterable, /, *iterables, strict=False)

# apply a 10% discount to each price. Round the result to two decimals
prices = [20.00, 45.50, 30.00, 100.00]
discounted_prices = list(map(lambda p: round(p * 0.9, 2), prices))
print(discounted_prices)

# select the patients with at least three symptoms, then create a list of strings showing the patient id and the corresponding number of symptoms
# sort the result according to the patient id
patients = [
    {"id": "p_001", "symptoms": ["cough", "fatigue", "nausea", "headache"]},
    {"id": "p_005", "symptoms": ["fatigue", "dizziness", "headache"]},
    {"id": "p_002", "symptoms": ["dizziness"]},
    {
        "id": "p_003",
        "symptoms": ["fatigue", "headache", "cough", "nausea", "dizziness"],
    },
    {"id": "p_004", "symptoms": ["fatigue", "cough"]},
]
# step 1: filter
frequent_patients = list(filter(lambda p: len(p["symptoms"]) >= 3, patients))
# step 2: map
patients_with_counts = list(
    map(
        lambda p: {"id": p["id"][-3:], "n_symptoms": len(p["symptoms"])},
        frequent_patients,
    )
)
# step 3: sort by patient id
sorted_patients = sorted(patients_with_counts, key=lambda p: p["id"])
print(sorted_patients)

# expected results on the example:
result = [
    {"id": "001", "n_symptoms": 4},
    {"id": "003", "n_symptoms": 5},
    {"id": "005", "n_symptoms": 3},
]

# we have a dataset of sell operations in supermarkets
# we read the entire dataset from the csv file
import csv

with open("dataset/supermarket.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    records = list(reader)

print(records)

# skip the first row (column header)

# in column 1 we have the branch name of each operation
# in column 7 we have the quantity sold in each transaction
# build a dictionary where keys are branch names and values are corresponding lists of sold quantites


# normalize the list of quantities per branch (use map and lambda function):
# https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)
