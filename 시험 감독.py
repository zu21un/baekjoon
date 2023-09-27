N = int(input())

A = map(int, input().split())

B, C = map(int, input().split())

answer = 0

for student in A:
    if student > 0:
        answer += 1

    if student > B:
        q, r = divmod(student - B, C)
        answer += q
        if r > 0:
            answer += 1

print(answer)
