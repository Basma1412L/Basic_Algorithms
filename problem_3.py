def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list=mergesort(input_list)
    length=len(input_list)
    arrL = []
    arrR = []
    if length%2==0:
        i = length-1
        while i>0:
            arrL.append(input_list[i])
            arrR.append(input_list[i-1])
            i-=2
    else:
        i = length-1
        arrL.append(input_list[i])
        i-=1
        while i>0:
            arrL.append(input_list[i])
            arrR.append(input_list[i-1])
            i-=2
    left=''.join([str(x) for x in arrL])
    right = ''.join([str(x) for x in arrR])
    return [int(left),int(right)]



def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case3 = [[1,0,2,3,4], [431, 20]]
test_function(test_case2)
test_function(test_case3)