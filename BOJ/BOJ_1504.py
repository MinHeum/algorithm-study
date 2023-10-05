from sys import stdin
from collections import deque


INF = float("inf")
N, E = map(int, stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, stdin.readline().split())


def dijkstra(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    queue = deque([(start, 0)])

    while queue:
        node, cost = queue.popleft()

        if dist[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            if dist[next_node] > dist[node] + next_cost:
                dist[next_node] = dist[node] + next_cost
                queue.append((next_node, dist[next_node]))

    return dist[end]


answer = min(
    dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),
    dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N),
)

print(answer if answer < INF else -1)
