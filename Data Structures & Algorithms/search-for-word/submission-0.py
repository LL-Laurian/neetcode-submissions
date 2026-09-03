class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        used = [[False] * cols for _ in range(rows)]

        def dfs(i, j, s_index):
            if board[i][j] != word[s_index]:
                return False

            if s_index == len(word) - 1:
                return True

            used[i][j] = True

            # right
            if j < cols - 1 and not used[i][j + 1]:
                if dfs(i, j + 1, s_index + 1):
                    used[i][j] = False
                    return True

            # left
            if j > 0 and not used[i][j - 1]:
                if dfs(i, j - 1, s_index + 1):
                    used[i][j] = False
                    return True

            # down
            if i < rows - 1 and not used[i + 1][j]:
                if dfs(i + 1, j, s_index + 1):
                    used[i][j] = False
                    return True

            # up
            if i > 0 and not used[i - 1][j]:
                if dfs(i - 1, j, s_index + 1):
                    used[i][j] = False
                    return True

            used[i][j] = False
            return False


        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False    
