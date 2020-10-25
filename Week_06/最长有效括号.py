"""
最长有效括号

DP

    DP 方程：dp[i] = dp[i - k]|0 + X
        s[i] == ")"
            若 s[i - 1] == "(":
                k = 2, X = 2
                i >= 2 => dp[i] = dp[i - 2] + 2
                否则    => dp[i] = 0 + 2
            否则 若 i - 上一个位置的长度 > 0 且 已经匹配成功的括号的前一个括号为"(": （当前")"匹配成功）
                k = 1, X = 当前已匹配成功的前一个位置匹配成功的长度（有则返回长度，无则返回0）
                有 => dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                无 => dp[i] = dp[i - 1] + 0 + 2

"""


# 1
# DP
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans, n = 0, len(s)
        if n == 0: return 0
        dp = [0] * n
        for i in range(len(s)):
            if s[i] == ")":
                if i == 0: continue
                if s[i - 1] == "(":
                    dp[i] = [0, dp[i - 2]][i >= 2] + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + [0, dp[i - dp[i - 1] - 2]][i - dp[i - 1] >= 2] + 2
                maxans = max(maxans, dp[i])
                print(i, maxans)
        return maxans


# 辅助栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack, ans = [], 0
        for i in range(len(s)):
            if not stack or s[i] == "(" or s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans


# 2
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack, ans = [], 0
        for i in range(len(s)):
            if not stack or s[i] == "(" or s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans


# 3
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack, ans = [], 0
        for i in range(len(s)):
            if not stack or s[i] == "(" or s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans


# 4
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack, ans = [], 0
        for i in range(len(s)):
            if not stack or s[i] == "(" or s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans


# 5
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack, ans = [], 0
        for i in range(len(s)):
            if not stack or s[i] == "(" or s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans
