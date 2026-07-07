class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            tmp = 0
            for j in range(32):
                if (1 << j) & i:
                    tmp += 1
            ans.append(tmp)
        
        return ans 