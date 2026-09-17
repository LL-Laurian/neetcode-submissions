class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        cur = []

        m = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }


        def dfs(index):
            if index == len(digits):
                if index == 0:
                    return []
                    
                res.append("".join(cur))
                return
            
            for d in m[digits[index]]:
                cur.append(d)
                dfs(index+1)
                cur.pop()

        dfs(0)
        return res