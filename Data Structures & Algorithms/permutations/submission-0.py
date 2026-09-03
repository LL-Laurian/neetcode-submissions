class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(prefix):
            if len(prefix) == len(nums):
                res.append(prefix.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    prefix.append(nums[i])
                    used[i] = True

                    dfs(prefix)

                    prefix.pop()
                    used[i] = False

        dfs([])
        return res      
