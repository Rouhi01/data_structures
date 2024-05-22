def insert(array, value):
    """Insert into unsorted array"""
    array = array[:len(array)] + [value]
    return array


# array = [10, 35, 3, 88, 34, 24, 98, 9]
# value = 3
# print(insert(array, value))

def insert_2(array, value):
    """Insert into sorted array"""
    index = len(array)
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if value == array[mid]:
            index = mid
            break
        elif value > array[mid]:
            left = mid + 1
        else:
            right = mid -1
    else:
        index = left

    if index == len(array):
        array = array[:index] + [value]
    else:
        array = array[:index] + [value] + array[index:]
    return array


# array = [1, 2, 3, 4, 5, 8, 9, 11, 30, 44, 54, 64]
# value = 60
# print(insert_2(array, value))