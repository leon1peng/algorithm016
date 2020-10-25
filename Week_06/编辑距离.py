"""
编辑距离

DP 方程：
    当 word1[i] == word2[j]: dp[i][j] = dp[i - 1][j - 1]
    当 word1[i] != word2[j]: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
"""
import functools


# 1
# DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


# 回溯 索引
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def backtrack(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:  # 局部贪心
                insert = backtrack(i, j + 1)
                delete = backtrack(i + 1, j)
                replace = backtrack(i + 1, j + 1)
                return min(insert, delete, replace) + 1
        return backtrack(0, 0)


# 2
# DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


# 回溯 索引
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def backtrack(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:  # 局部贪心
                insert = backtrack(i, j + 1)
                delete = backtrack(i + 1, j)
                replace = backtrack(i + 1, j + 1)
                return min(insert, delete, replace) + 1
        return backtrack(0, 0)


# 3
# DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


# 回溯 索引
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def backtrack(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:  # 局部贪心
                return min(backtrack(i, j + 1), backtrack(i + 1, j), backtrack(i + 1, j + 1)) + 1
        return backtrack(0, 0)


# 4
# DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


# 回溯 索引
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def backtrack(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:  # 局部贪心
                return min(backtrack(i, j + 1), backtrack(i + 1, j), backtrack(i + 1, j + 1)) + 1
        return backtrack(0, 0)


# 5
# DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


# 回溯 索引
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def backtrack(i, j):
            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:  # 局部贪心
                return min(backtrack(i, j + 1), backtrack(i + 1, j), backtrack(i + 1, j + 1)) + 1
        return backtrack(0, 0)
