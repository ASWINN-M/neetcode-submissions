class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums = {}
        for i in nums:
            if i in hash_nums:
                hash_nums[i] += 1
            else:
                hash_nums[i] = 1
        print(hash_nums)
        sorted_keys = sorted(hash_nums, key=hash_nums.get)
        res = sorted_keys[-k : ]
        print(res)
        return res
        