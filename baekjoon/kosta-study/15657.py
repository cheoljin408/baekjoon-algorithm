import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
c_nums = itertools.combinations_with_replacement(nums, M)
for i in c_nums:
    for j in range(M):
        print(i[j], end=' ')
    print()