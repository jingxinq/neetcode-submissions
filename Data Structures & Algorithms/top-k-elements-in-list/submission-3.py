class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count freq per num
        # 2. bucket sort it
        # 3. get top k
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        
        for key, value in count.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
            if len(res) == k:
                return res

                





