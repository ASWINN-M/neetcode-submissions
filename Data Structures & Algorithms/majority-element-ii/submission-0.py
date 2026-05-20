class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hash_nums = {}
        for i in nums:
            if i in hash_nums:
                hash_nums[i] += 1
            else:
                hash_nums[i] = 1
        for k,v in hash_nums.items():
            if v > len(nums) // 3:
                res.append(k)
        return res
        