class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)
        return len(newSet) != len(nums)
            
        