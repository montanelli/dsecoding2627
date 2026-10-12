# STRING SLICING
################
# [ start:stop:step ]
# start: the index of the first char to slice (default: 0)
# stop: the index of the last char to slice (excluded) (default: end of the string)
# step: the number of chars to move (default = 1)

s = "coding for data science"
# c o d i n g
# 0 1 2 3 4 5
print(s[1:4:1])  # odi
print(s[:])  # coding for data science
print(s[7:])  # for data science
print(s[:6])  # coding
print(s[1:4:2])  # oi
print(s[::2])  # odd chars
print(s[1::2])  # even chars

s1 = "coding"
# c   o  d  i  n  g
# 0   1  2  3  4  5
# -6 -5 -4 -3 -2 -1
print(s1[-1])  # g
print(s1[-4:])  # ding
print(s1[-4:-1])  # din
print(s1[::-1])  # gnidoc
print(s1[-1:-4:-1])  # gni
print(s1[-2::-2])  # ndc
print(s1[-3:-6:-2])  # io

# string concatenation
s1 = "coding"
s2 = "for data management"
s = s1 + " " + s2

# join operation
l = ["coding", "for", "data", "management"]
s = " ".join(l)

# EXERCISE 1.1
############
# write a program that takes a fiscal code in input. The code is formatted as follows:
## MNTSFN77E29
# first 3 chars -> lastname (ABC)
# next 3 chars -> firstname (DEF)
# next 2 chars -> birth year (99)
# next 1 chars -> letter of the month (A:JAN, B:FEB, ...)
# next 2 chars -> day of birth (12)
# the program has to use string slicing to extract the code parts and returns a readable text
# manage if the month is not in range [1,12]
# Translate month in string
# Example of expected output on the example:
## Letters of lastname: MNT
## Letters of Firstname: SFN
## Year: 77
## Month: May
## Day: 29
cf = str(input("Enter a fiscal code: "))


# EXERCISE 1.2
############
# insert a string at a specific index of another one
# expeted output on the example: a wonderful day
s1 = "a day"
s2 = " wonderful"
index = 1


# EXERCISE 1.3
############
# Given an email address, return the part before the @ symbol
# find a way to detect the @ position. Manage if the symbol is missing


# EXERCISE 1.4
############
# given a string in input, return true/false if it is a palindrome
# examples of palindrome words: radar, otto, civic
def check_pal(w, c=True):
    """check if a word in input is palindrome.

    Keyword arguments:
    string -- the word to evaluate
    boolean -- a switch to decide whether to consider the letter cases

    Return:
    bool -- True when palindrome; False otherwise
    """

    if not c:
        w = w.lower()

    if w == w[::-1]:
        return True
    else:
        return False

    # alternative: return w == w[::-1]


def check_pal_iterative(w, c=True):
    """check if a word in input is palindrome using iterations and not string slicing

    Keyword arguments:
    string -- the word to evaluate
    boolean -- a switch to decide whether to consider the letter cases

    Return:
    bool -- True when palindrome; False otherwise
    """

    if not c:
        w = w.lower()

    start = 0
    end = len(w) - 1
    is_pal = True

    while start < end:
        if w[start] != w[end]:
            is_pal = False
            break

        start += 1
        end -= 1

    return is_pal


word = "radar"
word = "Radar"
word = "otto"
print(check_pal(word))


# EXERCISE 1.5
############
# move the last n chars at the beginning of a string
# Expected output on the example: outwork
# check that n is a valid index in the string
s = "workout"
n = 3


# EXERCISE 1.6
############
# Interweave two givan words in input
# use blanks to fill a string if one is shorter than the other
# expected output on the example: "starnodl l"
s1 = "sand"
s2 = "troll"


# EXERCISE 1.7
############
# reverse of the exercise 6: extract two strings from an interwined one
# expected output on the example: sand, troll


# LISTS
#######
# order: each element has a position
# index: each element has an index starting from 0
# mutable: the list content can be manipulated
# heterogeneity: you can have a list with elements of diffent type
seasons = ["autumn", "winter"]

seasons.append("spring")
seasons.insert(1, "summer")
seasons.remove("summer")

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

M1 = [["one", "two", "three"], ["four", "five", "six"]]

l = ["one", "two", "three", "four", "five", "six"]

# lists can be sliced
print(l[0])  # one
print(l[-1])  # six
print(l[1:2])  # two
print(l[1::2])  # two four six

# LIST COMPREHENSION
# compact syntax for iterations over lists
l = ["coding", "for", "data", "management"]

# return only the elements that are longer than 4 chars
result = []
for w in l:
    if len(w) > 4:
        result.append(w)

