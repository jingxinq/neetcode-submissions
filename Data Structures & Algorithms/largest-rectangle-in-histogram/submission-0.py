class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area = height x width
        # how to get width?

        # if height for i-1 / i+1 >= i, then can extend the width
        # how to use monotic stack?
        res = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = height * (i - index)
                res = max(res, area)
                start = index
            stack.append((start, h))

        for i, h in stack:
            area = h * (len(heights) - i)
            res = max(res, area)

        return res
