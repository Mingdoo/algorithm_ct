def fac(n):
    if n <= 2:
        return n
    else:
        return n * fac(n-1)

print(fac(20))