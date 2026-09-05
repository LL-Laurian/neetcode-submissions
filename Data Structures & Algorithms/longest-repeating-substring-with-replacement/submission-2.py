class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        beg, end = 0, 0

        cur = {}
        acc = 0

        for end in range(len(s)):
            acc += 1
            if s[end] not in cur:
                cur[s[end]] = 1
            else:
                cur[s[end]] += 1
            most = max(cur.values())
            if acc - most <= k:
                ret = max(ret, end - beg + 1)
                end += 1
            else:
                while beg <= end and acc - most > k:
                    cur[s[beg]] -= 1
                    beg += 1
                    acc -= 1
            print(beg, end)

        return ret