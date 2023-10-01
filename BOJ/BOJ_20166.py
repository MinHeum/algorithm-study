from sys import stdin, setrecursionlimit

# 재귀 깊이 설정
setrecursionlimit(10 ** 9)

n, m, k = map(int, stdin.readline().split())
answer_dict = {}
words = []
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy =  [0, 1, 0, -1, -1, 1, 1, -1]
ans_list = []

for _ in range(n):
    words.append(list(stdin.readline().rstrip()))

for _ in range(k):
    data = stdin.readline().rstrip()
    answer_dict[data] = 0
    ans_list.append(data)


def dfs(x, y, cnt, word):
    if cnt > 5:
        return

    if word in answer_dict:
        answer_dict[word] += 1

    for i in range(8):
        nx, ny = (x + n + dx[i]) % n, (y + m + dy[i]) % m
        dfs(nx, ny, cnt + 1, word + words[nx][ny])


for i in range(n):
    for j in range(m):
        start = ''
        dfs(i, j, 1, start + words[i][j])

for k in ans_list:
    if k in answer_dict:
        print(answer_dict[k])
