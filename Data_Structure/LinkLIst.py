'''

无序链表的实现

'''
# coding=utf-8
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext



class UnoderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add_Head(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def addOtherData(self, item):
        pass

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current.getNext()
                count +=1
                print(count)
        return found


n = UnoderedList()
n.add_Head(10)
n.add_Head(76)
n.add_Head(1254)
print(n.search(10))
