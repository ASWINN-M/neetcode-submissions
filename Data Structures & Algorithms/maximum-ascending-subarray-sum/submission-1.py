class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 1
        while r < len(nums):
            if nums[r - 1] < nums[r]:
                r += 1

            else:
                res = max(res , sum(nums[l : r]))
                l = r
                r += 1
        res = max(res , sum(nums[l : r + 1]))
        return res