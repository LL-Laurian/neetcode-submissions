class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def dfs(idx, cur):
            if idx > n:
                return
            res.append(cur.copy())

            for i in range(idx, n):
                if i>idx and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                dfs(i+1,cur)
                cur.pop()
                
                

        dfs(0, [])
        return res