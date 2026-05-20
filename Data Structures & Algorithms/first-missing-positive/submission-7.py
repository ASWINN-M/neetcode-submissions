class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or max(nums) < 1:
            return 1
        
        start = min(nums)
        check_nums = set(nums)

        for i in range(1 , len(nums) + 1):
            if i not in check_nums:
                return i
        
        return max(nums) + 1 if max(nums) > 0 else 1