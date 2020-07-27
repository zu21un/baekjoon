string = input()
len = len(string)
cnt = string.count(' ')
if (string[0]==' ') and (string[len - 1]==' '):
    cnt -= 1
elif (string[0]!=' ') and (string[len - 1]!=' '):
    cnt += 1
print(cnt)