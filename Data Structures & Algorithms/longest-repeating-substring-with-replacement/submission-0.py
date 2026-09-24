class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        max_freq = 0
        L, R = 0, 0
        #perform k replacements 0 <= k <= s.length
        #return length of longest substring

        for R in range(len(s)):
            count[s[R]] = count.get(s[R],0)+1
            max_freq = max(max_freq, count[s[R]])

            while (R-L+1-max_freq > k):
                count[s[L]] -= 1
                L += 1

            res = max(res, R-L+1)

        return res

            

            
            
            
