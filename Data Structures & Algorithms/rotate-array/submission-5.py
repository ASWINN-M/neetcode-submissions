class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l , r = 0 , len(nums) - 1
        
        def reverse(nums , l , r):
            while l < r:
                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
                r -= 1
            return nums
        
        k = k % len(nums)

        reverse(nums , 0 , len(nums) - 1)
        reverse(nums , 0 , k - 1)
        reverse(nums , k , len(nums) - 1)
        print(nums)