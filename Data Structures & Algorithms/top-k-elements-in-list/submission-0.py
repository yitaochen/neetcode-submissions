class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # something about heavy hitter
        # simplest solution would be just counter
        cnt = Counter(nums)
        return [k for k, v in cnt.most_common(k)]