N = int(input())
R = []
G = []
B = []
Q = []
W = []
E = []
for i in range(N):
    a, b, c = map(int, input().split())
    R.append(a)
    G.append(b)
    B.append(c)
Q.append(R[0])
W.append(G[0])
E.append(B[0])
for i in range(1, N):
    if W[i - 1] < E[i - 1]:
        tmp = W[i - 1]
    else:
        tmp = E[i - 1]
    Q.append(R[i] + tmp)
    
    if Q[i - 1] < E[i - 1]:
        tmp = Q[i - 1]
    else:
        tmp = E[i - 1]
    W.append(G[i] + tmp)
    
    if Q[i - 1] < W[i - 1]:
        tmp = Q[i - 1]
    else:
        tmp = W[i - 1]
    E.append(B[i] + tmp)

min = Q[N - 1]
if W[N - 1] < min:
    min = W[N - 1]
if E[N - 1] < min:
    min = E[N - 1]
    
print(min)
    
