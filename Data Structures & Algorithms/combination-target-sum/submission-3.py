class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        min_num = min(nums)

        def dfs(index, target):
            result =[]
            for i in range(index, len(nums)):
                num = nums[i]
                if num == target:
                    result.append([num])
                
                if target - num >= min_num:
                    subsets = dfs(i, target-num)
                    for subset in subsets:
                        subset.append(num)
                        result.append(subset)

            return result

     
        return dfs(0, target) 