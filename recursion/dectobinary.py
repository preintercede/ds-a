def dtob(n):
    assert int(n) == n, "Integers only"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * dtob(int(n/2))


print(dtob(56))
