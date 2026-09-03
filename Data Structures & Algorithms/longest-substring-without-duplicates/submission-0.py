class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        prev_len = 0

        for i, char in enumerate(s):
            if char not in seen:
                prev_len +=1
                seen[char] = i
            
            else:
                prev_char_i = seen[char]
                if prev_len >= i - prev_char_i:
                    prev_len = i - prev_char_i
                else:
                    prev_len = prev_len + 1
                
                seen[char] =i

            max_len = max(max_len, prev_len)
        
        return max_len
        

                