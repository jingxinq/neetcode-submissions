class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        r = l
        while l < len(s):
            while s[r] != "#":
                r += 1
            str_len = int(s[l:r])
            str_temp = s[r+1:r+1+str_len]
            res.append(str_temp)
            l = r+1+str_len
            r = l

        return res