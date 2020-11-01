"""
括号生成
"""


# 1
# 回溯
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(stack, left, right):
            if len(stack) == 2 * n:
                ans.append("".join(stack))
                return
            if left < n:
                stack.append("(")
                backtrack(stack, left + 1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(stack, left, right + 1)
                stack.pop()
        backtrack([], 0, 0)
        return ans


# DFS
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur_s, left, right):
            if left == 0 and right == 0:
                res.append(cur_s)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_s + "(", left - 1, right)
            if right > 0:
                dfs(cur_s + ")", left, right - 1)

        dfs("", n, n)
        return res


# 2
# 回溯
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur_str, left, right):
            if len(cur_str) == 2 * n:
                res.append(cur_str)
                return
            if left < n:
                backtrack(cur_str + "(", left + 1, right)
            if right < left:
                backtrack(cur_str + ")", left, right + 1)

        backtrack("", 0, 0)
        return res


# DFS
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur_s, left, right):
            if left == 0 and right == 0:
                res.append(cur_s)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_s + "(", left - 1, right)
            if right > 0:
                dfs(cur_s + ")", left, right - 1)

        dfs("", n, n)
        return res



