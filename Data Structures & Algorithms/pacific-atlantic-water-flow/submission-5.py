class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i, j, ocean):
            ocean.add((i, j))

            for ni, nj in neighbors(i, j):
                if (
                    (ni, nj) not in ocean
                    and heights[ni][nj] >= heights[i][j]
                ):
                    dfs(ni, nj, ocean)

        def neighbors(i, j):
            nei = []

            if i > 0:
                nei.append((i - 1, j))
            if i < rows - 1:
                nei.append((i + 1, j))
            if j > 0:
                nei.append((i, j - 1))
            if j < cols - 1:
                nei.append((i, j + 1))

            return nei

        # Pacific: top + left
        for i in range(rows):
            dfs(i, 0, pacific)

        for j in range(cols):
            dfs(0, j, pacific)

        # Atlantic: bottom + right
        for i in range(rows):
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            dfs(rows - 1, j, atlantic)

        res = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res
            


            
            
