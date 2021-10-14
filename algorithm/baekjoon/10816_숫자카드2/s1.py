import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
hash_cards = {}
for card in cards:
    hash_cards[card] = hash_cards.get(card, 0) + 1

res = []
M = int(input())
find = list(map(int, input().split()))

for c in find:
    res.append(hash_cards.get(c, 0))

print(*res)