"""
接雨水
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left, right = 0, n - 1
        maxleft, maxright = height[0], height[n - 1]
        ans = 0

        while left <= right:
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        return ans
