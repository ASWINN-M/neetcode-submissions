from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_count = 1
        set_nums = set(nums)
        lst_nums = list(set_nums)
        for i in range(len(lst_nums)):
            count = 1
            if lst_nums[i] - 1 in lst_nums:
                curr = lst_nums[i] - 1
                while curr in lst_nums:
                    count += 1
                    curr -= 1
                max_count = max(max_count , count)
        return max_count
            

        