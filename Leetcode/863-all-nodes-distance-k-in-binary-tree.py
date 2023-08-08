class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 트리의 역방향으로도 갈 수 있게 하는 TreeNode를 새로 만드는 함수
        def set_parent(cur, parent):
            if cur:
                cur.parent = parent
                set_parent(cur.left, cur)
                set_parent(cur.right, cur)
        
        set_parent(root, None)

        answer = []
        visit = set()

        def dfs(cur, distance):
            if cur is None or cur in visit:
                return
            
            visit.add(cur)
            if distance == k:
                answer.append(cur.val)
                return
            dfs(cur.parent, distance + 1)
            dfs(cur.left, distance + 1)
            dfs(cur.right, distance + 1)
        dfs(target, 0)

        return answer