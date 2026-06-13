class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window with budget 
        # naive version is to check every unique char
        # optimal version that we track max_f up to r 
        # it is okay to have stale max_f because shrinking won't inrease answer beyond 
        # a window length that was already achievable when maxf was accurate
        # sol 1
        charSet = set(s)
        n = len(s)
        ans = 0

        for c in charSet:
            count = 0
            l = 0
            for r in range(n):
                if s[r] == c:
                    count += 1
                while r - l + 1 - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                ans = max(ans, r - l + 1)
        
        return ans 