from sys import stdin

N = int(stdin.readline().rstrip())
arr = [0] * (N + 1)
dp = [[0] * (N + 1) for _ in range(3)]

for i in range(1, N + 1):
    arr[i] = int(stdin.readline().rstrip())

for i in range(1, N + 1):
    dp[0][i] = max(dp[0][i - 1], max(dp[1][i - 1], dp[2][i - 1]))
    dp[1][i] = dp[0][i - 1] + arr[i]
    dp[2][i] = dp[1][i - 1] + arr[i]

answer = max(dp[0][N], max(dp[1][N], dp[2][N]))
print(answer)
