class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # dp[i][j] = True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # Build palindrome table
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

        res = []
        path = []

        def dfs(start):
            if start == n:
                res.append(path.copy())
                return

            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])

                    dfs(end + 1)

                    path.pop()

        dfs(0)

        return res