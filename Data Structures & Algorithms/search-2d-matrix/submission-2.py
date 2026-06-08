class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target < matrix[i][0] or target > matrix[i][-1]:
                continue
            
            left = 0 
            right = len(matrix[i]) - 1
            while left <= right: 
                middle = (left + right) // 2
                if matrix[i][middle] > target:
                    right -= 1
                elif matrix[i][middle] < target:
                    left += 1
                else:
                    return True
            return False
        
        return False 