class Solution:
    def canJump(self, nums: List[int]) -> bool:

        m = [-1] * len(nums)
        
        def reachable(index):
            if m[index] != -1:
                return True if m[index]==1 else False

            if index == 0:
                m[index]=1
                return True

            for i in range(index-1, -1, -1):
                if nums[i] >= index - i:
                    if reachable(i):
                        m[i] =1
                        return True
            m[i] = 0
            return False
        
        return reachable(len(nums)-1)