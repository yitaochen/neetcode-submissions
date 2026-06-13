class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # memorize the last appearance of each char 
        mp = {}
        n = len(s)
        l = 0
        ans = 0
        for r in range(n):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            ans = max(ans, r - l + 1)
        
        return ans 