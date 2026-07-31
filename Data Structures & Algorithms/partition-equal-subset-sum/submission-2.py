class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total//2
        if total%2 !=0:
            return False

        dp = set()
        
        for num in nums:
            if num == half:
                return True
            currentdp = dp.copy()
            dp.add(num)
            for value in currentdp:
                new_sum = value + num
                if new_sum == half:
                    return True
                dp.add(value + num)
        
        return False
