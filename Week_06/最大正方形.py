"""
最大正方形

DP:
    1. 分治(子问题): problem[i][j] = min(sub[i - 1][j], sub[i][j - 1]) + 1
    2. 状态数组： dp[i][j]
    3. DP 方程： dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
"""


# 1
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else int(matrix[i - 1][j - 1])
        max_num = 0
        for i in range(len(dp)):
            row_max = max(dp[i])
            max_num = max(max_num, row_max)
        return max_num * max_num


# 2
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else int(matrix[i - 1][j - 1])
        max_num = 0
        for i in range(len(dp)):
            row_max = max(dp[i])
            max_num = max(max_num, row_max)
        return max_num * max_num


# 3
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else int(matrix[i - 1][j - 1])
        max_num = 0
        for i in range(len(dp)):
            row_max = max(dp[i])
            max_num = max(max_num, row_max)
        return max_num * max_num


# 4
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else int(matrix[i - 1][j - 1])
        max_num = 0
        for i in range(len(dp)):
            row_max = max(dp[i])
            max_num = max(max_num, row_max)
        return max_num * max_num


# 5
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else int(matrix[i - 1][j - 1])
        max_num = 0
        for i in range(len(dp)):
            row_max = max(dp[i])
            max_num = max(max_num, row_max)
        return max_num * max_num
