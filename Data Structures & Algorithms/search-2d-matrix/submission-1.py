class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mL, mR = 0, len(matrix)-1
        n = []
        while mL <= mR:
            mid = (mL+mR) // 2
            if target < matrix[mid][0]:
                mR = mid - 1
            elif target > matrix[mid][-1]:
                mL = mid + 1
            else:
                n = matrix[mid]
                break

        nL, nR = 0, len(n)-1
        while nL <= nR:
            mid = (nL+nR) // 2
            if target < n[mid]:
                nR = mid - 1
            elif target > n[mid]:
                nL = mid + 1
            else:
                return True

        return False





        