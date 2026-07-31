class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=0
        i=0
        new_string =""

        def checkNonalpha(c):
            return not (
            ('A' <= c <= 'Z') or
            ('a' <= c <= 'z') or
            ('0' <= c <= '9')
        )
        
        for char in s:
            if not checkNonalpha(char):
                new_string+=char

        l = len(new_string)

        while i < l//2 and j<l//2:
            if new_string[i].lower() != new_string[l-j-1].lower():
                return False
            j+=1
            i+=1
        return True
