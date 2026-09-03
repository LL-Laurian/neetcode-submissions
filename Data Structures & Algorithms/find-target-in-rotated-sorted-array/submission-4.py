class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        print(l, r, (l+r)//2)
        
        while l < r:
            mid = (l+r)//2
            if r-1 == l and nums[l] != target:
                return -1
            
            print(mid)

            if nums[mid] == target:
                return mid

            # mid > target and drop is on mid, r
            elif nums[mid] > target and nums[mid] > nums[l]:
                if nums[l] <= target:
                    r = mid
                else:
                    l = mid
            # mid > target and drop is on left, mid
            elif nums[mid] > target and nums[mid] < nums[l]:
                r = mid
            # mid < target and drop is on mid, r
            elif nums[mid] < target and nums[mid] > nums[l]:
                l = mid
            # mid > target and drop is on left, mid
            elif nums[mid] < target and nums[mid] < nums[l]:
                if nums[r-1] < target:
                    r = mid
                else:
                    l = mid
                
        return -1