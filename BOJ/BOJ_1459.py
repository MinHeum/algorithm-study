from sys import stdin


# X, Y, W(가로), S(대각선)
X, Y, W, S = map(int, stdin.readline().rstrip().split())

# 가로 세로만 이동하는 경우
answer1 = (X + Y) * W

# 대각선으로만 이동하는 경우
if (X + Y) % 2 == 0:
    answer2 = max(X, Y) * S
else:
    answer2 = (max(X, Y) - 1) * S + W

# 대각선으로 이동하다가 가로 세로로 이동하는 경우
answer3 = min(X, Y) * S + (max(X, Y) - min(X, Y)) * W

print(min(answer1, answer2, answer3))
