from sys import stdin
N, M =  map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[[1e9 for _ in range(3)] for _ in range(M)] for _ in range(N)]

for i in range(M):
    dp[0][i][0] = arr[0][i]
    dp[0][i][1] = arr[0][i]
    dp[0][i][2] = arr[0][i]

# i는 행
for i in range(1, N):
    # j는 열
    for j in range(M):
        # k가 0이면 전 단계에서 왼쪽에서 온 것, 1이면 전 단계에서 위에서 온 것, 2이면 전 단계에서 오른쪽에서 온 것
        for k in range(3):
          if j == 0 and k == 0:
              continue
          elif j == M-1 and k == 2:
              continue
          
          if k == 0:
              dp[i][j][k] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + arr[i][j]
          elif k == 1:
              dp[i][j][k] = min(dp[i-1][j][0], dp[i-1][j][2]) + arr[i][j]
          elif k == 2:
              dp[i][j][k] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + arr[i][j]

answer = 1e9

for i in range(M):
    for j in range(3):
        if i == 0 and j == 0:
            continue
        elif i == M-1 and j == 2:
            continue
        answer = min(answer, dp[N-1][i][j])

print(answer)