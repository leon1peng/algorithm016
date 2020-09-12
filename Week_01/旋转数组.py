"""
旋转数组
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k -= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
