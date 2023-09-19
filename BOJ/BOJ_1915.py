n, m = map(int, input().split())

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j, v in enumerate(input()):
        dp[i+1][j+1] = int(v)

ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i][j]:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans ** 2)
