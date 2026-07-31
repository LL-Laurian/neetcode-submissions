class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        sort_s1 = sorted(s1)
        l2 = len(s2)

        for i in range(l2-l1+1):
            
            if (sort_s1 == sorted(s2[i:i+l1])):
                return True

        return False

