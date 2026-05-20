class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        n = len(nums)
        ans[n:] = nums
        ans[:n] = nums 
        return ans