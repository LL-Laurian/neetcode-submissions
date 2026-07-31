class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=0
        i=0
        chars = []

        def checkNonalpha(c):
            return not (
            ('A' <= c <= 'Z') or
            ('a' <= c <= 'z') or
            ('0' <= c <= '9')
        )
        
        for char in s:
            if not checkNonalpha(char):
                chars.append(char)

        l = len(chars)

        while i < l//2 and j<l//2:
            if chars[i].lower() != chars[l-j-1].lower():
                return False
            j+=1
            i+=1
        return True
