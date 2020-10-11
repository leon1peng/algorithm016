"""
搜索二维矩阵
"""


# 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // col][mid % col] < target:
                left = mid + 1
            else:
                right = mid
        return left < row * col and matrix[left // col][left % col] == target


# 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col, left = len(matrix), len(matrix[0]), 0
        right = row * col
        while left < right:
            mid = (left + right) // 2
            if matrix[mid // col][mid % col] < target:
                left = mid + 1
            else:
                right = mid
        return left < row * col and matrix[left // col][left % col] == target


