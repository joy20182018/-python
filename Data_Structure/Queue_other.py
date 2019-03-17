'''

并规定列表起始段为队首，列表末段位队尾

Queue() 创建一个空的新队列。 它不需要参数， 并返回一个空队列。
enqueue(item) 将新项添加到队尾。 它需要 item 作为参数， 并不返回任何内容。
dequeue() 从队首移除项。 它不需要参数并返回 item。 队列被修改。
isEmpty() 查看队列是否为空。 它不需要参数， 并返回布尔值。
size() 返回队列中的项数。 它不需要参数， 并返回一个整数。

'''

class QueueData:
    def __init__(self):
         self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


# q = QueueData()
# q.enqueue(12)
# q.enqueue('frgve')
# q.enqueue('rewf')
# q.enqueue(123)
# q.enqueue(1246546)
# print(q.size())
# print(q.dequeue())
# print(q.dequeue())