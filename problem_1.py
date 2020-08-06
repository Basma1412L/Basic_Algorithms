def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number<0 or number=="" or not isinstance(number, int)):
        return None
    return binary_search_recursive(number, 0, number-1)


def approxSqrt(n,number):
    lower=n*n
    higher=(n+1)*(n+1)
    if (lower<=number and higher> number):
        return True
    else:
        return False

def binary_search_recursive(target, start_index, end_index):
    if target==0:
        return 0
    elif target==1:
        return 1
    if start_index > end_index:
        return -1
    mid_index = (start_index + end_index) // 2
    sqrt=mid_index*mid_index
    if approxSqrt(mid_index,target):
        return mid_index
    elif target < sqrt:
        return binary_search_recursive(target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(target, mid_index + 1, end_index)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")



def linear_sqrt(n):
    if (n<0 or n=="" or not isinstance(n, int)):
        return None
    i =1
    while i<n:
        power2=i*i
        if (power2==n):
            return i
        i+=1

def test_function(test_case):
    if(len(test_case)==0):
        return
    number = test_case[0]
    if linear_sqrt(number) == sqrt(number):
        print("Pass")
    else:
        print("Fail")

test_function([100])
#expected 10
test_function([49000000])
#trying big number
test_function([-1])
#trying negative numbers
test_function([])
#trying empty test cases
