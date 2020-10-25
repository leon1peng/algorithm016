"""
任务调度器

DP 方程： dp[i] = dp[i - 1] + 1 if count(char) == max(count(char))
"""


# 1
# DP
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length, task_map = len(tasks), dict()
        if length <= 1: return length
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        res = (task_sort[0][1] - 1) * (n + 1)
        for sort in task_sort:
            if sort[1] == task_sort[0][1]: res += 1
        return res if res >= length else length


# 2
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length, task_map = len(tasks), dict()
        if length <= 1: return length
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        res = (task_sort[0][1] - 1) * (n + 1)
        for sort in task_sort:
            if sort[1] == task_sort[0][1]: res += 1
        return res if res >= length else length


# 3
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length, task_map = len(tasks), dict()
        if length <= 1: return length
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        res = (task_sort[0][1] - 1) * (n + 1)
        for sort in task_sort:
            if sort[1] == task_sort[0][1]: res += 1
        return res if res >= length else length


# 4
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length, task_map = len(tasks), dict()
        if length <= 1: return length
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        res = (task_sort[0][1] - 1) * (n + 1)
        for sort in task_sort:
            if sort[1] == task_sort[0][1]: res += 1
        return res if res >= length else length


# 5
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length, task_map = len(tasks), dict()
        if length <= 1: return length
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        res = (task_sort[0][1] - 1) * (n + 1)
        for sort in task_sort:
            if sort[1] == task_sort[0][1]: res += 1
        return res if res >= length else length
