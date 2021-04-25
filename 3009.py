X = []
Y = []
for i in range(3):
    A, B = map(int, input().split())
    if A in X:
        X.remove(A)
    else if A not in X:
        X.append(A)
    
    if B in Y:
        Y.remove(B)
    else if B not in Y:
        Y.append(B)
print(X[0], Y[0])