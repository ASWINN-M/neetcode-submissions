class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0 , len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] > x:
                r = m - 1
            elif arr[m] < x:
                l = m + 1
            else:
                l = m
                break
        res = []
        l , r = l - 1 , l 
        
        while k > 0 and l >= 0 and r < len(arr):
            if abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1
        
        while k > 0 and l >= 0:
            res.append(arr[l])
            l -= 1
            k -= 1
        while k > 0 and r < len(arr):
            res.append(arr[r])
            r += 1
            k -= 1
        
        return sorted(res)
        
        


