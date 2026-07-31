class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [None] * l
        
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, l):
            cur = dp[i-1] + nums[i]
            if cur > nums[i]:
                dp[i] = cur
            else: dp[i] = nums[i]
            
            max_sum = max(max_sum, dp[i])
        
        return max_sum
        