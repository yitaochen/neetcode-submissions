class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            key = tuple(cnt)
            if key in mp:
                mp[key].append(s)
            else:
                mp[key] = [s]
        
        return [v for k, v in mp.items()]
