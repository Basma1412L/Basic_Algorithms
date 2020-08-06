
## Example Test Case of Ten Integers
import random
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max=-1
    min=1000000000
    for i in ints:
        if i>max:
            max=i
        if i<min:
            min =i
    return (min,max)
    pass

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


l = [i for i in range(50, 1000)]  # a list containing 50 - 999
random.shuffle(l)

print ("Pass" if ((50, 999) == get_min_max(l)) else "Fail")


l = [i for i in range(-10,0)]  # a list containing -10, -1
random.shuffle(l)
print ("Pass" if ((-10, -1) == get_min_max(l)) else "Fail")