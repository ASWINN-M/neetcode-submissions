class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}

        for k , v in enumerate(nums):
            hash_nums[v] = k
        
        for i in range(len(nums)):
            if target - nums[i] in hash_nums:
                if i != hash_nums[target - nums[i]]:
                    return [i , hash_nums[target - nums[i]]]
