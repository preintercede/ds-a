from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, 1.6])

# print(arr2)

# O(n) beginning of array
# O(1) at end of array
# O(n) at the middle of array
#arr1.insert(2, 9)
# print(arr1)

# traverse


def traverseArray(array):
    for i in array:  # O(n)
        print(i)


# traverseArray(arr1)

# get element of index

def accessElement(array, index):
    if index >= len(array):  # O(1)
        print('There is no element in this index')
    else:
        print(array[index])


# accessElement(arr1, 5)

#search in array

def searchInArray(array, value):
    for i in array:  # O(n)
        if i == value:
            return array.index(value)
    return "The element does not exist in this array"


# print(searchInArray(arr1, 5))


# remove element from array

arr1.remove(4)
print(arr1)
