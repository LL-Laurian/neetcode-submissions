class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_str = ''
        n = len(s)
        dp = [[False] * n for _ in range(n)]


        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):  
                    dp[i][j] = True
                    curr_len = j-i + 1
                    if curr_len > max_len:
                        max_len = curr_len
                        max_str = s[i:j+1]
        
        return max_str


