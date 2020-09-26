"""
全排列
47
https://leetcode-cn.com/problems/permutations-ii/
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(sol, nums, check):
            if len(sol) == len(nums):
                res.append(sol)
                return

            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                backtrack(sol + [nums[i]], nums, check)
                check[i] = 0

        nums.sort()
        res = []
        check = [0 for i in range(len(nums))]

        backtrack([], nums, check)
        return res