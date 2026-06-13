class Solution:
    # length prefix
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = []
        for s in strs:
            ans.append(str(len(s)))
            ans.append('#')
            ans.append(s)
        
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        ans = []
        n = len(s)
        i = 0
        while i < n:
            j = i 
            l = ""
            while s[j] != '#':
                l += s[j]
                j += 1
            ans.append(s[j+1:j+1+int(l)])
            i = j+1+int(l)
        
        return ans 