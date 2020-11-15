"""
解码方法
DP:
思路一：
    1. 分治(子问题)： count[i] = sub[i - 1] + sub[i - 2]
    2. 状态数组: dp[i]
    3. DP 方程：
            I: 若 s[i] == "0": 若 s[i - 1] in ["1", "2"]: dp[i] = dp[i - 2]；否则 return 0
            注： 因为该情况下解码唯一，只能是（10 or 20）
            II： 否则若 s[i - 1] == "1" 或 (s[i - 1] == "2" 且 "1" <= s[i] <= "6"):
                    dp[i] = dp[i - 1] + dp[i - 2]
思路二：
    将思路一中“DP 方程的第二步合并”
            II:
"""


# 1
# 思路一
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        pre = cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == "0":
                if s[i - 1] in ["1", "2"]: cur = pre
                else: return 0
            elif s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"): cur += pre
            pre = tmp
        return cur


# 思路二
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]: return 0
        dp = [0 for x in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9: dp[i] += dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26: dp[i] += dp[i - 2]
        return dp[len(s)]


# 思路二代码优化
class Solution:
    def numDecodings(self, s: str) -> int:
        pre, cur = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            cur, cur = cur, cur * (9 < int(s[i - 1:i + 1]) <= 26) + cur * (int(s[i]) > 0)
        return cur


# 2
# 思路一
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        pre = cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == "0":
                if s[i - 1] in ["1", "2"]:
                    cur = pre
                else:
                    return 0
            elif s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                cur += pre
            pre = tmp
        return cur


# 思路二
class Solution:
    def numDecodings(self, s: str) -> int:
        pre, cur = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pre, cur = pre, cur * (9 < int(s[i - 1:i + 1]) <= 26) + cur * (int(s[i]) > 0)
        return cur


# 3
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        pre = cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == "0":
                if s[i - 1] in ["1", "2"]:
                    cur = pre
                else:
                    return 0
            elif s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                cur += pre
            pre = tmp
        return cur


class Solution:
    def numDecodings(self, s: str) -> int:
        pre, cur = 1, int(s[0] != "0")
        for i in range(1, len(s)):
            pre, cur = cur, pre * (9 < int(s[i - 1:i + 1]) <= 26) + cur * (int(s[i]) > 0)
        return cur


# 4
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        pre = cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == "0":
                if s[i - 1] in ["1", "2"]:
                    cur = pre
                else:
                    return 0
            elif s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                cur += pre
            pre = tmp
        return cur


class Solution:
    def numDecodings(self, s: str) -> int:
        pre, cur = 1, int(s[0] != "0")
        for i in range(1, len(s)):
            pre, cur = cur, pre * (9 < int(s[i - 1:i + 1]) <= 26) + cur * (int(s[i]) > 0)
        return cur


# 5
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        pre = cur = 1
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == "0":
                if s[i - 1] in ["1", "2"]:
                    cur = pre
                else:
                    return 0
            elif s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                cur += pre
            pre = tmp
        return cur


class Solution:
    def numDecodings(self, s: str) -> int:
        pre, cur = 1, int(s[0] != "0")
        for i in range(1, len(s)):
            pre, cur = cur, pre * (9 < int(s[i - 1:i + 1]) <= 26) + cur * (int(s[i]) > 0)
        return cur
