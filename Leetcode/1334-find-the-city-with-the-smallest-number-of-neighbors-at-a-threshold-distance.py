class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 플로이드 워셜 알고리즘 사용

        # 1. 그래프 초기화
        graph = [[float('inf')] * n for _ in range(n)]

        # 2. 자기 자신으로 가는 비용은 0으로 초기화
        for i in range(n):
            graph[i][i] = 0

        # 3. 간선 정보를 그래프에 입력
        for edge in edges:
            a, b, cost = edge
            graph[a][b] = cost
            graph[b][a] = cost

        # 4. 플로이드 워셜 알고리즘 수행
        for k in range(n):
            for a in range(n):
                for b in range(n):
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

        # 5. 각 도시별로 연결된 도시의 수를 계산
        counts = [0] * n
        for i in range(n):
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    counts[i] += 1

        # 6. 연결된 도시의 수가 가장 작은 도시를 찾음
        min_count = min(counts)
        for i in range(n - 1, -1, -1):
            if counts[i] == min_count:
                return i
            
        return -1
    