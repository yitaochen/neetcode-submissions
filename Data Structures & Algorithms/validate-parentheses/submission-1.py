class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if stack and left[stack[-1]] == c:
                    stack.pop()
                else:
                    return False 
        
        if not stack:
            return True 
        else:
            return False 