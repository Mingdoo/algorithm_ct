from sys import stdin
from collections import Counter

input = stdin.readline


def minecraft(g, b):
    gg = Counter(g)
    ret = []  # (시간, 땅의 높이)
    # 깍는게 시간이 더 많이 걸리니까 깍는걸 더 적게하는 높은 곳부터 시작
    # 땅의 높이가 가장 높은곳에서 낮은 곳으로
    for h in range(max(gg.keys()), -1, -1):
        gt = 0
        inventory = b
        needed = 0
        for gh, gc in gg.items():
            # 지정 높이(h)보다 높은 곳은 깍아서 인벤토리로
            if h < gh:
                inventory += (gh - h) * gc
                gt += 2 * (gh - h) * gc
            # 지정 높이(h)보다 낮은 곳은 갯수 확인
            elif h > gh:
                needed += (h - gh) * gc
                gt += (h - gh) * gc

        # 지정된 높이(h)보다 작은 곳을 채울 블록이 있는지 확인
        if inventory >= needed:
            ret.append([gt, h])
        # 없으면 한칸 내려감
    ret.sort(key=lambda x: (x[0], -x[1]))
    return ret[0]


if __name__ == "__main__":
    N, M, B = map(int, input().split())
    grounds = []
    for _ in range(N):
        grounds.extend(list(map(int, input().split())))
    res = minecraft(grounds, B)
    print(res[0], res[1])