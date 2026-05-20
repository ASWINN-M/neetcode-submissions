class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        for l in range(len(nums)):
            s = 0
            for r in range(l , len(nums)):
                s += nums[r]

                if s >= target:
                    res = min(res , r - l + 1)
                    break
                
        return 0 if res == float('inf') else res
                
        
        