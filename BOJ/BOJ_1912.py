from sys import stdin

n = int(stdin.readline().rstrip())

nums = list(map(int, stdin.readline().rstrip().split()))

dp = []
dp.append(nums[0])
for i in range(1, n):
    dp.append(max(dp[i-1] + nums[i], nums[i]))
    
print(max(dp))
