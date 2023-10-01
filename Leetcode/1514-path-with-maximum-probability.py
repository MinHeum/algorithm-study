import heapq


class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        INF = 1e9

        # n개의 노드, edges는 노드간의 연결 정보, succProb는 각 edge의 확률
        # start_node에서 end_node로 가는데 성공할 확률의 최대값을 구하라
        # 다익스트라 알고리즘을 사용하면 된다.

        # 1. 그래프 초기화
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # 2. 다익스트라 알고리즘
        # 2-1. dist 배열 초기화
        dist = [0] * n
        dist[start_node] = 1
        # 2-2. 우선순위 큐 초기화
        pq = []
        
        # 2-3. 시작 노드를 큐에 넣는다.
        heapq.heappush(pq, (-1, start_node))

        # 2-4. 큐가 빌 때까지 반복한다.
        while pq:
            # 2-5. 큐에서 노드를 하나 꺼낸다.
            prob, node = heapq.heappop(pq)

            # 2-6. 노드의 인접 노드를 확인한다.
            for adj_node, adj_prob in graph[node]:
                # 2-7. 인접 노드의 dist를 업데이트한다.
                if dist[adj_node] < dist[node] * adj_prob:
                    dist[adj_node] = dist[node] * adj_prob
                    heapq.heappush(pq, (-dist[adj_node], adj_node))

        return dist[end_node]
    
    