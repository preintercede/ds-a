def permutation(l1, l2):
    l2.reverse()
    if l1 == l2:
        return True
    else:
        return False


print(permutation([1, 2, 3], [2, 3, 1]))
