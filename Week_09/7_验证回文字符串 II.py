"""
验证回文字符串 II
"""


# 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        if s[: mid] == s[-1: -1-mid: -1]:
            return True
        for i in range(mid):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                mid = (j - i) // 2
                return s[i: i+mid] == s[j-1: j-mid-1: -1] or s[i+1: i+mid+1] == s[j: j-mid: -1]


# 2
class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        if s[: mid] == s[-1: -1-mid: -1]:
            return True
        for i in range(mid):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                mid = (j - i) // 2
                return s[i: i+mid] == s[j-1: j-mid-1: -1] or s[i+1: i+mid+1] == s[j: j-mid: -1]


# 3
class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        if s[: mid] == s[-1: -1-mid: -1]:
            return True
        for i in range(mid):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                mid = (j - i) // 2
                return s[i: i+mid] == s[j-1: j-mid-1: -1] or s[i+1: i+mid+1] == s[j: j-mid: -1]


# 4
class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        if s[: mid] == s[-1: -1-mid: -1]:
            return True
        for i in range(mid):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                mid = (j - i) // 2
                return s[i: i+mid] == s[j-1: j-mid-1: -1] or s[i+1: i+mid+1] == s[j: j-mid: -1]


# 5
class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        if s[: mid] == s[-1: -1-mid: -1]:
            return True
        for i in range(mid):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                mid = (j - i) // 2
                return s[i: i+mid] == s[j-1: j-mid-1: -1] or s[i+1: i+mid+1] == s[j: j-mid: -1]





