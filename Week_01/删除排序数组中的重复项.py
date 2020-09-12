"""
删除排序数组中的重复项
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        preNum = nums[0]
        for num in nums:
            if num != preNum:
                preNum = num
                nums[count] = num
                count += 1
        return count
