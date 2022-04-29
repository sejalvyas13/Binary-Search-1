// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the target row by binary search
        #find the target element in that row by binary search
        
        if len(matrix) == 0 or len(matrix[0]) == 0 : return False
        
        #finding target row by iterating over first elements of every column
        j = 0
        top = 0
        bottom = len(matrix) - 1
        targetRow = 0
        while top < bottom :
            if bottom - top == 1 :
                if matrix[top][0] <= target and target < matrix[bottom][0]:
                    targetRow = top
                else :
                    targetRow = bottom
                break
            mid = (top + bottom) // 2
            if target <= matrix[mid][0] :
                bottom = mid
            else :
                top = mid
        
        # binary search on top row
        left = 0
        right = len(matrix[0])-1
        while left <= right :
            mid = (left + right) // 2
            if target == matrix[targetRow][mid] :
                return True
            if target < matrix[targetRow][mid] :
                right = mid - 1
            else :
                left = mid + 1
        return False
        
