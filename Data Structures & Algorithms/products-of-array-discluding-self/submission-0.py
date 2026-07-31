class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count0 = 0

        for num in nums:
            if num == 0:
                count0+=1
                continue
            product*=num
        
        if count0>=2:
            return [0] * len(nums)
        
        arr =[product] * len(nums)
        
        if count0 == 1:
            arr =[0] * len(nums)

        for i, num in enumerate(nums):
            if num == 0:
                arr[i] = product
            else:
                arr[i]= int(arr[i]/num)
        
        return arr