class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}

        for k , v in enumerate(nums):
            hash_nums[v] = k
        
        res = [0 , 0]
        for i in range(len(nums)):
            if target - nums[i] in hash_nums and i != hash_nums[target - nums[i]]:
                res[0] = i
                res[1] = hash_nums[target - nums[i]]
                break
        
        return res