# define a Python function that returns the Least Frequent Character in a string (returns the chars with the minimum frequency)
def least_freq_chars(s):
    f = {}
    for c in s:
        if c in f:
            f[c] += 1
        else:
            f[c] = 1
    
    # get the minimum frequency
    the_min = min(f.values())
    
    # determine the items of f with minimum frequency
    the_least_chars = []
    for e in f:
        if f[e] == the_min:
            the_least_chars.append(e)
    
    return the_least_chars
    
  
s = "things never change if you do not try"
print(least_freq_chars(s))