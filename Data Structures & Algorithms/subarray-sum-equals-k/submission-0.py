class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        s , res = 0 , 0

        for r in range(len(nums)):
            s += nums[r]

            res += prefix.get(s - k , 0)
            prefix[s] = 1 + prefix.get(s , 0)

        return res


