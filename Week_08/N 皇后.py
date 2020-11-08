"""
N 皇后

回溯
"""


# 1
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, cur_str = [], "." * n

        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                res.append(tmp)
                return

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    backtrack(row + 1, tmp + [cur_str[:col] + "Q" + cur_str[col + 1:]], cols | {col}, pie | {row + col}, na | {row - col})

        backtrack(0, [], set(), set(), set())
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


# 2
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, cur_str = [], "." * n

        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                res.append(tmp)
                return

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    backtrack(row + 1, tmp + [cur_str[:col] + "Q" + cur_str[col + 1:]], cols | {col}, pie | {row + col}, na | {row - col})

        backtrack(0, [], set(), set(), set())
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


# 3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, cur_str = [], "." * n

        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                res.append(tmp)
                return

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    backtrack(row + 1, tmp + [cur_str[:col] + "Q" + cur_str[col + 1:]], cols | {col}, pie | {row + col}, na | {row - col})

        backtrack(0, [], set(), set(), set())
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


# 4
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, cur_str = [], "." * n

        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                res.append(tmp)
                return

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    backtrack(row + 1, tmp + [cur_str[:col] + "Q" + cur_str[col + 1:]], cols | {col}, pie | {row + col}, na | {row - col})

        backtrack(0, [], set(), set(), set())
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


# 5
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, cur_str = [], "." * n

        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                res.append(tmp)
                return

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    backtrack(row + 1, tmp + [cur_str[:col] + "Q" + cur_str[col + 1:]], cols | {col}, pie | {row + col}, na | {row - col})

        backtrack(0, [], set(), set(), set())
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]













