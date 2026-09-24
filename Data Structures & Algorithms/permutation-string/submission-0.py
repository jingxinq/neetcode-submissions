class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char,0)+1

        s2_map = {}
        for char in s2[:len(s1)]:
            s2_map[char] = s2_map.get(char, 0) + 1
        if s1_map == s2_map:
            return True

        L = 0
        for R in range(len(s1),len(s2)):
                s2_map[s2[R]] = s2_map.get(s2[R],0)+1
                s2_map[s2[L]] -= 1

                if s2_map[s2[L]] == 0:
                    del s2_map[s2[L]]

                if s1_map == s2_map:
                    return True
                else: 
                    L += 1
        return False



            
            

        