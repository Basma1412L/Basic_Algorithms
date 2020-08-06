

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(array, target, mid_index + 1, end_index)


def binary_search_pivot(array,start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]
    post_mid_element = array[mid_index+1]
    pre_mid_element = array[mid_index -1]
    first_element = array[start_index]

    if mid_element > post_mid_element:
        return mid_index
    elif pre_mid_element>mid_element:
        return mid_index-1
    elif mid_element < first_element:
        return binary_search_pivot(array,start_index, mid_index-1)
    else:
        return binary_search_pivot(array, mid_index + 1, end_index)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot_index=binary_search_pivot(input_list,0,len(input_list)-1)
    if (input_list[pivot_index]==number):
        return pivot_index
    left=binary_search_recursive(input_list[:pivot_index+1],number,0,pivot_index)
    if (left==-1):
        right=binary_search_recursive(input_list[pivot_index+1:],number,0,len(input_list[pivot_index+1:])-1)
    else:
        return left
    if not(right==-1):
        return pivot_index+right+1
    else:
        return -1


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
