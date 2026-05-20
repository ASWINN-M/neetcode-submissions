class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l , r = 0 , len(nums) - 1
        k %= len(nums)

        nums[:] = nums[-k:] + nums[:-k]
        
        print(nums)
         