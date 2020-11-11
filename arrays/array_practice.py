from array import *

# create and traverse an array

my_arr = array('i', [1, 2, 3, 4, 5])


def traverseArr(arr):
    for i in arr:
        print(i)


traverseArr(my_arr)

# access individual element through index

print('---')
print(my_arr[4])

# append any value to array using append

print('---')
my_arr.append(6)
print(my_arr)


# insert value to an array using insert

print('---')
my_arr.insert(0, 11)
print(my_arr)


# extend array using extend

print('---')
my_arr1 = array('i', [10, 11, 12])
my_arr.extend(my_arr1)
print(my_arr)


# add items from  list into array using fromlist

print('---')
tempList = [20, 21, 22]
my_arr.fromlist(tempList)
print(my_arr)


# remove array element using remove

print('---')
my_arr.remove(22)
print(my_arr)

# remove last array element using pop

print('---')
my_arr.pop()
print(my_arr)

# fetch element through its index using index

print('---')
print(my_arr.index(20))

# reverse array using reverse

print('---')
my_arr.reverse()
print(my_arr)

# get array buffer info through buffer_info

print('---')
print(my_arr.buffer_info())

# check for num of occurences using count

print('---')
print(my_arr.count(11))

# convert array to string using tostring

print('---')
strTemp = my_arr.tostring()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)

# convert array to python list with the same elements using tolist

print('---')
# print(my_arr.tolist())


# slice elements from array

print('---')
print(my_arr[1:4])
