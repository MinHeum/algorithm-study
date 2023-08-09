class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n개의 노드가 있고 n개의 edge 가 있다면, 항상 사이클을 형성한다.
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        print(parent)
        print(rank)

        # find 함수 구현
        def find(n):
            p = parent[n]
            
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        # union 함수 구현
        def union(e1, e2):
            p1, p2 = find(e1), find(e2)

            # 이미 같은 부모를 가질 때에, False 를 반환
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
