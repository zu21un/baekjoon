def factorial(num:int)->int:
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

N = int(input())
print(factorial(N))