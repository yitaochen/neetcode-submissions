class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def dfs(lp, rp):
            if lp == n and rp == n:
                ans.append("".join(stack))
                return 
            
            if lp < n:
                stack.append('(')
                dfs(lp+1, rp)
                stack.pop()

            if lp >= rp + 1:
                stack.append(')')
                dfs(lp, rp+1)
                stack.pop()
            
        dfs(0, 0)

        return ans 
            

            
            