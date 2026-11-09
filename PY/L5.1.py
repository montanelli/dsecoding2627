# error handling

# syntax error
if True
    print('ok')

# runtime error
my_value = input("specify a number")
number = int(my_value)

# logics error
price = 10
discount = 20
final_price = price + discount

i = 1
while i >= 1:
    print ("current number: ", i)
    i += 1
    
# ask the user to insert the age. Convert the input to integer. Print a message when the input cannot be converted
user_age = input("enter your age: ")

try:
    age = int(user_age)
    print(f"Your age is {age}.")
except ValueError:
    print("Please, enter an integer number as age.")
    
# ask the user to insert two numbers and divide the first by the second. Handle invalid input
try:
    num = float(input("Enter the numerator: "))
    den = float(input("Enter the denominator: "))

    result = num / den
    print(f"The ratio is {result}")
except ValueError:
    print("Please, insert a integer or floating number.")
except ZeroDivisionError:
    print("Dividing by zero is not possible.")

# open a text file, read the content and close the file when you complete the read operation
import csv 
f = None

try:
    f = open("dataset/supermarket.csv", newline="")
    reader = csv.reader(f, delimiter=",")
except:
    print("The file cannot be found")
finally:
    if f is not None:
        f.close()
        print("Read complete, file closed")

# write a function to calculate a discount. raise an error if the price is negative or the discount is not between 0 and 80.
def calculate_discount(price, discount):
    try:
        price = float(price)
        discount = float(discount)
    except ValueError:
        print("price and discount must be integer/float numbers")
        return None
        
    if price < 0:
        raise ValueError("Price cannot be negative.")
    
    if not 0 <= discount <= 80:
        raise ValueError("Discount must belong to range [0,80].")
    
    return price * (1-discount/100)

print(calculate_discount(150, 20))

# a file contains student records on exams. One record per line, three fields with "name, exam, result"
# build a dictionary with exam results for each student and manage possible errors in record specifications
exams = {}

try:
    with open("dataset/exam_results.txt", newline="") as f:
        for line_number, line in enumerate(f, start=1):
            fields = line.strip().split(",")
            
            if len(fields) != 3:
                print((f"Line {line_number}: invalid record, skipping."))
                continue    
            
            student, course, grade = fields
            try:
                grade = int(grade)
            except ValueError:
                print(f"Line {line_number}: invalid grade, skipping.")
                continue
            
            if not 18<= grade <= 31:
                print(f"Line {line_number}: out-of-range grade, skipping.")
                continue
            
            if student not in exams:
                exams[student] = []
                
            exams[student].append({
                "course": course,
                "grade": grade
            })
            
except FileNotFoundError:
    print("Source file not found")
else:
    for student, exams in exams.items():
        print(f"\n{student}:")
        for exam in exams:
            print(f" {exam['course']}: {exam['grade']}")
        