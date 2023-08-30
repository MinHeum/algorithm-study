class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 재귀를 이용한 dfs
        answer = []
        def dfs(left, right, s):
            if len(s) == n*2:
                answer.append(s)
                return
            
            if left < n:
                dfs(left + 1, right, s + '(')
            if right < left:
                dfs(left, right + 1, s + ')')
            
        dfs(0,0,'')
        return answer