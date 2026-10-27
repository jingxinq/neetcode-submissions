class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                char_stack.append(char)
            else:
                if not char_stack: 
                    return False
                popped = char_stack.pop()
                if (char == ")" and popped != "(") or (char == "}" and popped != "{") or (char == "]" and popped != "["):
                    return False
        
        return not char_stack 

        