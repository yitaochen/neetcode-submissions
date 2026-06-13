class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search problem 
        r = max(piles)
        l = 1

        def eat(k):
            t = 0
            for p in piles:
                t += p // k + 1 if p % k else p // k
            return t
        
        while l < r:
            mid = l + (r - l) // 2
            if eat(mid) > h:
                l = mid + 1
            else:
                r = mid 
        
        return r
