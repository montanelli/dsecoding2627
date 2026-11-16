# write a Python function to remove the first x elements and the last Y elements from a list in input
# the function has to check:
## x, y must be valid parameters: integer numbers that are existing in the input list
## x < y
def slice_list(the_list, x, y):
    try: 
        x = int(x)
        y = int(y)
    except ValueError:
        print("only integer numbers are valid parameters.")
        return None 
    
    if x < 0 or y < 0:
        raise ValueError("Negative values not allowed.")
    
    if x >= y:
        raise ValueError("x must be lower than y parameters.")
    
    if (x >= len(the_list)) or (y >= len(the_list)):
        raise ValueError("x,y must be lower than the length of the input list")
    
    return the_list[x:-y]  
    
# main
animals = ["dog", "cat", "elephant", "tiger", "bear", "lion"]
print(slice_list(animals, 2, 1))
# expected output: [ "elephant", "tiger", "bear" ]