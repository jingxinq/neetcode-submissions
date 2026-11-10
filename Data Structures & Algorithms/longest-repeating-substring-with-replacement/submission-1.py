class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        max_freq = {}
        for r in range(len(s)):
            max_freq[s[r]] = max_freq.get(s[r], 0) + 1
            while (r-l+1) - max(max_freq.values())>k:
                max_freq[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
        