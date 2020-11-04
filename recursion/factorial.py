def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive number.'
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(4))
print(factorial(-1))
print(factorial('n'))
