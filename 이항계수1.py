N, K = map(int, input().split())
numerator = 1
denominator = 1
for i in range(K):
    numerator *= (N-i)
    denominator *= i + 1
print(int(numerator/denominator))
    
