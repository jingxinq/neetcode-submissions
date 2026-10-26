class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums_map = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in nums_map:
                diff_idx = nums_map[diff]
                res.append(diff_idx)
                res.append(idx)
                return res
            else:
                nums_map[n] = idx



