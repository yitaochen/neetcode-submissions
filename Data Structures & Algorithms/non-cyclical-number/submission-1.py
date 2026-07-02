class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp 
        
        return True 
            