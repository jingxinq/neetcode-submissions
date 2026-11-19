class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        alphabet_map = [0] * 26

        for c in s1:
            idx = ord(c) - ord('a')
            alphabet_map[idx] += 1

        k = len(s1)
        l = 0
        temp_map = [0] * 26
        for r in range(k-1, len(s2)):
            if r == k-1:
                for j in range(k):
                    idx = ord(s2[j]) - ord('a')
                    temp_map[idx] += 1
            else:
                temp_map[ord(s2[l-1]) - ord('a')] -= 1
                temp_map[ord(s2[r]) - ord('a')] += 1
            if temp_map == alphabet_map:
                return True
            l += 1
            
        return False

        
        