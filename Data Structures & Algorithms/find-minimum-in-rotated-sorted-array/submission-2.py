class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        min_val = float("inf")

        while l <= r:
            m = (l + r) // 2

            if nums[l] > nums[r] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            min_val = min(nums[m] , min_val)
        
        return min_val
