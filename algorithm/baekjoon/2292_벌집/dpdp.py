def solution(arr):
    global N, answer, visited
    N = len(arr)
    answer = 5
    arr = sorted(arr, key=lambda a: abs(a))
    for i in range(N):
        if arr[i] == 0:
            return 1
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == 0:
                return 2
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if arr[i] + arr[j] + arr[k] == 0:
                    return 3

    visited = [0] * N
    for i in range(N):
        visited[i] = 1
        dfs(i, arr[i], 1, arr)
        visited[i] = 0
    return answer

def dfs(v, total, idx, arr):
    global answer, N, visited
    if idx >= answer:
        return
    if total == 0:
        if idx < answer:
            answer = idx
        return
    else:
        for j in range(v+1, N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(j, total + arr[j], idx+1, arr)
                visited[j] = 0