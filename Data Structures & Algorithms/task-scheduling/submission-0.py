class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        hq = [-v for v in cnt.values()]
        heapq.heapify(hq)

        t = 0
        q = deque()

        while hq or q:
            t += 1

            if not hq:
                t = q[0][1]
            else:
                v = 1 + heapq.heappop(hq)
                if v:
                    q.append([v, t + n])
        
            if q and q[0][1] == t:
                heapq.heappush(hq, q.popleft()[0])
        
        return t