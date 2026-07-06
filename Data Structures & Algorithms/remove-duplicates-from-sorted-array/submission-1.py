class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}
        l = 0
        for i in nums:
            freq[i] = freq.get(i , 0) + 1
        
        
        res = list(freq.keys())
        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)
