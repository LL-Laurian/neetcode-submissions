class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        min_num = min(nums)
        res = []
        for i, num in enumerate(nums):

            if num == target:
                res.append([num])
            
            if target - num >= min_num:
                subsets = self.combinationSum(nums[i:], target-num)
                for subset in subsets:
                    subset.append(num)
                    res.append(subset)
                
        return res