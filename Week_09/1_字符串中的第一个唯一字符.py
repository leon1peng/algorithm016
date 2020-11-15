"""
字符串中的第一个唯一字符
"""
import collections


# 1
# 哈希表
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


# 字典+集合
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {c: s.count(c) for c in set(s)}
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            if i != -1 and i == s.rfind(c):
                ans = min(ans, i)
        return ans if ans != len(s) else -1


# 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_map = {c: s.count(c) for c in set(s)}
        for i, c in enumerate(s):
            if dict_map[c] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_map = collections.Counter(s)
        for i, c in enumerate(s):
            if dict_map[c] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            idx = s.find(c)
            if idx != -1 and idx == s.rfind(c):
                ans = min(ans, idx)
        return ans if ans != len(s) else -1


# 3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_map = collections.Counter(s)
        for i, c in enumerate(s):
            if dict_map[c] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            idx = s.find(c)
            if idx != -1 and idx == s.rfind(c):
                ans = min(ans, idx)
        return ans if ans != len(s) else -1


# 4
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_map = collections.Counter(s)
        for i, c in enumerate(s):
            if dict_map[c] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            idx = s.find(c)
            if idx != -1 and idx == s.rfind(c):
                ans = min(ans, idx)
        return ans if ans != len(s) else -1


# 5
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_map = collections.Counter(s)
        for i, c in enumerate(s):
            if dict_map[c] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            idx = s.find(c)
            if idx != -1 and idx == s.rfind(c):
                ans = min(ans, idx)
        return ans if ans != len(s) else -1


