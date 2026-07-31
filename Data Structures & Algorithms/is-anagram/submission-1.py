from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = dict(sorted(Counter(s).items()))
        tc = dict(sorted(Counter(t).items()))
        return sc == tc


        