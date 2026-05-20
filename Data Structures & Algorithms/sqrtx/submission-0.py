class Solution:
    def mySqrt(self, x: int) -> int:
        l , r = 1 , x

        if not x:
            return 0
        
        while l <= r:
            m = (l + r) // 2

            if m ** 2 == x:
                return m       
            elif m ** 2 > x:
                r = m - 1
            else:
                l = m + 1

        return r