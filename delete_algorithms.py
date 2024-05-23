def delete(array, value):
    """Delete a value from unsorted array"""
    index = -1
    for i in range(0, len(array)):
        if value == array[i]:
            index = i
            break
    if index == -1:
        return 'Value does not exist.'
    else:
        for i in range(index, len(array) -1):
            array[i] = array[i + 1]
        return array[:len(array)-1]

# array = [80, 34, 56, 30, 345, 96, 33, 11, 1]
# value = 568
# print(delete(array, value))


def delete_2(array, value):
    """Delete a value from sorted array"""
    index = -1
    left = 0
    right = len(array) -1
    while left <= right:
        mid = (left + right) // 2
        if value == array[mid]:
            index = mid
            break
        elif value > array[mid]:
            left = mid + 1
        else:
            right = mid -1
    if index == -1:
        return 'Value does not exist.'
    else:
        for i in range(index, len(array)-1):
            array[i] = array[i+1]
        return array[:len(array) -1]

# array = [1, 2, 4, 5, 8, 99]
# value = 1
# print(delete_2(array, value))
