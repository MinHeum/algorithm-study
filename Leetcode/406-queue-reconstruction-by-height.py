class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 높이의 역순으로 정렬하고, 같은 높이면 k의 오름차순으로 정렬
        people.sort(key=lambda x: (-x[0],x[1]))
        ans = []
        for p in people:
            # k는 자신보다 크거나 같은 사람의 수
            ans.insert(p[1], p)
        return ans