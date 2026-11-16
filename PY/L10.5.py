import sys

# determine the output of the following codes
# A #
s = "never change your mind"
s1 = s.split()
s2 = " ".join(s1[1::2])

print(s2)  # result: change mind

# B #
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = [n for r in m for n in r]
print(l) # result [1,2,3,4,5,6,7,8,9]

# alternative syntax
l = []
for r in m:
    for n in r:
        l.append(n)

# C #
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

print([x for x in l1 if x in l2]) # result: [4, 5]

# D #
print([x for x in range(10, 100) if str(x) == str(x)[::-1]])
# output: [11, 22, 33, 44, 55, 66, 77, 88, 99]

# E #
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d = {}
for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
    d[k1] = v1
    d[k2] = v2
print(d)

# content of dictionary d after the first iteration: 
d = {
    "a": 1,
    "b": 3
}

# content of dictionary d after the second iteration (and final):
d = {
    "a": 1,
    "b": 2,
    "c": 4
}

sys.exit()
