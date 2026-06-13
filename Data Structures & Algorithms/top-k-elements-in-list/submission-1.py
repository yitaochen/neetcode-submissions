class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # something about heavy hitter
        # simplest solution would be just counter
        # O(n), O(n) solution bucket sort, using freq as index to group numbers 
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        
        n = len(nums)
        freqs = [[] for _ in range(n+1)]

        for key, val in cnt.items():
            freqs[val].append(key)
        
        ans = []

        while k > 0:
            for i in range(n, -1, -1):
                if freqs[i]:
                    if len(freqs[i]) <= k:
                        ans += freqs[i]
                        k -= len(freqs[i])
                    else:
                        ans += freqs[:k]
                        k = 0
        
        return ans 
        

