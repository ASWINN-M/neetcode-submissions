class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for i in nums:
            freq[i] = freq.get(i , 0) + 1
        n = len(nums)
        for k , v in freq.items():
            if v > n // 3:
                res.append(k)
        return res