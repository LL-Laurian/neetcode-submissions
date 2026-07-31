class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        dp = [[0] * l for _ in range(l) ]

        dp[0][0] = triangle[0][0]

        # level
        for i in range(1, l):
            # index i
            for j in range (i+1):
                #same position
                p1 = dp[i-1][j] + triangle[i][j] if j != i else float("inf")

                p2 = dp[i-1][j-1] + triangle[i][j] if j >=1 else float("inf")
                dp[i][j]= min(p1, p2)

                #print(i, j, p1, p2, dp[i][j])

        
        return min(dp[l-1])
