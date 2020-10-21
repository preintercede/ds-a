def isUnique(string):
    letters = {}
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True
    return True


print(isUnique('abc'))
print(isUnique('abcdc'))
print(isUnique('abcdefghijklmnopqrstuvwxyz'))
print(isUnique('abcdefghijklmnopqrstuvwxyzz'))
print(isUnique('dsfadsfas'))
print(isUnique(''))
