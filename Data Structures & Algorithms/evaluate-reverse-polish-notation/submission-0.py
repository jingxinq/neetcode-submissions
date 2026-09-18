class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                res.append(int(token))
            else:
                result = ""
                a = res.pop()
                b = res.pop()
                if token == "+":
                    result = b + a
                elif token == "-":
                    result = b - a
                elif token == "*":
                    result = b * a
                elif token == "/":
                    result = int(b / a)
                res.append(result)
        return res.pop()
               
        