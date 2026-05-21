class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] == target or nums[m] == target or nums[r] == target:
                if nums[l] == target:
                    return l
                elif nums[m] == target:
                    return m
                else:
                    return r    
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                
            
        
        return -1