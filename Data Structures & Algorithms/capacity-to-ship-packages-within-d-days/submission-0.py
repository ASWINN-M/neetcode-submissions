class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ships = days
        l , r = max(weights) , sum(weights)
        res = float("inf")
        while l <= r:
            cap = (l + r) // 2
            sub_sum , ship = 0 , 1
            i = 0
            while i < len(weights):
                if sub_sum + weights[i] > cap:
                    ship += 1
                    sub_sum = 0
                else:
                    sub_sum += weights[i]
                    i += 1
            
            if ship > ships:
                l = cap + 1
            else:
                r = cap - 1
                res = min(res , cap)
        
        return res
        