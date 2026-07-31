class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recurrence dp[i] = minimum cost so far to reach the ith floor. 
        #                  = in(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        l = len(cost)
        dp = [0] * (l+1)
        
        for i in range(2, l+1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[l]

            