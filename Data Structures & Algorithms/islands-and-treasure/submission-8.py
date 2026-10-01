class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        # Get valid neighbors
        def neighbors(i, j):
            res = []

            if i > 0:
                res.append((i - 1, j))
            if i < rows - 1:
                res.append((i + 1, j))
            if j > 0:
                res.append((i, j - 1))
            if j < cols - 1:
                res.append((i, j + 1))

            return res

        while queue:
            cur_i, cur_j = queue.popleft()

            for nei_i, nei_j in neighbors(cur_i, cur_j):

                if grid[nei_i][nei_j] == 2147483647:
                    grid[nei_i][nei_j] = grid[cur_i][cur_j] + 1
                    queue.append((nei_i, nei_j))