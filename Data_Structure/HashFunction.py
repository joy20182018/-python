# def Hash(astring, tablesize):
#     sum = 0
#     for pos in range(len(astring)):
#         sum = sum + ord(astring[pos])
#
#     return sum % tablesize
#
# print(Hash('cat', 100))
'''

map数据结构
Map() 创建一个新的 map 。 它返回一个空的 map 集合。
put(key， val) 向 map 中添加一个新的键值对。 如果键已经在 map 中， 那么用新值替换旧值。
get(key) 给定一个键， 返回存储在 map 中的值或 None。
del 使用 del map[key] 形式的语句从 map 中删除键值对。
len() 返回存储在 map 中的键值对的数量。
in 返回 True 对于 key in map 语句， 如果给定的键在 map 中， 否则为False

'''

class HashTable:   # 搜索性能O(1)
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #替换
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # 替换

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
        if position == startslot:
            stop = True

        return data

    def __getitem__(self, key):

        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)