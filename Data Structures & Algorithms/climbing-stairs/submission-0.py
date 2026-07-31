class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [1] * (n+1)

        for i in range(1, n+1):
            dp[i] = dp[i-1]+dp[i-2] if i>=2 else dp[i-1]

        return dp[n]