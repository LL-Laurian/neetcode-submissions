class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        sort_s1 = Counter(s1)
        l2 = len(s2)

        for i in range(l2-l1+1):
            if s2[i] not in sort_s1:
                continue
            elif (sort_s1 == Counter(s2[i:i+l1])):
                return True

        return False

