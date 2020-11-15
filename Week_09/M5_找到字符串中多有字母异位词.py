"""
找到字符串中多有字母异位词

滑动窗口
"""


# 1
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count, s_count, res = [0] * 26, [0] * 26, []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res


# 2
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count, s_count, res = [0] * 26, [0] * 26, []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res


# 3
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count, s_count, res = [0] * 26, [0] * 26, []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res


# 4
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count, s_count, res = [0] * 26, [0] * 26, []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res


# 5
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count, s_count, res = [0] * 26, [0] * 26, []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res

