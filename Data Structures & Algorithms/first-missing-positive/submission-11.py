class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        present = set(nums)

        if 1 not in present:
            return 1
        
        itr = max(nums)
        found = False 
        for i in range(1, len(nums) + 1):
            if i not in present:
                found = True
                return i
        if not found:
            return itr + 1
            
        
