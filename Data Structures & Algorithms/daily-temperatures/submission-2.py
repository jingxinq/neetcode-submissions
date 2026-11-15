class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for idx, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                temp = st.pop()
                res[temp] = idx - temp 
            st.append(idx)

        return res
        