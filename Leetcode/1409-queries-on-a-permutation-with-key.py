from collections import deque
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        answer = []
        P = deque([i for i in range(1,m+1)])

        for query in queries:
            answer.append(P.index(query))
            P.remove(query)
            P.appendleft(query)
        
        return(answer)