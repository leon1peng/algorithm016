"""
回文子串

DP
"""


# 1
# DP
class Solution:
    def __init__(self):
        self.res = 0

    def countSubstrings(self, s: str) -> int:
        n, self.res = len(s), 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j, self.res = i - 1, j + 1, self.res + 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res


# 暴力
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    res += 1
        return res


# 2
class Solution:
    def __init__(self):
        self.res = 0

    def countSubstrings(self, s: str) -> int:
        n, self.res = len(s), 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j, self.res = i - 1, j + 1, self.res + 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res


# 3
class Solution:
    def __init__(self):
        self.res = 0

    def countSubstrings(self, s: str) -> int:
        n, self.res = len(s), 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j, self.res = i - 1, j + 1, self.res + 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res
