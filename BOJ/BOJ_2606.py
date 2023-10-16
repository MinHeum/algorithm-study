from sys import stdin

N = int(stdin.readline())  # 컴퓨터의 수
pairs = int(stdin.readline())  # 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(N + 1)]
for _ in range(pairs):
    a, b = map(int, stdin.readline().split())
    # a와 b는 서로 연결되어있음
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N + 1)  # 방문 여부 배열 (1부터 시작)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:  # v와 연결된 노드들이 방문되지 않았다면 dfs 수행
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)

print(visited.count(True) - 1)
