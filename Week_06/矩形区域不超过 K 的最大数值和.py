"""
矩形区域不超过 K 的最大数值和

bisect:
    1. bisect_left(arr, cur - k)
        在 arr 中查找 cur-k，cur-k 存在时返回 cur-k 左侧的位置，cur-k 不存在返回应该插入的位置.
    2. insort(arr, cur)
        在 arr 中上述对应函数会返回的位置插入 cur。
"""
import bisect


# 1
# 双指针+前缀和+二分
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col, res = len(matrix), len(matrix[0]), float("-inf")
        for left in range(col):
            row_sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    row_sum[j] += matrix[j][right]
                arr, cur = [0], 0
                for tmp in row_sum:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr): res = max(cur - arr[loc], res)
                    bisect.insort(arr, cur)
        return res


# 2
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col, res = len(matrix), len(matrix[0]), float("-inf")
        for left in range(col):
            row_sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    row_sum[j] += matrix[j][right]
                arr, cur = [0], 0
                for tmp in row_sum:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr): res = max(cur - arr[loc], res)
                    bisect.insort(arr, cur)
        return res
