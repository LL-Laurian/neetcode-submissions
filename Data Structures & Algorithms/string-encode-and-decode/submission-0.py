class Solution:

    def encode(self, strs: List[str]) -> str:
        s =""
        for string in strs:
            s+=string
            s+='逗'
        
        return s

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        cur =""
        l = []
        for ch in s:
            if ch != '逗':
                cur+=ch
            
            else:
                l.append(cur)
                cur=""
        
        return l