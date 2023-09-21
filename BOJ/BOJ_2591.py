from sys import stdin

s = stdin.readline().rstrip()

dp = [0] * (len(s) + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, len(s) + 1):
    # 0이 아니면 1자리 수로 만들 수 있음
    if s[i - 1] != "0":
        dp[i] += dp[i - 1]
    # 10 ~ 34이면 2자리 수로 만들 수 있음
    if 10 <= int(s[i - 2:i]) <= 34:
        dp[i] += dp[i - 2]

print(dp[len(s)])
