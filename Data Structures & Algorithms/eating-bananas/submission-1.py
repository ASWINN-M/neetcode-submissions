import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = float("inf")
        while l <= r:
            k = (l + r) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / k)
            
            if count > h:
                l = k + 1
            else:
                res = min(res , k)
                r = k - 1
            
            

        return res
            
            
            