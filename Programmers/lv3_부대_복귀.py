def solution(n, roads, sources, destination):
    from collections import deque
    answer = []
    graph = dict()

    for i in range(1, n + 1):
        graph[i] = []

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n+1)

    q = deque()
    q.append([destination, 0])

    visited = [False] * (n + 1)

    while q:
        node, dist = q.popleft()

        if visited[node]:
            continue

        visited[node] = True
        distance[node] = dist

        for next_node in graph[node]:
            if not visited[next_node]:
                q.append([next_node, dist + 1])

    for source in sources:
        answer.append(distance[source])

    return answer
  
