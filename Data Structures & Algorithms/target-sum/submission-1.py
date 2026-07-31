class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # 2d version [i] = [The reachable sum]

        l = len(nums)
        total = 0

        if l == 0:
            return 0
        
        if l == 1:
            count = 0
            if target == nums[0]:
                count +=1
            if target == -1 * nums[0]:
                count +=1 
            return count   

        dp = [[] for _ in range(l)]
        dp[0] = [nums[0], -1 * nums[0]]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            
            for s in dp[i-1]:
                plus = s+num
                minus = s-num
                dp[i].append(plus)
                dp[i].append(minus)

                if i == l-1:
                    if plus == target:
                        total +=1
                    if minus == target:
                        total +=1

        return total
