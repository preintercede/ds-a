from collections import Counter


def is_Permutation(word1, word2):
    if len(word1) != len(word2):
        return False
    counter = Counter()
    for c in word1:
        counter[c] += 1
    for c in word2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


print(is_Permutation("taco cat", "cato tac"))
print(is_Permutation("taco cat", "cato tad"))
print(is_Permutation("dsfv42", "2sdfv4"))
