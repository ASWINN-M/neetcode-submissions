class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights) , sum(weights)
        res = 0
        
        while l <= r:
            capacity = (l + r) // 2
            ship = 1
            wei = 0
            i = 0
            while i < len(weights):
                if wei + weights[i] > capacity:
                    ship += 1
                    wei = 0
                else:
                    wei += weights[i]
                    i += 1
            if ship > days:
                l = capacity + 1
            else:
                r = capacity - 1
                res = capacity
        return res




