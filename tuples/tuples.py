newTuple = 'a', 'b', 'c', 'd', 'e'
# newTuple1 = tuple('abcde')

# print(newTuple)
# print(newTuple1)

# print(newTuple[1])

# for i in newTuple:
#     print(i)

# for i in range(len(newTuple)):  # O(n)
#     print(newTuple[i])


def searchTuple(pTuple, value):
    for i in pTuple:  # O(n)
        if i == value:
            return pTuple.index(i)
    return 'Value not found in the tuple'


print(searchTuple(newTuple, 'b'))
