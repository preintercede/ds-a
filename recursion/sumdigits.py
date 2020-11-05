def sumOfDigits(n):
    # assert n >= 0 and int(n) == n, 'Positive integers only'
    if n == 0:
        return 0
    elif n < 0:
        print('Positive integers only')
    else:
        return int(n % 10) + sumOfDigits(int(n/10))


print(sumOfDigits(54))
print(sumOfDigits(1234))
print(-12)
print(sumOfDigits(-123))
