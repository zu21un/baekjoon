import sys

N = int(input())
users = []
for i in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    users.append((int(age),name,i))
users.sort(key=lambda x:(x[0],x[2]))
for user in users:
    print(user[0], user[1])

