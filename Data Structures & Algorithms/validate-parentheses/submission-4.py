class Solution:
    def isValid(self, s: str) -> bool:
        pmap = { 
            '(': ')',
            ')':'(',
            '{':'}',
            '}':'{',
            '[': ']',
            ']': '['}
        
        l = len(s)
        stack =[]
        for i in range(l):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if stack == [] or pmap[stack.pop()] != s[i]:
                    return False
        
        
        return stack ==[]

