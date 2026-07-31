class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count=0
        rows= len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r <0 or r >= rows or c <0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] =0

            right = dfs(r+1,c)
            left = dfs(r-1,c)
            up = dfs(r, c-1)
            down= dfs(r, c+1)

            return right + left + up + down + 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_count = max(max_count, dfs(r,c))
        
        return max_count