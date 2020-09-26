"""
组合
77
https://leetcode-cn.com/problems/combinations/
"""
import itertools


# 方法1
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n < k or k <= 0:
            return res

        def backtrack(i, k, tmp):
            if k == 0:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrack(j + 1, k - 1, tmp + [j])
        backtrack(1, k, [])
        return res


# 方法二
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))
