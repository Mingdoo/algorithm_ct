N = int(input())
q, r = divmod(N, 5)
if r == 3:
    print(q+1)
elif r == 4:
    if q == 0:
        print(-1)
    else:
        print(q+2)
elif r == 0:
    print(q)
elif r == 1:
    if q == 0:
        print(-1)
    else:
        print(q+1)
elif r == 2:
    if q <= 1:
        print(-1)
    else:
        print(q+2)