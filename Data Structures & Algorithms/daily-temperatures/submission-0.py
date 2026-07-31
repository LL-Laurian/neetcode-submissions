class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack != [] and stack[-1][1] < temp:
                item_index = stack.pop()[0]
                result[item_index] = i - item_index
            
            stack.append((i, temp))
        
        return result