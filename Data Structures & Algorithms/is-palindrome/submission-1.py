class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            left = s[l].lower()
            right = s[r].lower()
            if left.isalnum() and right.isalnum():
                if left != right:
                    return False
                else:
                    l += 1
                    r -= 1
            elif not left.isalnum():
                l +=1
            else:
                r -= 1
        
        return True

