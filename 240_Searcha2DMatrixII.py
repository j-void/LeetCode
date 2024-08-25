class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            left, right = 0 , len(arr)-1
            while left < right:
                mid = (left+right)//2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    return True, mid
            return False, left
        rows = len(matrix)
        cols = len(matrix[0])
        
        r = rows-1
        c = 0
        while r >= 0 and c <= cols-1:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1
            else:
                c += 1

        return False
        
