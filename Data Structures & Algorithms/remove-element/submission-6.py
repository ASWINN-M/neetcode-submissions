class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        k = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[r] , nums[l] = nums[l] , nums[r]
                l += 1
            else:
                k += 1
        return len(nums) - k
            