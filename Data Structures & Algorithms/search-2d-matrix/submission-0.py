class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L,R = 0, len(matrix)-1
        m = 0
        while L<=R:
            mid = (L+R)//2
            if target > matrix[mid][-1]:
                L = mid + 1
            elif target < matrix[mid][0]:
                R = mid - 1
            else:
                m = mid
                break
        
        nL, nR = 0, len(matrix[m])-1
        while nL <= nR:
            mid = (nL+nR)//2
            if target > matrix[m][mid]:
                nL = mid + 1
            elif target < matrix[m][mid]:
                nR = mid - 1
            else:
                return True

        return False

                