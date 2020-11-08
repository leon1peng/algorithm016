"""
N 皇后 II

"""


# 1
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                tmp += 1
                return tmp

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    tmp = backtrack(row + 1, tmp, cols | {col}, pie | {row + col}, na | {row - col})
            return tmp

        return backtrack(0, 0, set(), set(), set())


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        self.count = 0

        def DFS(n, row, cols, pie, na):
            if row >= n:
                self.count += 1
                return
            bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得道当前所有的空位
            while bits:
                p = bits & -bits  # 取到最低位的 1
                bits = bits & (bits - 1)  # 表示在 p 位置上放入皇后
                DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
        DFS(n, 0, 0, 0, 0)
        return self.count


# 2
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                tmp += 1
                return tmp

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    tmp = backtrack(row + 1, tmp, cols | {col}, pie | {row + col}, na | {row - col})
            return tmp

        return backtrack(0, 0, set(), set(), set())


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        self.count = 0

        def DFS(n, row, cols, pie, na):
            if row >= n:
                self.count += 1
                return
            bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得道当前所有的空位
            while bits:
                p = bits & -bits  # 取到最低位的 1
                bits = bits & (bits - 1)  # 表示在 p 位置上放入皇后
                DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
        DFS(n, 0, 0, 0, 0)
        return self.count


# 3
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                tmp += 1
                return tmp

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    tmp = backtrack(row + 1, tmp, cols | {col}, pie | {row + col}, na | {row - col})
            return tmp

        return backtrack(0, 0, set(), set(), set())


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        self.count = 0

        def DFS(n, row, cols, pie, na):
            if row >= n:
                self.count += 1
                return
            bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得道当前所有的空位
            while bits:
                p = bits & -bits  # 取到最低位的 1
                bits = bits & (bits - 1)  # 表示在 p 位置上放入皇后
                DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
        DFS(n, 0, 0, 0, 0)
        return self.count


#
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                tmp += 1
                return tmp

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    tmp = backtrack(row + 1, tmp, cols | {col}, pie | {row + col}, na | {row - col})
            return tmp

        return backtrack(0, 0, set(), set(), set())


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        self.count = 0

        def DFS(n, row, cols, pie, na):
            if row >= n:
                self.count += 1
                return
            bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得道当前所有的空位
            while bits:
                p = bits & -bits  # 取到最低位的 1
                bits = bits & (bits - 1)  # 表示在 p 位置上放入皇后
                DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
        DFS(n, 0, 0, 0, 0)
        return self.count


# 5
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                tmp += 1
                return tmp

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    tmp = backtrack(row + 1, tmp, cols | {col}, pie | {row + col}, na | {row - col})
            return tmp

        return backtrack(0, 0, set(), set(), set())


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        self.count = 0

        def DFS(n, row, cols, pie, na):
            if row >= n:
                self.count += 1
                return
            bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得道当前所有的空位
            while bits:
                p = bits & -bits  # 取到最低位的 1
                bits = bits & (bits - 1)  # 表示在 p 位置上放入皇后
                DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
        DFS(n, 0, 0, 0, 0)
        return self.count



