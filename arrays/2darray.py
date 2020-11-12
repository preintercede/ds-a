import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5],
                      [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# insert adds to beginning
# newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)

# append adds to end
# newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)


# access elements of 2d array
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])


# accessElements(twoDArray, 1, 2)


# traverse 2d array

def traverse2D(array):
    for i in range(len(array)):  # O(mn)
        for j in range(len(array[0])):
            print(array[i][j])


# traverse2D(twoDArray)

def search2DArray(array, value):
    for i in range(len(array)):  # O(mn)
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index ' + str(i) + " " + str(j)
    return 'Cannot find the element'


# print(search2DArray(twoDArray, 14))


# delete 2d array

newTwoDArray = np.delete(twoDArray, 1, axis=1)
print(newTwoDArray)
