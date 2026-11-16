# write a Python function to split a list into a given number of segments
def slice_segments(the_list, segments):
    # proposed solution
    # consider three segments x = len(the_list) / 3
    # output: the_list[0:x], the_list[x, 2x], the_list[2x, 3x]
    length = len(the_list)
    # iterative solution: we need to create the number of segments specified in the parameter 
    # check that segments is a positive integer
    try: 
        segments = int(segments)
    except ValueError:
        print("Segments must be an integer.")
        return None
        
    # check that segments is positive (and not greater than len(the_list))
    if segments < 0 or segments > length:
        raise ValueError("Segments must be in the range [0, len(list)].")
    
    # now segment the list in input
    # compute the size of each segment (use the floor division)
    x = length // segments 
    result = []
    for s in range(segments):
        lower_bound = s * x
        upper_bound = (s + 1) * x
        item = the_list[lower_bound:upper_bound]
        result.append(item)
    
    return result

animals = ["dog", "cat", "elephant", "tiger", "bear", "lion", "turtle"]
print(slice_segments(animals, 3))
# expected output on the example: ["dog", "cat"], ["elephant", "tiger"], ["bear", "lion"]