import heapq, sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    input()

    queue = list(map(int, input().split()))
    heap = []
    while queue:
        v = queue.pop(0)
        heapq.heappush(heap, v)
    heap = [-1] + heap

    idx = len(heap) - 1
    answer = 0
    while idx > 0:
        answer += heap[idx]
        idx = idx // 2

    print(f'#{tc} {answer - heap[len(heap) - 1]}')