# list comprehension version:
# [expression for element in sequence if condition]
result = [w for w in l if len(w) > 4]

# return the odd chars of a list element if it is longer than 4 chars, and return the even chars otherwise
result = [w[::2] if len(w) > 4 else w[1::2] for w in l]


# EXERCISE 2.1
############
# Build a matrix M1 of size K where an element of index (i,j) contains the value corresponding to i+j.
# Return also i) a list with the average of values by row, ii) a list with the average of values by column
# Expected output:
# Matrix M1:
# [[0, 1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 6]
# [3, 4, 5, 6, 7]
# [4, 5, 6, 7, 8]]

# Row averages: [2.0, 3.0, 4.0, 5.0, 6.0]
# Column averages: [2.0, 3.0, 4.0, 5.0, 6.0]


# the function returns a matrix with corresponding averages by row and column
# the parameter k is the size of the matrix to build
def matrix_and_averages(k):
    # matrix creation
    M = [[i + j for i in range(k)] for j in range(k)]

    # average by row: the output is a list where each element is the avg value of the corresponding row
    row_avg = [sum(r) / len(r) for r in M]

    # average by column: the output is a list where each element is the avg value of the corresponding column

    col_avg = [sum(M[i][j] for i in range(k)) / k for j in range(k)]

    return M, row_avg, col_avg


# main
k = 5
matrix, r_average, c_average = matrix_and_averages(k)

for row in matrix:
    print(row)

print(f"the average of rows is: {r_average}")
print(f"the average of columns is: {c_average}")

# EXERCISE 2.2
############
# given a list, create a new one that:
# - removes leading and trailing spaces (function strip);
# - ignores empty strings;
# - converts each remaining name to title case (function title).
# expected output on example: ['Alice', 'Bob', 'Charlie', 'David']
names = ["  alice", "BOB  ", "  ChArLiE  ", "", "   ", "david"]


# EXERCISE 2.3
############
# Mask the values of list in input.
# Create a new list in which all characters except the first two and the last two are replaced with *.
# expected output on example: ['AB****56', 'XY****54', 'CD****12', 'EF42']
codes = ["AB123456", "XY987654", "CD000012", "EF42"]


# EXERCISE 2.4
############
# Create a nested list containing the length of every word in each sentence.
# hint: use split function
# Expected result on example: [[6, 2, 10],[4, 7, 4, 6],[5, 5, 8, 6]]
sentences = [
    "Python is expressive",
    "Data science uses models",
    "Lists store multiple values",
]


# EXERCISE 2.5
############
# Given a lowercase string, move every letter forward by K positions in the alphabet. Preserve spaces and non alphabetic chars:
# hint: use % (module operator) to manage shifts in the end of alphabet
# hint: use join function to transform the final list into a string
# Expected result on example: sbwkrq lv dpdclqj
message = "python is amazing"
alphabet = "abcdefghijklmnopqrstuvwxyz"
k = 3


# EXERCISE 2.6
############
# write a function for encoding and decoding according to exercise 5


# TUPLES
########
# tuples are like lists but immutable
brands = ("Apple", "IBM", "Google")
print(brands[2])
brands[0] = "Microsoft"


# SETS
######
# sequences of items without position and without duplicates
# unordered: no access by index/position
# uniqueness: not possible to store two identical items
# Mutable: items can change
# heterogenous: you can stor mixed types
fruits = set()
fruits.add("pear")
fruits.add("apple")
fruits.add(12)
fruits.add("pear")
fruits.remove("apple")
fruits.clear()

f_tom = {"Mark", "Angela", "Ann", "John"}
f_carol = {"Alice", "Mark", "Ann", "William"}

print(f_tom | f_carol)  # union: Mark, Angela, Ann, John, Alice, William
print(f_tom & f_carol)  # intersection: Mark, Ann
print(f_tom - f_carol)  # set difference: Angela, John
print(f_carol - f_tom)  # set difference: Alice, William

# you have a list of items:
tools = [
    "mouse",
    "printer",
    "scanner",
    "laptop",
    "printer",
    "printer",
    "laptop",
    "laptop",
    "laptop",
    "mouse",
]

unique_tools_set = set(tools)  # the result is a set with unique values
unique_tools_list = list(unique_tools_set)  # the result is a list with unique values


# EXERCISE 3.1
############
# Create a set containing all the unique lowercase words.
# expected result on example: 'python', 'is', 'simple', 'and', 'powerful', 'flexible'
sentence = "Python is simple and Python is powerful and flexible"


