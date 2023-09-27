num_dict = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 0, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
}

N, K, P, X = map(int, input().split())

change = [[-1 for _ in range(10)] for _ in range(10)]


def get_convert_cnt(n, m):
    before = num_dict[n]
    after = num_dict[m]
    cnt = 0
    for a, b in zip(before, after):
        cnt += a ^ b

    return cnt


for i in range(10):
    for j in range(10):
        change[i][j] = get_convert_cnt(i, j)

num = [0 for _ in range(K)]

for i in range(K):
    num[-i - 1] = (X // (10**i)) % 10

changed = 0
idx = 0

stack = []
num_set = set()

stack.append([num, changed, idx])

while stack:
    num, changed, idx = stack.pop()
    if changed > P:
        continue
    if changed >= 1:
        convert_num = 0
        for n in num:
            convert_num *= 10
            convert_num += n
        if 1 <= convert_num <= N:
            num_set.add(convert_num)
    if idx >= K:
        continue
    for i in range(10):
        _num = num[:]
        a = _num[idx]
        b = i
        _num[idx] = b
        c = change[a][b]
        stack.append([_num, changed + c, idx + 1])

print(len(list(num_set)))
