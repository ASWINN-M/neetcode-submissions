class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l , r = 0 , n - 1
        peak = -1
        
        while l <= r:
            m = (l + r) // 2

            if mountainArr.get(m - 1) < mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            elif mountainArr.get(m - 1) > mountainArr.get(m) > mountainArr.get(m + 1):
                r = m - 1
            else:
                peak = m
                break
        l1 , r1 = 0 , peak
        l2 , r2 = peak + 1 , n - 1
        first_occ = -1
        while l1 <= r1:
            m = (l1 + r1) // 2

            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                r1 = m - 1
            else:
                l1 = m + 1        
            
        
        while l2 <= r2:
            m = (l2 + r2) // 2

            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                l2 = m + 1
            else:
                r2 = m - 1
        
        
        
        return first_occ
        

        