class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        s = 0
        res = 0
        for n in range(len(nums)):
            s += nums[n]
            check = s - k
            res += prefix.get(check , 0)
            prefix[s] = prefix.get(s , 0) + 1
        return res

        

        