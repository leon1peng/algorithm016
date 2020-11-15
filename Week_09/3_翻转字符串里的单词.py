"""
翻转字符串里的单词
"""


# 1
# 双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


# 分割 + 倒序
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# 2
# 双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


# 分割 + 倒序
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# 3
# 双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


# 分割 + 倒序
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# 4
# 双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


# 分割 + 倒序
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# 5
# 双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)


# 分割 + 倒序
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

