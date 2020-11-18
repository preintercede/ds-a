myDict = {'name': 'Bob', "age": 20}
myDict['age'] = 21  # O(1)
myDict['address'] = '123 Street St'  # O(1)
# print(myDict)

newDict = {'name': 'Bobby', 'age': 30,
           'city': 'Los Angeles', 'education': 'Bachelors'}


def traverseDict(dict):
    for key in dict:  # O(n)
        print(key, dict[key])


# traverseDict(newDict)

def searchDict(dict, value):
    for key in dict:  # O(n)
        if dict[key] == value:
            return key, value
    return 'Value does not exist'


# print(searchDict(newDict, 'Los Angeles'))

# newDict.clear()
# print(newDict)


# print(newDict2)
