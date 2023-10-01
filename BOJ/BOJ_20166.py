N, M, K = map(int, input().split())

board = [list(input()) for _ in range(N)]
words = [input() for _ in range(K)]

answer = {}

for word in words:
    answer[word] = 0

ROW = len(board)
COL = len(board[0])
darr = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]

def dfs(x, y, word, idx):
    if idx == len(word):
        return 1
    cnt = 0
    for dx, dy in darr:
        nx, ny = (x + dx) % ROW, (y + dy) % COL
        if board[nx][ny] == word[idx]:
            cnt += dfs(nx, ny, word, idx + 1)
    return cnt

for i in range(N):
    for j in range(M):
        for word in words:
            if board[i][j] == word[0]:
                answer[word] += dfs(i, j, word, 1)

for word in words:
    print(answer[word])