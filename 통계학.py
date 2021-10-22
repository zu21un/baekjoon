from collections import Counter

N = int(input())
nums = []
freq = {}
for _ in range(N):
    num = int(input())
    nums.append(num)
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
nums.sort()
print(round(sum(nums) / N))
print(nums[int(N/2)])
max_freq = max(freq.values())
max_nums = []
for k, v in freq.items():
    if v == max_freq:
        max_nums.append(k)
if len(max_nums) > 1:
    max_nums.sort()
    print(max_nums[1])
else:
    print(max_nums[0])
print(nums[-1] - nums[0])


# commons = counter.most_common(1)

# for k, v in counter.items():
#     if k != commons[0][0] and v == commons[0][1]:
#         commons.append((k, v))
# if len(commons) > 1:
#     commons.sort(key = lambda x: x[0])
#     print(commons[1][0])
# else:
#     print(commons[0][0])

