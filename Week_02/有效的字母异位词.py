
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
