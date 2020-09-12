"""
双端队列
"""


class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_length = k
        self.queue = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.queue) < self.max_length:
            self.queue = self.queue[::-1]
            self.queue.append(value)
            self.queue = self.queue[::-1]
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.queue) < self.max_length:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.queue:
            self.queue = self.queue[1:]
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.queue:
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.queue:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.queue:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not len(self.queue)

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.queue) == self.max_length


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(64)
param_1 = obj.insertFront(6)
print(param_1)
param_2 = obj.insertLast(2)
print(param_2)
param_3 = obj.deleteFront()
print(param_3)
param_4 = obj.deleteLast()
print(param_4)
param_5 = obj.getFront()
print(param_5)
param_6 = obj.getRear()
print(param_6)
param_7 = obj.isEmpty()
print(param_7)
param_8 = obj.isFull()
print(param_8)
