class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recurrence dp[i] = minimum cost so far to reach the ith floor. 
        #                  = min(dp[i-1] + cost[i], dp[i-2] + cost[i])    

        l = len(cost) + 2
        dp = [0] * l
        
        for i in range(2, l):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 2]

        return min(dp[-1], dp[-2])
            