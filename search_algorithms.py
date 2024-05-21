def linear_search(array, value):
    for i in range(0, len(array)-1):
        if array[i] == value:
            return f'Index of value is {i}'
    else:
        return 'Value does not exist.'


# array = [5, 2, 3, 33, 89, 1, 11, 20]
# value = 33
# print(linear_search(array, value))

def binary_search(array, value):
    left = 0
    right = len(array) -1
    while left <= right:
        mid = (left + right) // 2
        if value == array[mid]:
            return f'Index of value is {mid}'
        elif value > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return 'Value does not exist.'


# array = [1, 2, 3, 4, 5, 6, 8, 11, 45, 50]
# value = 6
# print(binary_search(array, value))