# EXERCISE 3.2
############
# Given a set of permissions, find:
# 1. users with both read and write access;
# 2. users with read access but not write access;
# 3. users with at least one permission;
# 4. users with no permission;
# 5. users with exactly one type of permission.
all_users = {"alice", "bob", "carol", "david", "emma", "frank", "grace"}

read_access = {"alice", "bob", "carol", "david", "emma"}
write_access = {"alice", "carol", "frank"}
admin_access = {"alice", "grace"}


# DICTIONARIES
############
# a sequence of elements with (key: value) structure (associative array)
# Ordered: elements have a specific position (key)
# Indexed: each element has a unique key
# Heterogeneous: you can mix elments with different data type
# Mutable: you can edit the dict content
capitals = {"Italy": "Rome", "France": "Paris", "Germany": "Berlin"}

# reading elements
print(capitals["France"])

# print all the items of the dictionary
for k in capitals.keys():
    print(capitals[k])

# useful methods on dictionaries:
capitals.items()  # returns the k, v pairs of the dict
capitals.values()  # returns a list with the dict values
capitals.keys()  # returns a list with keys in dict

# editing/inserting
capitals["Spain"] = "Madrid"

# deleting elements
del capitals["France"]


# EXERCISE 4.1
############
# Given a sentence, create a dictionary in which:
# - each key is a lowercase word;
# - each value is the number of occurrences of that word.
sentence = "Python is simple and Python is powerful and flexible"


# EXERCISE 4.2
############
# Given a dictionary containing products and prices:
# Create a new dictionary containing only products whose price is between €50 and €300, inclusive. Apply a 10% discount to their prices.
products = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 80,
    "monitor": 350,
    "webcam": 95,
    "printer": 220,
}


# EXERCISE 4.3
############
# Given a dictiory with exam results. Find:
# 1. the highest score;
# 2. all students who obtained it.
# Expected result on example:
# Highest score: 91
# Best student(s): ['Bob', 'David']
scores = {"Alice": 82, "Bob": 91, "Carol": 78, "David": 91, "Emma": 87}

max_performance = max(scores.values())
print(f"the highest performance is {max_performance}")

max_students = []
for k, v in scores.items():
    if v == max_performance:
        max_students.append(k)

# alternative with list comprehension:
# max_students = [ k for k, v in scores.items() if v == max_performance ]

print(f"the student with highest performance are {max_students}")


# EXERCISE 4.4
############
# Given a dictionary that associates students with their degree programmes
# Create a dictionary that associates each programme with the list of students enrolled in it.
# Expected result on example:
# { "Data Science": ["Alice", "Carol"],
#    "Computer Science": ["Bob", "Emma"],
#    "Economics": ["David"] }

programmes = {
    "Alice": "Data Science",
    "Bob": "Computer Science",
    "Carol": "Data Science",
    "David": "Economics",
    "Emma": "Computer Science",
}


# EXERCISE 4.5
############
# given a dictionary with exam results, create a dictionary associating each student with their average score.
# Expected result on example: {'Alice': 23.25, 'Bob': 24.67, 'Carol': 21.67}
students = {
    "Alice": {"Python": 25, "Databases": 28, "Statistics": 22, "Machine Learning": 18},
    "Bob": {"Python": 20, "Databases": 28, "Statistics": 26},
    "Carol": {"Python": 25, "Databases": 11, "Mathematics": 29},
}

student_avgs = {}
for s_name, s_exams in students.items():
    s_avg = sum([v for v in s_exams.values()]) / len(s_exams.values())
    student_avgs[s_name] = round(s_avg, 2)

print(student_avgs)


# EXERCISE 4.6
############
# Consider the exam results of the Exercise 5. For each student, return the list of missing exams
# consider only the exams that appear at least once in the dictionary
# expected result on example: {'Alice': ['Mathematics'], 'Bob': ['Mathematics', 'Machine Learning'], 'Carol': ['Statistics', 'Machine Learning']}
# hint: the function set applied to a dictionary create a set with the dict keys
students = {
    "Alice": {"Python": 25, "Databases": 28, "Statistics": 22, "Machine Learning": 18},
    "Bob": {"Python": 20, "Databases": 28, "Statistics": 26},
    "Carol": {"Python": 25, "Databases": 11, "Mathematics": 29},
}

student_courses = {}  # list of list with taken courses

for s_name, s_exams in students.items():
    student_courses[s_name] = set(s_exams.keys())

all_courses = set()
for item in student_courses:
    all_courses = all_courses | student_courses[item]

missing_courses = {}
for s_name, s_courses in student_courses.items():
    missing_courses[s_name] = all_courses - s_courses

print(missing_courses)
