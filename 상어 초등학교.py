import sys

input = sys.stdin.readline

N = int(input())

students = {}

classroom = [[0 for _ in range(N)] for _ in range(N)]


def find(student, classroom):
    num, stu_likes = student[0], student[1:]
    tmp = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(N):
        for y in range(N):
            if classroom[x][y] != 0:
                continue
            likes = 0
            empty = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if classroom[nx][ny] in stu_likes:
                    likes += 1
                elif classroom[nx][ny] == 0:
                    empty += 1
            tmp.append((likes, empty, x, y))

    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    result = (tmp[0][2], tmp[0][3])
    return result


for _ in range(N**2):
    student = list(map(int, input().split()))
    r, c = find(student, classroom)
    classroom[r][c] = student[0]
    students[student[0]] = student[1:]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        num = classroom[x][y]
        stu_likes = students[num]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if classroom[nx][ny] in stu_likes:
                cnt += 1
        if cnt != 0:
            answer += 10 ** (cnt - 1)
print(answer)
