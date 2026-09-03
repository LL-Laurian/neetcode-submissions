class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ress = [[]]

        for num in nums:
            new_ress =[]
            for res in ress:
                new = res.copy() if res is not None else []
                new.append(num)
                new_ress.append(new)
            
            ress.extend(new_ress)

        return ress
        

