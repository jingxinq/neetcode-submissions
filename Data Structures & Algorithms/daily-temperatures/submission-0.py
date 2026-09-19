class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    prev_idx = stack[-1]
                    stack.pop()
                    res[prev_idx] = i - prev_idx
                stack.append(i)
        return res
            
            