class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinish(k) -> bool:
            total = 0
            for p in piles:
                total += (p+k-1)//k
            return total <= h
        
        l, r = 1, max(piles)

        while l < r:
            mid = (r+l)//2
            if canFinish(mid):
                r = mid
            else:
                l = mid+1

        return l

