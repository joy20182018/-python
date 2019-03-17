'''

双端队列

Deque() 创建一个空的新 deque。 它不需要参数， 并返回空的 deque。
addFront(item) 将一个新项添加到 deque 的首部。 它需要 item 参数 并不返回任何内容。
addRear(item) 将一个新项添加到 deque 的尾部。 它需要 item 参数并不返回任何内容。
removeFront() 从 deque 中删除首项。 它不需要参数并返回 item。 deque 被修改。
removeRear() 从 deque 中删除尾项。 它不需要参数并返回 item。 deque 被修改。
isEmpty() 测试 deque 是否为空。 它不需要参数， 并返回布尔值。
size() 返回 deque 中的项数。 它不需要参数， 并返回一个整数。

'''


class DequeData:

    def __init__(self):
        self.deque = []

    def isEmpty(self):
        return self.deque == []

    def addFront(self, item):
        self.deque.append(item)
        # self.deque.insert(len(self.deque))

    def addRear(self, item):
         self.deque.insert(0,item)

    def removeFront(self):
        return self.deque.pop()

    def removeRear(self):
        return self.deque.pop(0)

    def size(self):
        return len(self.deque)