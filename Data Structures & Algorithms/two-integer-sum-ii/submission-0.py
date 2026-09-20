class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1
        res=[]
        while L<R:
            total = numbers[L]+numbers[R]
            if total == target:
                res.append(L+1)
                res.append(R+1)
                return res
            elif total < target:
                L+=1
            else:
                R-=1

            
                
        