class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        check = set(nums)
        print(check)
        for i in nums:
            count = 1
            j = i
            if j - 1 in check:
                while (j - 1) in check:
                    count += 1
                    j -= 1
            
            res = max(res , count)
        return res