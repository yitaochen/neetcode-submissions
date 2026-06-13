class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = nums
        heapq.heapify(self.hq)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        while len(self.hq) > self.k:
            heapq.heappop(self.hq)
        
        return self.hq[0]
