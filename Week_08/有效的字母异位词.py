"""
有效的字母异位词
"""


# 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join((lambda x: (x.sort(), x)[1])(list(s))) == "".join((lambda x: (x.sort(), x)[1])(list(t)))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        set_s = set(s)
        if set_s == set(t):
            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False


# 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s)
        if set_s == set(t):
            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False


# 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s)
        if set_s == set(t):
            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False


# 4
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s)
        if set_s == set(t):
            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False


# 5
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s)
        if set_s == set(t):
            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False

