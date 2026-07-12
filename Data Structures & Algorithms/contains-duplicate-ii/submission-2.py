class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(list)
        for key , v in enumerate(nums):
            freq[v].append(key)
        
        val = list(freq.values())
        for i in range(len(val)):
            if len(val[i]) > 1:
                for j in range(len(val[i]) - 1):
                    if abs(val[i][j] - val[i][j + 1]) <= k:
                        return True
        
        return False

        

        
