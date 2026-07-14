class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0 
        if n == 0:
            return 1.0
        sign = n > 0
        if not sign:
            n *= -1
        if n == 1:
            tmp = x 
        elif n == 2:
            tmp = x * x
        else:
            tmp = self.myPow(x, n//2) * self.myPow(x, n - n//2)
        
        if not sign:
            return 1 / tmp
        else:
            return tmp