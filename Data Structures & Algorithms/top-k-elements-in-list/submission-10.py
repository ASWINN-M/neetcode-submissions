class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for i in nums:
            freq[i] = freq.get(i , 0) + 1
        
        count = {i : [] for i in range(len(nums) + 1)}

        for key , v in freq.items():
            count[v].append(key)
        print(count)
        for i in range(len(nums), -1, -1):
            if count[i] != [] and k != 0:
                k -= len(count[i])
                res.append(count[i])
        
        flat = [x for sublist in res for x in sublist]
        return flat

        

        

        
        