"""
数组的相对排序
"""


# 1
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        return res + sorted(arr1)


# 2
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        return res + sorted(arr1)


# 3
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        return res + sorted(arr1)


# 4
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        return res + sorted(arr1)


# 5
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            while i in arr1:
                res.append(i)
                arr1.remove(i)
        return res + sorted(arr1)

