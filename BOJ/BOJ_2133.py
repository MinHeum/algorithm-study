from sys import stdin

# 3 * N 크기의 벽을 2 * 1, 1 * 2 크기의 타일로 채우는 경우의 수를 구하기


N = int(stdin.readline())


dp = []
dp.append(1)  # 0번째 인덱스는 1로 초기화

for i in range(1, N + 1):  # 1부터 N까지
    if i % 2 == 1:
        dp.append(0)  # N이 홀수이면 0을 추가
        continue

    dp.append(dp[i - 2] * 3)  # 2 * 1 타일로 채우는 경우의 수
    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2  # 1 * 2 타일로 채우는 경우의 수

print(dp[N])
