N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

num_dict = {}

for num in A:
    num_dict[num] = True

for num in B:
    if num in num_dict:
        print(1)
    else:
        print(0)
    
    




