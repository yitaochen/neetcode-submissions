class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # once sort, each loop falls back to sorted 2sum
        # thus O(n^2) in time O(1) in space excluding output mem
        # need to skip duplicates 
        nums.sort()
        n = len(nums)
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                continue 
            if i > 0 and nums[i-1] == num:
                continue 
            j, k = i + 1, n - 1
            while j < k:
                tmp = num + nums[j] + nums[k]
                if tmp > 0:
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    ans.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        
        return ans 