class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(l , r):
            m = (l + r) // 2
            if l > r:
                return -1
            
            if nums[m] > target:
                return binSearch(l , m - 1)
            if nums[m] < target:
                return binSearch(m + 1 , r)
            else:
                return m
        
        return binSearch(0 , len(nums) - 1)
            