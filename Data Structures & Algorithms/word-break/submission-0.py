class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means s[i:] can break into words in wordDict
        n = len(s)
        m = len(wordDict)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and dp[i + len(w)]:
                    if s[i:i+len(w)] == w:
                        dp[i] = True
                        break
        return dp[0]
            
