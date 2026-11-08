class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                val2 = stack.pop()
                val1 = stack.pop()
                res = val2 + val1
                stack.append(res)
            elif t == '-':
                val2 = stack.pop()
                val1 = stack.pop()
                res = val1 - val2
                stack.append(res)
            elif t == '*':
                val2 = stack.pop()
                val1 = stack.pop()
                res = val1 * val2
                stack.append(res)
            elif t == '/':
                val2 = stack.pop()
                val1 = stack.pop()
                res = int(val1/val2)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack.pop()


        