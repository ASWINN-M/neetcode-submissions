class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {i : [] for i in nums}

        for n in range(len(nums)):
            freq[nums[n]].append(n)
        
        for key , val in freq.items():
            if len(val) > 1:
                for i in range(1 , len(val)):
                    if abs(val[i - 1] - val[i]) <= k:
                        return True

        return False