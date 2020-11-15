"""
最长上升子序列
"""
from typing import List


# 1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if dp[m] < num:
                    i = m + 1
                else:
                    j = m
            dp[i] = num
            if j == res:
                res += 1
        return res


# 2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if dp[m] < num:
                    i = m + 1
                else:
                    j = m
            dp[i] = num
            if j == res:
                res += 1
        return res


# 3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if dp[m] < num:
                    i = m + 1
                else:
                    j = m
            dp[i] = num
            if j == res:
                res += 1
        return res


# 4
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if dp[m] < num:
                    i = m + 1
                else:
                    j = m
            dp[i] = num
            if j == res:
                res += 1
        return res


# 5
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if dp[m] < num:
                    i = m + 1
                else:
                    j = m
            dp[i] = num
            if j == res:
                res += 1
        return res


