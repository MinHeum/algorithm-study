class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # 이 문제도 Union - Find 를 사용하면 풀 수 있을 것 같습니다!
        parent = [i for i in range(26)]
        def find(e):
            p = parent[ord(e) - ord('a')]
            
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(e1, e2):
            p1, p2 = find(e1), find(e2)

            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        answer = ''

        for i in range(len(baseStr)):
            answer += chr(find(baseStr[i]) + ord('a'))

        return answer
