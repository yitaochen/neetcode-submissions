class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # obvious sliding window 
        if not t:
            return ""
        cnt = Counter(t)
        win = {}
        have, need = 0, len(cnt)
        l = 0
        n = len(s)
        ansPos = [-1, -1]
        ansLen = float("inf")
        for r in range(n):
            c = s[r]
            win[c] = win.get(c, 0) + 1
            if win[c] < cnt[c]:
                continue 
            elif win[c] == cnt[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < ansLen:
                    ansLen = r - l + 1
                    ansPos = [l, r]
                c = s[l]
                win[c] -= 1
                if win[c] < cnt[c]:
                    have -= 1
                l += 1
        
        l, r = ansPos
        return s[l:r+1] if ansLen < float("inf") else ""


