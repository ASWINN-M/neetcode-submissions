class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_hash = {}
        res = [0,0]
        for i,n in enumerate(nums):
            if target - nums[i] in n_hash:
                res[1] = i
                res[0] = n_hash[target - nums[i]]
            n_hash[n] = i
        return res
        