class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        beg = 0
        cur = defaultdict(int)


        for end in range(len(s)):
            cur[s[end]] += 1
            while beg <= end and sum(cur.values()) - max(cur.values()) > k:
                cur[s[beg]] -= 1
                beg += 1
            ret = max(ret, end - beg + 1)
            end += 1

        return ret