class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i , 0) + 1
        n = len(nums)
        for k , v in freq.items():
            if v > n / 2:
                return k
        