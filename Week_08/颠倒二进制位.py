"""
颠倒二进制位
"""


# 1
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans >> 0


class Solution:
    def reverseBits(self, n: int) -> int:
        ans, mask = 0, 1
        for i in range(32):
            if n & mask:
                ans |= 1 << (31 - i)
            mask <<= 1
        return ans


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


# 2
class Solution:
    def reverseBits(self, n: int) -> int:
        ans, mask = 0, 1
        for i in range(32):
            if n & mask:
                ans |= 1 << (31 - i)
            mask <<= 1
        return ans


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


# 3
class Solution:
    def reverseBits(self, n: int) -> int:
        ans, mask = 0, 1
        for i in range(32):
            if n & mask:
                ans |= 1 << (31 - i)
            mask <<= 1
        return ans


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


# 4
class Solution:
    def reverseBits(self, n: int) -> int:
        ans, mask = 0, 1
        for i in range(32):
            if n & mask:
                ans |= 1 << (31 - i)
            mask <<= 1
        return ans


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
