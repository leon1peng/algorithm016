"""
位1的个数
"""


# 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res


# 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res


# 3
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


# 4
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


# 5
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n &= (n - 1)
        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
