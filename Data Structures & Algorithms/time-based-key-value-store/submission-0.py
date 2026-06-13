class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        pairs = self.keys.get(key, [])
        l, r = 0, len(pairs) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if pairs[mid][1] <= timestamp:
                ans = pairs[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans 
        

        
