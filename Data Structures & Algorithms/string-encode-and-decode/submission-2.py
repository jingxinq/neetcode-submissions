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
        i = 0
        j = i
        while i < len(s):
            while s[j] != "#":
                j += 1
            s_len = int(s[i:j])
            s_temp = s[j+1:j+1+s_len]
            res.append(s_temp)
            i = j+1+s_len
            j = i
        return res

        