class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = []
        for i in range(len(nums)):
            if nums[i] in remaining:
                arr = []
                arr.append(remaining.index(nums[i]))
                arr.append(i)
                return arr
            remaining.append(target - nums[i])
                
        