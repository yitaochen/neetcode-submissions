class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the min first 
        # then just do wrap around 
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m 
            else:
                l = m + 1
        
        k = r 

        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2
            nm = (m + k) % n 
            if nums[nm] > target:
                r = m - 1
            elif nums[nm] < target:
                l = m + 1
            else:
                return nm 
        
        return -1