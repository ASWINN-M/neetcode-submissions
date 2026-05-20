class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        check = 0
        for r in range(len(nums)):
            check += nums[r]

            while check >= target:
                res = min(res , r - l + 1)
                check -= nums[l]
                l += 1
        return res if res != float('inf') else 0

                
        
        