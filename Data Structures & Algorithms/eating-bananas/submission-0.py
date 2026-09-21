import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k is too small, exceed h
        # k is large enough, wont exceed h

        L, R = 1, max(piles)
        res = 0
        while L <= R:
            mid = (L+R)//2
            total_time = 0
            for p in piles:
                time = math.ceil(p / mid)
                total_time += time
            if total_time <= h:
                R = mid - 1
                res = mid
            elif total_time > h:
                L = mid + 1
        return res
