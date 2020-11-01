"""
单词接龙
"""
from collections import deque, defaultdict


# 1
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 先验判断
        if endWord not in wordList:
            return 0
        # 提前构建邻接表 -> 用generic state做key
        in_words = defaultdict(list)
        word_len = len(beginWord)
        for word in wordList:
            for i in range(word_len):
                in_words[word[:i] + '*' + word[i + 1:]].append(word)
        # 建队列 加初始状态
        queue = deque()
        memo = set()
        queue.append(beginWord)
        memo.add(beginWord)
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_word = queue.popleft()
                for i in range(word_len):
                    in_cur_word = cur_word[:i] + '*' + cur_word[i + 1:]
                    # 下一个状态的所有word
                    for word in in_words[in_cur_word]:
                        if word == endWord:
                            return step + 1
                        if word not in memo:
                            queue.append(word)
                            memo.add(word)
            step += 1
        else:
            return 0
