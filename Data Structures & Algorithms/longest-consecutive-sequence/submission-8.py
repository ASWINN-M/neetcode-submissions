class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = set()
        for i in nums:
            seen.add(i)
        
        for i in range(len(nums)):
            j = nums[i]
            temp = 1
            if j - 1 in seen:
                while j in seen:
                    j += 1
                    temp += 1
            count = max(count , temp)

        return count       
