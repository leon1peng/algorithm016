# 学习笔记
### 位运算  布隆过滤器  LRU缓存  排序算法。

* 位运算： 在一些题目中，巧妙的应用位运算往往可以极大地提升运算时间，要熟记一些常用的位运算技巧
* LRU和LFU缓存的算法要记牢
* 经典的排序算法要总结熟记，整理后上传

# 十大经典排序算法

### 测试数据
original_list = [2, 56, 25, 14, 5, 38, 6, 2, 0, 45, 14, 36, 21, 12, 1, 1, 23, 56, 9, 0, 1, 9, 54]

### 比较排序法

1、冒泡排序
```Python
def bubble_sort(nums_list: list) -> list:
    for i in range(1, len(nums_list)):
        for j in range(0, len(nums_list) - i):
            if nums_list[j] > nums_list[j + 1]:
                nums_list[j], nums_list[j + 1] = nums_list[j + 1], nums_list[j]
    return nums_list
```

2、快速排序
```Python
def quick_sort(nums_list):
    def solve(nums_list, left, right):

        if left >= right:
            return nums_list
        key = nums_list[left]
        low = left
        high = right
        while left < right:
            while left < right and nums_list[right] >= key:
                right -= 1
            nums_list[left] = nums_list[right]
            while left < right and nums_list[left] <= key:
                left += 1
            nums_list[right] = nums_list[left]
        nums_list[right] = key
        solve(nums_list, low, left - 1)
        solve(nums_list, left + 1, high)
        return nums_list

    return solve(nums_list, 0, len(nums_list) - 1)
```

3、归并排序
```Python
def merge_sort(nums_list):
    if len(nums_list) <= 1:
        return nums_list
    num = len(nums_list) // 2
    left = merge_sort(nums_list[:num])
    right = merge_sort(nums_list[num:])

    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]

    return res
```

4、堆排序
```Python
import heapq
def heap_sort(nums_list):
    heapq.heapify(nums_list)
    res = []
    while nums_list:
        res.append(heapq.heappop(nums_list))
    return res
```

5、选择排序
```Python
def select_sort(nums_list):
    left = len(nums_list)
    for i in range(left - 1):
        min_index = i
        for j in range(i + 1, left):
            if nums_list[j] < nums_list[min_index]:
                min_index = j
        nums_list[i], nums_list[min_index] = nums_list[min_index], nums_list[i]
    return nums_list
```

6、插入排序
```Python
def insert_sort(nums_list):
    for i in range(1, len(nums_list)):
        j = i - 1
        key = nums_list[i]
        while j >= 0:
            if nums_list[j] > key:
                nums_list[j + 1] = nums_list[j]
                nums_list[j] = key
            j -= 1
    return nums_list
```

7、希尔排序
```Python
def shell_sort(nums_list):
    count = len(nums_list)
    step = 2
    group = count // step
    while group > 0:
        for i in range(group):
            j = i + group
            while j < count:
                key = nums_list[j]
                k = j - group
                while k >= 0 and nums_list[k] > key:
                    nums_list[k + group] = nums_list[k]
                    k -= group
                nums_list[k + group] = key
                j += group
        group //= step
    return nums_list
```

### 非比较排序法

8、计数排序
```Python
def count_sort(nums_list):
    res = [None for i in range(len(nums_list))]
    max_arr = max(nums_list)
    c = [0 for i in range(max_arr + 1)]
    for a in nums_list:
        c[a] += 1
    for i in range(1, max_arr + 1):
        c[i] += c[i - 1]
    for i in range(len(nums_list) - 1, -1, -1):
        res[c[nums_list[i]] - 1] = nums_list[i]
        c[nums_list[i]] -= 1
    return res
```

9、桶排序
```Python
def bucket_sort(nums_list):
    max_num = max(nums_list)
    bucket = [0] * (max_num + 1)
    for i in nums_list:
        bucket[i] += 1
    sort_nums = []
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums
```

10、基数排序
```Python
def radix_sort(nums_list):
    max_arr = max(nums_list)
    d = len(str(max_arr))
    for k in range(d):
        s = [[] for i in range(10)]
        for i in nums_list:
            s[i // (10 ** k) % 10].append(i)
        nums_list = [j for i in s for j in i]
    return nums_list
```
