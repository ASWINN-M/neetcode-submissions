class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])

        l , r = 0 , cols - 1
        res = []
        for i in matrix:
            if i[l] <= target <= i[r]:
                res = i
                break
        
        if not res:
            return False
        l , r = 0 , len(res) - 1

        while l <= r:
            m = (l + r) // 2

            if res[m] < target:
                l = m + 1
            elif res[m] > target:
                r = m - 1
            else:
                return True
        
        return False
