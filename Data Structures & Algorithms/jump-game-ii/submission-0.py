class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0  

        goal = len(nums)-1
        count = 0
        index = 0

        while goal != 0 and index <= len(nums)-1:
            # print(goal, index)
            if index +nums[index] >= goal:
                goal = index
                count+=1
                index = 0
            else:
                index +=1
        
        return count