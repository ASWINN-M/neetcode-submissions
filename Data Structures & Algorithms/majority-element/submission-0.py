class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_nums = {}
        for i in nums:
            if i in hash_nums:
                hash_nums[i] += 1
            else:
                hash_nums[i] = 1
        return max(hash_nums,key = hash_nums.get)