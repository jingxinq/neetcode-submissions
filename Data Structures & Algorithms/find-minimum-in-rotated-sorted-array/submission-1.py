class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotate len(lums) times give the original array
        # all elements are unique
        # return minimum element of array 
        #
        
        L, R = 0, len(nums)-1
        while L < R:
            mid = (L+R) // 2
            if nums[R] < nums[mid]:
                L = mid+1
            else:
                R = mid

        return nums[L]
