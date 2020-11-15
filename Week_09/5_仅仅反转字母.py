"""
仅仅反转字母
"""


# 1
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        front, end = 0, len(S) - 1
        while front < end:
            if not S[front].isalpha():
                front += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[front], S[end] = S[end], S[front]
                front += 1
                end -= 1
        return "".join(S)


# 2
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        front, end = 0, len(S) - 1
        while front < end:
            if not S[front].isalpha():
                front += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[front], S[end] = S[end], S[front]
                front += 1
                end -= 1
        return "".join(S)


# 3
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        front, end = 0, len(S) - 1
        while front < end:
            if not S[front].isalpha():
                front += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[front], S[end] = S[end], S[front]
                front += 1
                end -= 1
        return "".join(S)


# 4
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        front, end = 0, len(S) - 1
        while front < end:
            if not S[front].isalpha():
                front += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[front], S[end] = S[end], S[front]
                front += 1
                end -= 1
        return "".join(S)


# 5
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        front, end = 0, len(S) - 1
        while front < end:
            if not S[front].isalpha():
                front += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[front], S[end] = S[end], S[front]
                front += 1
                end -= 1
        return "".join(S)


