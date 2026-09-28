# EXERCISE A
# ============#
# read the code and trace the execution
items = [12, 7, 15, 10, 18]
s = 0
c = 0

for v in items:
    if v > 10:
        s = s + v
        c = c + 1

r = s / c
print(r)

# what happens if items is empty
# this solution only manages when items is empty but not when the items are all below the threshold
items = []
s = 0
c = 0

if items:  # or if len(items) != 0
    for v in items:
        if v > 10:
            s = s + v
            c = c + 1

    r = s / c
    print(r)
else:
    print("Empty lists are not valid")

# alternative solution where we manage the case that all items are below the threshold
items = [12, 7, 15, 10, 18]
s = 0
c = 0

for v in items:
    if v > 10:
        s = s + v
        c = c + 1

if c != 0:
    r = s / c
    print(r)
else:
    print("We need a list with at least one value over the threshold")

# EXERCISE B
# ============#
# we have a dataset with daily temperatures
# we want a develop a program to discover:
# the average temperature;
# the maximum temperature;
# the number of days with temperatures above 22 °C.

# what we expect as input: a sequence of temperatures

# what we expect as output: i) avg temperature, ii) max temperature, iii) the number of days above the threshold

# python code
t = [19, 19.5, 23, 24.5, 24, 27, 27.2]
t_len = len(t)  # calculate the number of items in t
t_sum = sum(t)
t_avg = t_sum / t_len
t_max = max(t)

# the number of items over threshold can be calculated using list comprehension
v_22 = 0
for v in t:
    if v > 22:
        v_22 = v_22 + 1

print("The average temperature is", t_avg)
print("The maximum temperature is", t_max)
print("The number of temperatures over 22 is", v_22)

# what happens if the input is not like you expect
t = [19, "19.5", 23, "ND", 24, 27, 27.2]


if t_len > 0:
    t_avg = t_sum / t_len
    print("The average temperature is", t_avg)
else:
    print("Not possible to calculate the average")
if t_max > 0:
    print("The maximum temperature is", t_max)
else:
    print("Cannot determine the maximum temperature")

print("The number of temperatures over 22 is", v_22)

# alternative version with the use of function


# the function results the i) average temperature, ii) the max temperature, iii) the number of values over the threshold of th
# input: t is a list of temperatures (non numerical values are discarded), th is the threshold to consider
# output: t_avg, t_max, v_22
def temperature_analysis(t, th):
    t_len = 0
    t_sum = 0
    t_max = 0
    v_th = 0
    for v in t:
        if isinstance(v, (float, int)):
            t_sum += v  # t_sum = t_sum + v
            t_len += 1

            if v > t_max:
                t_max = v

            if v > th:
                v_th = v_th + 1

    t_avg = None
    if t_len > 0:
        t_avg = t_sum / t_len

    return t_avg, t_max, v_th


t_values = [19, "19.5", 23, "ND", 24, 27, 27.2]
r_avg, r_max, r_th = temperature_analysis(t_values, 23)

if r_avg is not None:
    print("The average temperature is", t_avg)
else:
    print("Not possible to calculate the average")


# EXERCISE C
# ============#
# Design a function that takes a list of travel times and calculates the average
# only values in the range [1, 120] are valid
# missing values and out-of-range values are ignored


# EXERCISE D
# ============#
# build a basic classifier in Python
# given a list of student evaluations (valid results are integer in the range [0,100]), classify the student into the following categories:
# < 50: not qualified (NQ);
# 50 <= e <= 69: basic knowledge (BS);
# 70 <= e <= 84: medium knowledge (MD);
# >= 85: advanced knowledge (AD).
# None in input produces None as output
# values outside the range (or non-integer values) produce None as output
def student_classifier(s):
    result = []

    for e in s:
        if e is None or not isinstance(e, int) or not 0 <= e <= 100:
            result.append(None)
        elif e < 50:
            result.append("NQ")
        elif e <= 69:
            result.append("BS")
        elif e <= 84:
            result.append("MD")
        else:
            result.append("AD")

    return result


# main code
student_evaluations = [42, 65, 78, None, "", 91, -1, 105]
student_classifications = student_classifier(student_evaluations)
print(student_classifications)
# expected result on the input:
# student_classifications = ['NQ', 'BS', 'MD', None, 'AD', None, None]

# EXERCISE E
# ============#
# A company tracks the daily number of visits to a service:
# A day is classified as:
# - low if the number of visits is less than 100;
# - normal if it is between 100 and 149;
# - high if it is at least 150.
# Design a Pyhton code that produces:
# 1. the classification of each day (print error when the item is not integer or missing);
# 2. the number of days in each category;
# 3. the average number of visits;
# 4. the day with the highest number of visits.
# Manage possible input errors:
# - ignore missing values in countings
# - ignore non integer values in countings
visits = [120, 135, 98, None, "error", 142, 120.5, 150, -1, 160]

low_days = 0
normal_days = 0
high_days = 0

total_visits = 0
valid_days = 0

highest_visits = None
highest_day = None

current_day = 0
for v in visits:
    current_day += 1

    if v is None or not isinstance(v, int) or v < 0:
        print("Day", current_day, ": error")
        continue

    if v < 100:
        category = "low"
        low_days += 1
    elif v < 150:
        category = "normal"
        normal_days += 1
    else:
        category = "high"
        high_days += 1

    print("Day", current_day, ":", category)
    total_visits += v
    valid_days += 1

    # update the highest value
    if highest_visits is None or v > highest_visits:
        highest_visits = v
        highest_day = current_day

print("Number of low days:", low_days)
print("Number of normal days:", normal_days)
print("Number of high days:", high_days)

if valid_days > 0:
    average = total_visits / valid_days
    print("Average number of visits:", average)
    print("Day with the highest number of visits:", highest_day)
    print("highest number of visits:", highest_visits)
else:
    print("No valid data on visits")

# expected output:
# day 1: normal
# day 2: normal
# day 3: low
# day 4: error
# day 5: error
# day 6: normal
# day 7: error
# day 8: high
# day 9: low
# day 10: high
# Number of low days: 2
# Number of normal days: 3
# Number of high days: 2
# Average number of visits: 127.42857142857143
# Day with the highest number of visits: 10
# highest number of visits: 160
