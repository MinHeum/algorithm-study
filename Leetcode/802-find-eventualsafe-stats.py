from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        rev = [ [] for _ in range(length) ]
        indegrees = [0] * length
        queue = deque()

        for i in range(length):
            edges = graph[i]
            for edge in edges:
                rev[edge].append(i)
                indegrees[i] += 1
            if not edges:
                queue.append(i)
        answer = []

        while queue:
            cur = queue.popleft()
            answer.append(cur)
            for nxt in rev[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    queue.append(nxt)

        return sorted(answer)