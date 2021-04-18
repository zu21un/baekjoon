A = int(input())
B = int(input())
C = A * (B % 10) #3
D = A * ((B // 10) % 10) #4
E = A * (B // 100) #5
F = A * B #6

print(C, D, E, F, sep = '\n') 