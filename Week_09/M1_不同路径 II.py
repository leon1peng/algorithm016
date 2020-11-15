"""
不同路径 II

DP: dp[j] += dp[j - 1]
"""
from typing import List


# 1
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        dp = [0 for i in range(width)]
        dp[0] = 1

        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[width - 1]


# 2
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        dp = [0 for i in range(width)]
        dp[0] = 1

        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[width - 1]


# 3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        dp = [0 for i in range(width)]
        dp[0] = 1

        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[width - 1]


# 4
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        dp = [0 for i in range(width)]
        dp[0] = 1

        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[width - 1]


# 5
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        dp = [0 for i in range(width)]
        dp[0] = 1

        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[width - 1]

