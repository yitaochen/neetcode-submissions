class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix max left, max right
        # can be optimized to two pointers
        n = len(height)
        l, r = 0, n - 1
        lmax = height[l]
        rmax = height[r]

        ans = 0
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                ans += rmax - height[r]
        
        return ans 