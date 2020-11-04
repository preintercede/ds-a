def fibbonaci(n):
    if n < 0:
        print('Only positive integers allowed')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)


print(fibbonaci(10))
print(fibbonaci(2))
