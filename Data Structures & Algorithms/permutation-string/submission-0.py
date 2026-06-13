class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for c in s1:
            cnt1[ord(c) - ord('a')] += 1
        for i in range(len(s1)):
            cnt2[ord(s2[i]) - ord('a')] += 1
        matches = sum(1 if cnt1[i] == cnt2[i] else 0 for i in range(26))
        l = 0 
        if matches == 26:
            return True 
        
        for r in range(len(s1), len(s2)):
            index = ord(s2[r]) - ord('a')
            cnt2[index] += 1
            if cnt1[index] == cnt2[index]:
                matches += 1
            elif cnt1[index] + 1 == cnt2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            l += 1
            cnt2[index] -= 1
            if cnt1[index] == cnt2[index]:
                matches += 1
            elif cnt1[index] - 1 == cnt2[index]:
                matches -= 1
            
            if matches == 26:
                return True 
        
        return False

