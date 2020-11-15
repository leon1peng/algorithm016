# 学习笔记
## 不同路径 II
leetcode 上第 63 题 - 不同路径 II
链接：https://leetcode-cn.com/problems/unique-paths-ii/

### 分析 (DP)
    a. 重复性 （分治）： 
    I: 位置 (i, j) 上没有障碍物
        problem[i, j] = problem[i − 1, j] + problem[i, j − 1]
    II: 位置 (i, j) 上有障碍物
        problem[i, j] = 0
    b. 定义状态数组 : f[i, j]
    c. DP方程 : 
        I: 位置 (i, j) 上没有障碍物
            dp[i, j] = dp[i − 1, j] + dp[i, j − 1]
        II: 位置 (i, j) 上有障碍物
            dp[i, j] = 0
    
        即，状态转移方程为： dp[i, j] = (dp[i − 1, j] + dp[i, j − 1]) or 0

```Python
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        dp = [0 for i in range(width)] 
        dp[0] = 1
        
        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[width - 1]  
```
