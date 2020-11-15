"""
符串转换整数 (atoi)
"""
import re


# 1
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) < 1:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


# 2
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) < 1:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


# 3
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) < 1:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


# 4
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) < 1:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


# 5
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) < 1:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']:
            del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))




