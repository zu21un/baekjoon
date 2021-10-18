# https://www.acmicpc.net/problem/15651

N, M = map(int, input().split())

def dfs(arr, N, M):
    if 0 in arr:
        idx = arr.index(0)
        for i in range(1, N + 1):
            new_arr = arr[:]
            new_arr[idx] = i
            dfs(new_arr, N, M)
    else:
        result = ' '.join(map(str, arr))
        print(result)
        return

dfs([0]*M, N, M)
           
        