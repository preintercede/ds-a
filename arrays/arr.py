from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, 1.6])

# print(arr2)

# O(n) beginning of array
# O(1) at end of array
# O(n) at the middle of array
#arr1.insert(2, 9)
# print(arr1)


def traverseArray(array):
    for i in array:  # O(n)
        print(i)


traverseArray(arr1)
