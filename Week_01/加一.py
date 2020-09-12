"""
加一
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_num = 0
        for i in range(len(digits)):
            sum_num += digits[i] * pow(10, len(digits)-i-1)
        return [int(num) for num in str(sum_num+1)]

