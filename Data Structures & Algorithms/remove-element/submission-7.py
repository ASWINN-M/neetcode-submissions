class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l , r = 0 , len(nums) - 1
        
        while l <= r:
            if nums[r] == val:
                r -= 1
            elif nums[l] != val:
                l += 1
            else:
                (nums[r] , nums[l]) = (nums[l] , nums[r]) 
                l += 1
                r -= 1
             
        
        count = 0
        for i in nums:
            if i == val:
                count += 1
        
        return len(nums[:len(nums) - count])
            