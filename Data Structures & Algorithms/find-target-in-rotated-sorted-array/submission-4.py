class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        min_val = float("inf")
        idx = 0
        while l <= r:
            m = (l + r) // 2
            
            if nums[l] > nums[r] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            if min_val > nums[m]:
                min_val = nums[m]
                idx = m
        l , r = 0 , len(nums) - 1
        print(l , r , idx)
        if nums[idx] == target:
            return idx
        if nums[idx] <= target <= nums[-1]:
            l, r = idx, len(nums) - 1
        else:
            l, r = 0, idx - 1
        print(l , r)
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        