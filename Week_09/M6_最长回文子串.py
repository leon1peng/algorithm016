"""
最长回文子串
心扩散法 + （双指针）
"""


# 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        cur_length = [0, 1]
        for i in range(1, size):
            odd = self.long_sub(s, i - 1, i + 1)
            even = self.long_sub(s, i - 1, i)
            cur_length = max(cur_length, max(odd, even, key=lambda x: x[1] - x[0]), key=lambda x: x[1] - x[0])
        return s[cur_length[0]: cur_length[1]]

    def long_sub(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left, right = left - 1, right + 1
        return [left + 1, right]


# 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        cur_length = [0, 1]
        for i in range(1, size):
            odd = self.long_sub(s, i - 1, i + 1)
            even = self.long_sub(s, i - 1, i)
            cur_length = max(cur_length, max(odd, even, key=lambda x: x[1] - x[0]), key=lambda x: x[1] - x[0])
        return s[cur_length[0]: cur_length[1]]

    def long_sub(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left, right = left - 1, right + 1
        return [left + 1, right]


# 3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        cur_length = [0, 1]
        for i in range(1, size):
            odd = self.long_sub(s, i - 1, i + 1)
            even = self.long_sub(s, i - 1, i)
            cur_length = max(cur_length, max(odd, even, key=lambda x: x[1] - x[0]), key=lambda x: x[1] - x[0])
        return s[cur_length[0]: cur_length[1]]

    def long_sub(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left, right = left - 1, right + 1
        return [left + 1, right]


# 4
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        cur_length = [0, 1]
        for i in range(1, size):
            odd = self.long_sub(s, i - 1, i + 1)
            even = self.long_sub(s, i - 1, i)
            cur_length = max(cur_length, max(odd, even, key=lambda x: x[1] - x[0]), key=lambda x: x[1] - x[0])
        return s[cur_length[0]: cur_length[1]]

    def long_sub(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left, right = left - 1, right + 1
        return [left + 1, right]


# 5
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        cur_length = [0, 1]
        for i in range(1, size):
            odd = self.long_sub(s, i - 1, i + 1)
            even = self.long_sub(s, i - 1, i)
            cur_length = max(cur_length, max(odd, even, key=lambda x: x[1] - x[0]), key=lambda x: x[1] - x[0])
        return s[cur_length[0]: cur_length[1]]

    def long_sub(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left, right = left - 1, right + 1
        return [left + 1, right]
