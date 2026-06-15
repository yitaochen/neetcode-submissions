"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = {}
        # sweep line alg
        for i in intervals:
            mp[i.start] = mp.get(i.start, 0) + 1
            mp[i.end] = mp.get(i.end, 0) - 1
        
        cur = 0
        ans = 0
        for key in sorted(mp.keys()):
            cur += mp[key]
            ans = max(ans, cur)
        
        return ans 

            