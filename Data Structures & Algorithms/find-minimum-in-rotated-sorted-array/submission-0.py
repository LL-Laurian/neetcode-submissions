class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        curr_min = min(nums[l], nums[r-1])

        while l < r:
            mid = (l+r) //2
            curr_min = min(nums[l], nums[r-1], nums[mid], curr_min)

            print("l", l, "r", r, "mid", mid, "curr_min", curr_min)

            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        
        print("curr_min111", curr_min)
        return curr_min