class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        ROW = len(grid)
        COL = len(grid[0])
        for y in range(ROW):
            for x in range(COL):
                if grid[y][x] == 0:
                    continue
                for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ny, nx = y + dy, x + dx
                    if ny < 0 or ny >= ROW or nx < 0 or nx >= COL or grid[ny][nx] == 0:
                        answer += 1

        return answer
