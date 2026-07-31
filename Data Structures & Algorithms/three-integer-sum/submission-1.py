class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        m = defaultdict(list)
        res = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                remain = -1 * (nums[i] + nums[j])
                m[remain].append(((i, j), nums[i], nums[j]))

        for index, num in enumerate(nums):
            if num in m:
                for tup in m[num]:
                    if index not in tup[0]:
                        triplet = tuple(sorted(tup[1:] + (num,)))
                        if triplet not in seen:
                            seen.add(triplet)
                            res.append(triplet)
        

        return(res)


        