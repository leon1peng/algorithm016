"""
两数之和
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, number in enumerate(nums):
            if hashmap.get(target-number) is not None:
                return [index, hashmap.get(target-number)]
            hashmap[number] = index
