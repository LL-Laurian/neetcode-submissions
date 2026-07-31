class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m ={}

        for i, num in enumerate(numbers):
            
            if num in m:
                return [m[num], i+1]
            else:
                remain = target - num
                m[remain] = i+1

        