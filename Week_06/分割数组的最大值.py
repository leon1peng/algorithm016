"""
分割数组的最大值

DP 方程： dp[i][j] = min(dp[i][j], max(dp[i - 1][k], pre[j] - pre[k]))  # 0<= k < j
    ==> 结果超时
"""
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         pre = [0 for i in range(len(nums))]
#         pre[0] = nums[0]
#         for i in range(1, len(nums)):
#             pre[i] =  pre[i-1]  + nums[i]
#         dp = [[float('inf')] * len(nums) for i in range(m+1)]
#         for j in range(len(nums)):
#             dp[1][j] = pre[j]

#         for i in range(2, m + 1):
#             for j in range(i - 1, len(nums)):
#                 for k in range(0, j):
#                     dp[i][j] = min(dp[i][j], max(dp[i-1][k], pre[j] - pre[k]))
#         return dp[m][len(nums)-1]


# 二分查找
# 1
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)

        def test_mid(mid):
            num, cur_sum = 1, 0
            for i in nums:
                if cur_sum + i > mid:
                    cur_sum, num = i, num + 1
                else:
                    cur_sum += i
            return num > m

        while left < right:
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:
                left = mid+1
            else:
                right = mid

        return left


# 2
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)

        def test_mid(mid):
            num, cur_sum = 1, 0
            for i in nums:
                if cur_sum + i > mid:
                    cur_sum, num = i, num + 1
                else:
                    cur_sum += i
            return num > m

        while left < right:
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:
                left = mid+1
            else:
                right = mid

        return left


# 3
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)

        def test_mid(mid):
            num, cur_sum = 1, 0
            for i in nums:
                if cur_sum + i > mid:
                    cur_sum, num = i, num + 1
                else:
                    cur_sum += i
            return num > m

        while left < right:
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:
                left = mid+1
            else:
                right = mid

        return left
