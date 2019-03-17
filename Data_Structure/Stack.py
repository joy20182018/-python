'''

规定列表起始段为栈底，末端为栈顶

push(item)将一个新项添加到栈的顶部。 它需要 item 做参数并不返回任何内容。
pop() 从栈中删除顶部项。 它不需要参数并返回 item 。 栈被修改。
peek() 从栈返回顶部项， 但不会删除它。 不需要参数。 不修改栈。
isEmpty() 测试栈是否为空。 不需要参数， 并返回布尔值。
size() 返回栈中的 item 数量。 不需要参数， 并返回一个整数。
exhibitStack() 显示栈中内容，以查找bug

'''
'''
class StackData:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack == []:
            print("the stack is empty")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def exhibitStack(self):
        for i in range(len(self.stack)):
            if i == len(self.stack) - 1:
                print(self.stack[i], end= '')
            else:
                print(self.stack[i], end='')
                print(" <- ", end= '')
        print("")


'''
'''
s.push(18)
s.push(12)

s.push('trur')

print(s.size())
print(s.peek())
s.exhibitStack()
print(s.isEmpty())
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print(s.isEmpty())

'''
# s = StackData()
# s.push([12,3,5])

