shoppingList = ['Milk', 'Cheese', 'Butter']


# for i in range(len(shoppingList)):
#     shoppingList[i] = shoppingList[i] + "+"
#     print(shoppingList[i])


myList = [1, 2, 3, 4, 5, 6, 7]
# print(myList)
# myList.insert(0, 11) # beginning of list
# print(myList)
# myList.append(55) # end of list
# print(myList)

# newList = [11, 12, 13, 14]
# myList.extend(newList)
# print(myList)

varList = ['a', 'b', 'c', 'd', 'e', 'f']

# print(varList[1:])

# varList[0:2] = ['x', 'y']

# print(varList)

# varList.pop(1)
# print(varList)

# del varList[1]
# print(varList)

# varList.remove('e')
# print(varList)

searchList = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# if 100 in searchList:
#     print(searchList.index(20))
# else:
#     print('Value not in list')


def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'Value does not exist in this list'


# print(searchinList(searchList, 20))

a = [0, 1, 2, 3, 4, 5, 6]
# print(sum(a)/len(a))

# myNewList = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     myNewList.append(value)
# average = sum(myNewList)/len(myNewList)

# print('Average: ', average)

q = 'spam-spam2-spam3'
delimiter = '-'
w = q.split(delimiter)
# print(w)
# print(delimiter.join(w))

numbers = [1, 3, 2, 5, 4, 6, 7]
numbers.sort()
print(numbers)
