class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # different than trapping rain water
        # two pointers 
        # move the lower pointer, move only if it becomes higher
        n = len(heights)
        l, r = 0, n - 1
        lmax = heights[l]
        rmax = heights[r]
        ans = min(lmax, rmax) * (r - l)
        while l < r:
            if lmax < rmax:
                l += 1
                if heights[l] <= lmax:
                    continue 
                else:
                    lmax = heights[l]
                    ans = max(ans, min(lmax, rmax) * (r - l))
            else:
                r -= 1
                if heights[r] <= rmax:
                    continue
                else:
                    rmax = heights[r]
                    ans = max(ans, min(lmax, rmax) * (r - l))
        
        return ans 
