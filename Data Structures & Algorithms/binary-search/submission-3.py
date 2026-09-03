class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(start: int, end:int):
            if start<0 or end> len(nums):
                return -1
            if end-start == 1:
                if nums[start] == target:
                    return start
                else:
                    return -1
            
            mid = math.floor((end+start)/2)
            print(mid)
            if mid<0 or mid>= len(nums):
                return -1

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(start, mid)
            else:
                return binarySearch(mid+1, end)
        
        return binarySearch(0, len(nums))

        