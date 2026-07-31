class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 + l2 != len(s3):
            return False

        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i > 0:
                    dp[i][j] = dp[i][j] or (
                        dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    )

                if j > 0:
                    dp[i][j] = dp[i][j] or (
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                    )

        return dp[l1][l2]