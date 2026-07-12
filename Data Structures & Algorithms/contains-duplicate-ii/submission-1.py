class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        verify = False

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    verify = True
        
        if not verify:
            return False
        return True