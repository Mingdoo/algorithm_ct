inp = list(map(int, input().split()))

if inp == sorted(inp):
    print('ascending')
elif inp == sorted(inp, reverse = True):
    print('descending')
else:
    print('mixed')