class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l , r = max(nums) , sum(nums)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            temp , sub , i = 0 , 0 , 0

            while i < len(nums):
                temp += nums[i]
                if temp > mid:
                    sub += 1
                    temp = 0
                else:
                    i += 1
            
            if sub < k:
                r = mid - 1
                res = mid 
            else:
                l = mid + 1
        
        return res
