class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from collections import deque

        # 1. arr 입력받기
        arr = [[0] * len(board[0]) for _ in range(len(board))]

        start = []

        # 2. word의 첫 글자가 있는 좌표 찾기
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    start.append((i, j))

        # 2-1 word의 첫 글자가 없으면 False
        if not start:
            return False

        # 3. dfs
        def dfs(x, y, idx):
            if idx == len(word):
                return True

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if arr[nx][ny] == 0 and board[nx][ny] == word[idx]:
                        arr[nx][ny] = 1
                        if dfs(nx, ny, idx + 1):
                            return True
                        arr[nx][ny] = 0

            return False

        # 4. dfs 호출
        for x, y in start:
            arr[x][y] = 1
            if dfs(x, y, 1):
                return True
            arr[x][y] = 0

        return False
