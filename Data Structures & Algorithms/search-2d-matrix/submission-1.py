class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])
        l , r = 0 , len(matrix) - 1
        row = None
        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row = m
                break
            
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        print(row)
        if row == None:
            return False
        mat = matrix[row]
        print(mat)
        l , r = 0 , len(mat) - 1

        while l <= r:
            m = (l + r) // 2

            if mat[m] == target:
                return True
            
            elif mat[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False

        

        