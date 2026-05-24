class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i , 0) + 1
        
        for k , v in freq.items():
            if v > 1:
                return k