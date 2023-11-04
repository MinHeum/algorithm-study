class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import copy

        N = len(board)
        M = len(board[0])

        # 1. 살아있는 이웃의 수를 센다.
        # 2. 살아있는 이웃이 0~1이거나, 4~8이면 죽는다.

        def count_live_neighbors(i, j):
            # 근처의 살아있는 이웃의 수를 return하는 함수
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x == i and y == j:
                        continue
                    if 0 <= x < N and 0 <= y < M:
                        if board[x][y] == 1 or board[x][y] == 3:
                            count += 1
            return count

        copied_board = copy.deepcopy(board)

        for i in range(N):
            for j in range(M):
                count = count_live_neighbors(i, j)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        copied_board[i][j] = 0
                else:
                    if count == 3:
                        copied_board[i][j] = 1

        for i in range(N):  # copied_board를 board에 복사
            for j in range(M):
                board[i][j] = copied_board[i][j]

        return None
