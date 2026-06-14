class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP can get to O(n^2) 
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        index = 0
        l = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if l < j - i + 1:
                        index = i
                        l = j - i + 1
        
        return s[index:index+l]
