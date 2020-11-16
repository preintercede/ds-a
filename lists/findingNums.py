import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    12, 13, 14, 15, 16, 17, 18, 19, 20])


def findingNum(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            print(i)
    print('Number does not exist in this array.')


findingNum(myArray, 133)
