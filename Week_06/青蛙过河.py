"""
青蛙过河

"""


# 1
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n, s = len(stones), set(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)

        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need + 1 in dp[j] or need in dp[j]:
                    dp[i].add(need)

        return len(dp[-1]) > 0


# 2
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n, s = len(stones), set(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need in dp[j] or need + 1 in dp[j]:
                    dp[i].add(need)
        return len(dp[-1]) > 0


# 3
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n, s = len(stones), set(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need in dp[j] or need + 1 in dp[j]:
                    dp[i].add(need)
        return len(dp[-1]) > 0


# 4
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n, s = len(stones), set(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need in dp[j] or need + 1 in dp[j]:
                    dp[i].add(need)
        return len(dp[-1]) > 0


# 5
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n, s = len(stones), set(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need in dp[j] or need + 1 in dp[j]:
                    dp[i].add(need)
        return len(dp[-1]) > 0
