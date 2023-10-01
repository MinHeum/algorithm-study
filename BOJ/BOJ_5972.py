from sys import stdin
import heapq

INF = int(1e9)

N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    A, B, C = map(int, stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            cost = dist + next_dist

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(1)
print(distance[N])