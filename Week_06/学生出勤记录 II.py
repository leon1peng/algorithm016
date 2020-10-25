"""
学生出勤记录 II

DP
    1. 子问题: problem(i, j, k)  -> 第 i 天，有 j 个 A，末尾有 k 个 L。
    2. 状态数组:
        f(i, j, k)
        f(i, 0, 0), f(i, 0, 1), f(i, 0, 2), f(i, 1, 0), f(i, 1, 1), f(i, 1, 2)
    3. DP 方程: (所有原因都同1)
        1. dp(i, 0, 0) = dp(i-1, 0, 0) + dp(i-1,0,1) + dp(i-1, 0, 2)
            原因是因为无论第 i-1 天的末尾是 P、L 或者 LL，在第 i 天到场(末尾+P)，都会变成 dp[i, 0, 0]
        2. dp(i,0,1) = dp(i-1,0,0)
        3. dp(i,0, 2) = dp(i-1,0,1)
        4. dp(i, 1, 0) = dp(i-1,1,0) + dp(i-1,1,1) + dp(i-1, 1, 2) + dp(i-1,0,0) + dp(i-1,0,1) + dp(i-1, 0, 2)
        5. dp(i, 1, 1) = dp(i-1, 1, 0)
        6. dp(i, 1, 2) = dp(i-1, 1, 1)
"""


# 1
class Solution:
    def checkRecord(self, n: int) -> int:
        dp00 = dp01 = dp10 = 1
        dp02 = dp11 = dp12 = 0
        while n > 1:
            dp00, dp01, dp02, dp10, dp11, dp12 = (dp00 + dp01 + dp02) % 1000000007, dp00, dp01, (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007, dp10, dp11
            n -= 1
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007


# 2
class Solution:
    def checkRecord(self, n: int) -> int:
        dp00 = dp01 = dp10 = 1
        dp02 = dp11 = dp12 = 0
        while n > 1:
            dp00, dp01, dp02, dp10, dp11, dp12 = (dp00 + dp01 + dp02) % 1000000007, dp00, dp01, (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007, dp10, dp11
            n -= 1
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007


# 3
class Solution:
    def checkRecord(self, n: int) -> int:
        dp00 = dp01 = dp10 = 1
        dp02 = dp11 = dp12 = 0
        while n > 1:
            dp00, dp01, dp02, dp10, dp11, dp12 = (dp00 + dp01 + dp02) % 1000000007, dp00, dp01, (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007, dp10, dp11
            n -= 1
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007


# 4
class Solution:
    def checkRecord(self, n: int) -> int:
        dp00 = dp01 = dp10 = 1
        dp02 = dp11 = dp12 = 0
        while n > 1:
            dp00, dp01, dp02, dp10, dp11, dp12 = (dp00 + dp01 + dp02) % 1000000007, dp00, dp01, (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007, dp10, dp11
            n -= 1
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007


# 5
class Solution:
    def checkRecord(self, n: int) -> int:
        dp00 = dp01 = dp10 = 1
        dp02 = dp11 = dp12 = 0
        while n > 1:
            dp00, dp01, dp02, dp10, dp11, dp12 = (dp00 + dp01 + dp02) % 1000000007, dp00, dp01, (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007, dp10, dp11
            n -= 1
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % 1000000007
