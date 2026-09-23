class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return index of target
        L, R = 0, len(nums)-1
        mid = 0
        while L <= R:
            mid = (L+R)//2
            if nums[mid] == target:
                return mid
            elif nums[L] <= nums[mid]: #left is sorted
                if nums[L] <= target < nums[mid]:
                    R = mid-1
                else:
                    L = mid+1 # to find the rotation point
            else: # right is sorted
                if nums[mid] < target <= nums[R]:
                    L = mid+1
                else:
                    R = mid-1
 
        return -1

