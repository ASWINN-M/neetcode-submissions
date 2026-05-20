class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for i in nums:
            freq[i] = freq.get(i , 0) + 1
        res = heapq.nlargest(k , freq.keys() , key = freq.get)

        return res
        

        

        
        