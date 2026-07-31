from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one, two = Counter(s), Counter(t)
        for key in one:
            if key not in two or two[key] != one[key]:
                return False
        for key in two:
            if key not in one or two[key] != one[key]:
                return False
        return True


        