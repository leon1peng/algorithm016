"""
翻转对
"""
import bisect


# 1
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = []
        res = 0
        for num in nums:
            res += len(arr) - bisect.bisect_right(arr, num * 2)
            loc = bisect.bisect_right(arr, num)
            arr[loc:loc] = [num]
        return res






