myNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def findPairs(list, n):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if (list[i]+list[j] == n):
                print(list[i], list[j])


findPairs(myNums, 23)
