class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        heapq.heapify(hq)
        for stone in stones:
            heapq.heappush(hq, -stone)
        
        while len(hq) > 1:
            x = -heapq.heappop(hq)
            y = -heapq.heappop(hq)
            if x != y:
                heapq.heappush(hq, -abs(x-y))
            
        return -hq[0] if hq else 0